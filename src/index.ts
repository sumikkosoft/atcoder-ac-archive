import simpleGit from "simple-git";
import { workflow } from "./utils/workflow.js";

const main = async () => {
  if (process.env.NODE_ENV !== "production") {
    (await import("dotenv")).config();
  }
  const { USER_ID: userId, GITHUB_ID: githubId, GITHUB_EMAIL: githubEmail } = process.env;
  if (userId && githubId && githubEmail) {
    const git = simpleGit(process.cwd());

    await git.addConfig("user.name", githubId).addConfig("user.email", githubEmail);

    await git.fetch();
    const list = await git.branch();

    const brachName = `atcoder.jp/${userId}`;

    if (!list.all.includes(`remotes/origin/${brachName}`)) {
      await git.checkout(["--orphan", brachName]);
      await git.reset(["--hard"]);
    } else {
      await git.checkout([brachName]);
    }

    await workflow(git, userId);

    git.push("origin", brachName);
  } else console.error("設定が完了していません");
};

main();
