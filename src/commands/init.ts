import prompts from "prompts";
import type { Config, Db } from "../types/DatabaseService";

type Props = {
  db: Db;
};

const inputUserData = async () => {
  const onCancel = () => {
    throw new Error("Could not confirm your input, Try again");
  };

  return prompts(
    [
      {
        type: "text",
        name: "user_id",
        message: "保存したいAtCoder のuserId",
        validate: (value: string) => (!value ? "Please enter." : true),
      },
      {
        type: "text",
        name: "archive_dir",
        message: "保存したいディレクトリの絶対パス",
        initial: "",
      },
      {
        type: "text",
        name: "github_id",
        message: "Git にコミットするid",
        initial: "",
      },
      {
        type: "text",
        name: "github_email",
        message: "Git にコミットするメールアドレス",
        validate: (value: string) => (!value ? "Please enter." : true),
      },
      {
        type: "text",
        name: "github_repository",
        message: "GitHub Repository URL",
        initial: "",
      },
    ],
    { onCancel }
  ).then<Config>((input) => input);
};

export const init = async ({ db }: Props) => {
  try {
    const { user_id, archive_dir, github_email, github_id, github_repository } =
      await inputUserData();

    const configs: Config = {
      user_id,
      archive_dir,
      github_email,
      github_id: github_id || user_id,
      github_repository,
    };
    const result = db.setConfig(configs);
    result ? console.log("登録完了") : console.error("登録できませんでした");
  } catch (e) {
    console.error(e);
  }
};
