import prompts from "prompts";
import { Config, Db } from "../types/DatabaseService";

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
        name: "userId",
        message: "保存したいAtCoder のuserId",
        validate: (value: string) => (!value ? "Please enter." : true),
      },
      {
        type: "text",
        name: "archiveDir",
        message: "保存したいディレクトリの絶対パス",
        initial: "",
      },
    ],
    { onCancel }
  ).then<{ userId: string; archiveDir: string }>((input) => input);
};

export const init = async ({ db }: Props) => {
  try {
    const userInput = await inputUserData();

    const configs: Config = {
      user_id: userInput.userId,
      archive_dir: userInput.archiveDir,
    };
    const result = db.setConfig(configs);
    result ? console.log("登録完了") : console.error("登録できませんでした");
  } catch (e) {
    console.error(e);
  }
};
