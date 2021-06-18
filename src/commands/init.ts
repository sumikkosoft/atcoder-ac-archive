import prompts from "prompts";
import type { ConfigSchema, DbService } from "../utils/database.js";

type Props = {
  db: DbService;
};

const userInput = async () => {
  const onCancel = () => {
    throw new Error("Could not confirm your input, Try again");
  };

  return prompts(
    [
      {
        type: "text",
        name: "userId",
        message: "ソースコードを保存したいユーザーidを入力してください",
        validate: (value: string) => (!value ? "Please enter." : true),
      },
      {
        type: "text",
        name: "archiveDir",
        message: "保存したいディレクトリパスを入力してください(default: process.cwd())",
        initial: "",
      },
      {
        type: "confirm",
        name: "register",
        message: "登録します",
        initial: true,
      },
    ],
    { onCancel }
  ).then<{ userId: string; archiveDir: string; register: boolean }>((input) => input);
};

export const init = async ({ db }: Props) => {
  try {
    const input = await userInput();
    if (input.register) {
      const configs: ConfigSchema = {
        user_id: input.userId,
        archive_dir: input.archiveDir,
      };
      const result = db.setConfig(configs);
      result && console.log("登録完了");
    } else {
      console.error("登録しませんでした");
    }
  } catch (e) {
    console.error(e);
  }
};
