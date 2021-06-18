import { Db } from "../types/DatabaseService";
import { workflow } from "../utils/workflow.js";

type Props = {
  db: Db;
};

export const run = async ({ db }: Props) => {
  const userId = db.getUserId();
  if (!userId) return;
  console.log(`${userId}のデータを取得します`);

  await workflow(userId);
};
