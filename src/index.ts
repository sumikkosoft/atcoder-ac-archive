import simpleGit from "simple-git";
import { workflow } from "./utils/workflow.js";

const main = async () => {
  if (!process.env.CI) {
    (await import("dotenv")).config();
  }
  const { USER_ID: user_id, GITHUB_ID: github_id, GITHUB_EMAIL: github_email } = process.env;
  if (user_id && github_id && github_email) {
    const git = simpleGit(process.cwd());

    await git.addConfig("user.name", github_id).addConfig("user.email", github_email);

    await git.fetch();
    const list = await git.branch();

    const brachName = `atcoder.jp/${user_id}`;

    if (!list.all.includes(`remotes/origin/${brachName}`)) {
      await git.checkout(["--orphan", brachName]);
      await git.reset(["--hard"]);
    } else {
      await git.checkout([brachName]);
    }

    await workflow(git, user_id);

    git.push("origin", brachName);
  } else console.error("設定が完了していません");
};

main();
