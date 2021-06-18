import * as fs from "fs/promises";
import { lang2extension } from "lang2extension";
import { JSONFile, Low } from "lowdb";
import { createRequire } from "module";
import ora from "ora";
import path from "path";
import { UserInfo } from "../types/UserInfo";
import { fetchCode, requestAp } from "../utils/fetchCode.js";

const require = createRequire(import.meta.url);

const sleep = (second: number) =>
  new Promise((resolve) => {
    setTimeout(() => {
      resolve("The request is successful.");
    }, 1000 * second);
  });

export const workflow = async (userId: string) => {
  const archiveDir = path.join(process.cwd(), `atcoder.jp/${userId}/`);
  const datasetFile = path.join(archiveDir, "dataset.json");

  await fs.mkdir(archiveDir, { recursive: true });

  await fs.access(datasetFile).catch(() => {
    const json = require("../configs/defaultDataset.json");

    return fs.writeFile(datasetFile, JSON.stringify(json, null, 2));
  });

  const database = new Low<{ last_unix: number; dataset: UserInfo[] }>(new JSONFile(datasetFile));
  await database.read();

  if (database.data) {
    const lastUnix = database.data.last_unix;

    const getAllData = async (stack: UserInfo[], unix: number): Promise<UserInfo[]> => {
      const result = await requestAp(userId, unix + 1 || 0).then((data) =>
        data.filter((i) => i.result === "AC")
      );

      if (result.length) {
        const last_unix = result[result.length - 1].epoch_second;
        const spinner = ora("sleeping...zzz").start();
        await sleep(0.5);
        spinner.stop();
        spinner.clear();
        return getAllData(stack.concat(result), last_unix);
      } else {
        return stack;
      }
    };

    const submissions = await getAllData([], lastUnix);

    const saveSubmissions: UserInfo[] = [];

    for (let i = 0; i < submissions.length; i++) {
      const submission = submissions[i];

      const code = await fetchCode(submission);
      const extention = lang2extension(submission.language);
      const saveDir = path.join(archiveDir, submission.contest_id, submission.problem_id);

      await fs.mkdir(saveDir, { recursive: true });

      await fs.writeFile(path.join(saveDir, `${submission.id}${extention}`), code);

      saveSubmissions.push(submission);

      const spinner = ora("sleeping...zzz").start();
      await sleep(1);
      spinner.stop();
      spinner.clear();
    }

    if (saveSubmissions.length) {
      database.data.dataset = database.data.dataset.concat(saveSubmissions);
      database.data.last_unix = saveSubmissions[saveSubmissions.length - 1].epoch_second;

      await database.write();
    }
    console.log(`done: ${saveSubmissions.length}件追加`);
  }
};
