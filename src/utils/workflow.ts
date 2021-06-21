import * as fs from "fs/promises";
import { lang2extension } from "lang2extension";
import { JSONFile, Low } from "lowdb";
import ora from "ora";
import path from "path";
import simpleGit from "simple-git";
import { UserInfo } from "../types/UserInfo";
import { fetchCode, requestAp } from "../utils/fetchCode.js";

const INITIAL_DATASET_STATE = {
  last_unix: 1623924394,
};

const sleep = (second: number) =>
  new Promise((resolve) => {
    setTimeout(() => {
      resolve("The request is successful.");
    }, 1000 * second);
  });

export const workflow = async (userId: string, dir?: string) => {
  const startTime = new Date().getTime();

  const baseDir = dir || process.cwd();
  const archiveDir = path.join(baseDir, `atcoder.jp/${userId}/`);
  const datasetFile = path.join(archiveDir, "dataset.json");

  await fs.mkdir(archiveDir, { recursive: true });

  await fs
    .access(datasetFile)
    .catch(() => fs.writeFile(datasetFile, JSON.stringify(INITIAL_DATASET_STATE, null, 2)));

  const database = new Low<{ last_unix: number }>(new JSONFile(datasetFile));
  await database.read();

  if (database.data) {
    const lastUnix = database.data.last_unix;

    // Atcoder Problems へリクエスト
    const getAllData = async (stack: UserInfo[], unix: number): Promise<UserInfo[]> => {
      const result = await requestAp(userId, unix + 1 || 0).then((data) =>
        data.filter((i) => i.result === "AC")
      );

      if (result.length) {
        const last_unix = result[result.length - 1].epoch_second;
        const spinner = ora("sleeping...zzz").start();
        await sleep(1);
        spinner.stop();
        spinner.clear();

        return getAllData(stack.concat(result), last_unix);
      } else {
        return stack;
      }
    };

    const submissions = await getAllData([], lastUnix);

    const saveSubmissions: UserInfo[] = [];
    const git = simpleGit(path.join(baseDir, `atcoder.jp/`));
    await git.init().addConfig("user.name", "ivgtr").addConfig("user.email", "ivgtr.me@gmail.com");

    // AtCoder へのスクレイピング
    for (let i = 0; i < submissions.length; i++) {
      const submission = submissions[i];

      const code = await fetchCode(submission);
      const extention = lang2extension(submission.language);
      const saveDir = path.join(archiveDir, submission.contest_id, submission.problem_id);
      const saveFile = path.join(saveDir, `${submission.id}${extention || ".txt"}`);

      await fs.mkdir(saveDir, { recursive: true });

      await fs.writeFile(saveFile, code).then(async () => {
        await git.add(saveFile);
        await git.commit(
          `[${submission.result}] ${submission.contest_id} ${submission.problem_id}`
        );
      });

      saveSubmissions.push(submission);

      const spinner = ora("sleeping...zzz").start();
      await sleep(1.5);
      spinner.stop();
      spinner.clear();

      const sessionTime = new Date().getTime();

      // 300秒経過してたら終了
      if (process.env.NODE_ENV === "production" && (sessionTime - startTime) / 1000 > 300) {
        break;
      }
    }

    if (saveSubmissions.length) {
      database.data.last_unix = saveSubmissions[saveSubmissions.length - 1].epoch_second;

      await database.write();
    }
    console.log(`done: ${saveSubmissions.length}件追加`);
  }
};
