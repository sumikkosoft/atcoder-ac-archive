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
        validate: (value: string) => (!value ? "入力してください" : true),
      },
      {
        type: "text",
        name: "archive_dir",
        message: "保存先の絶対パス、/atcoder-ac-archive ディレクトリが作られます",
        initial: "",
      },
      {
        type: "text",
        name: "github_id",
        message: "Git にコミットするid",
        validate: (value: string) => (!value ? "入力してください" : true),
      },
      {
        type: "text",
        name: "github_email",
        message: "Git にコミットするメールアドレス",
        validate: (value: string) => (!value ? "入力してください" : true),
      },
    ],
    { onCancel }
  ).then<Config>((input) => input);
};

export const init = async ({ db }: Props) => {
  try {
    const { user_id, archive_dir, github_email, github_id } = await inputUserData();

    const configs: Config = {
      user_id,
      archive_dir,
      github_email,
      github_id,
    };
    const result = db.setConfig(configs);
    result ? console.log("登録完了") : console.error("登録できませんでした");
  } catch (e) {
    console.error(e);
  }
};
