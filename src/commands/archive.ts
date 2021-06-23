import simpleGit from "simple-git";
import type { Db } from "../types/DatabaseService";
import { workflow } from "../utils/workflow.js";

type Props = {
  db: Db;
};

export const archive = async ({ db }: Props) => {
  const result = db.getJson();
  if (!result?.user_id) return;
  console.log(`${result.user_id} のデータを取得します`);

  const git = simpleGit(result.archive_dir);

  await git
    .init()
    .addConfig("user.name", result.github_id)
    .addConfig("user.email", result.github_email);

  if (result.github_repository) {
    await git.addRemote("origin", result.github_repository);
  }

  await git.fetch();
  const list = await git.branch();

  const brachName = `atcoder.jp/${result.user_id}`;

  if (!list.all.includes(`remotes/origin/${brachName}`)) {
    await git.checkout(["--orphan", brachName]);
    await git.reset(["--hard"]);
  } else {
    await git.pull(["origin", `${brachName}/${brachName}`]);
    await git.checkout([brachName]);
  }

  await workflow(git, result.user_id, result.archive_dir);
};
