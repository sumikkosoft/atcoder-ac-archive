import * as fs from "fs/promises";
import { JSONFile, Low } from "lowdb";
import path from "path";
import type { SimpleGit } from "simple-git";
import { fetchAllCode } from "../utils/fetchCode.js";
import { getAllSubmissions } from "./getSubmissions.js";

const INITIAL_DATASET_STATE = {
  last_unix: 0,
};

export const workflow = async (git: SimpleGit, userId: string, dir?: string) => {
  const startTime = new Date().getTime();

  const baseDir = dir || process.cwd();
  const archiveDir = path.join(baseDir, `atcoder.jp/${userId}`);
  const datasetFile = path.join(archiveDir, "dataset.json");

  await fs.mkdir(archiveDir, { recursive: true });

  await fs
    .access(datasetFile)
    .catch(() => fs.writeFile(datasetFile, JSON.stringify(INITIAL_DATASET_STATE, null, 2)));

  const database = new Low<{ last_unix: number }>(new JSONFile(datasetFile));
  await database.read();

  if (database.data) {
    const lastUnix = database.data.last_unix;

    const submissions = await getAllSubmissions(userId, lastUnix);

    const saveSubmissions = await fetchAllCode(archiveDir, startTime, submissions, git);

    if (saveSubmissions.length) {
      database.data.last_unix = saveSubmissions[saveSubmissions.length - 1].epoch_second;

      await database.write();

      await git.add(datasetFile);
      await git.commit("Update: Last UNIX Data");
    }
    console.log(`done: ${saveSubmissions.length}件追加`);
  }
};
