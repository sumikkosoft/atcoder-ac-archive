import axios from "axios";
import { load } from "cheerio";
import * as fs from "fs/promises";
import { lang2extension } from "lang2extension";
import ora from "ora";
import path from "path";
import type { SimpleGit } from "simple-git";
import type { UserInfo } from "../types/UserInfo";
import { sleep } from "./sleep.js";

const requestHtml = async ({ contest_id, id }: UserInfo) => {
  const url = `https://atcoder.jp/contests/${contest_id}/submissions/${id}`;
  const html = axios
    .get<string>(url, {
      headers: { "Content-Type": "text/html" },
      responseType: "text",
    })
    .then(({ data }) => data);

  return html;
};

const parseHtml = async (html: string) => {
  const $ = load(html);
  const submissionCode = $("#submission-code").text();

  return submissionCode;
};

export const fetchCode = async (submission: UserInfo) => {
  const html = await requestHtml(submission);
  const submissionCode = await parseHtml(html);
  return submissionCode;
};

export const fetchAllCode = async (
  baseDir: string,
  startTime: number,
  submissions: UserInfo[],
  git: SimpleGit
) => {
  const saveSubmissions: UserInfo[] = [];

  // AtCoder へのスクレイピング
  for (let i = 0; i < submissions.length; i++) {
    const submission = submissions[i];

    const code = await fetchCode(submission);
    const extention = lang2extension(submission.language);
    const saveDir = path.join(baseDir, submission.contest_id, submission.problem_id);
    const saveFile = path.join(saveDir, `${submission.id}${extention || ".txt"}`);

    await fs.mkdir(saveDir, { recursive: true });

    await fs.writeFile(saveFile, code).then(async () => {
      await git.add(saveFile);
      await git.commit(`[${submission.result}] ${submission.contest_id} ${submission.problem_id}`);
    });

    saveSubmissions.push(submission);

    const spinner = ora("sleeping...zzz").start();
    await sleep(1.5);
    spinner.stop();
    spinner.clear();

    const sessionTime = new Date().getTime();

    // 300秒経過してたら終了
    if (process.env.CI && (sessionTime - startTime) / 1000 > 300) {
      break;
    }
  }

  return saveSubmissions;
};
