import { Db } from "../types/DatabaseService";
import { workflow } from "../utils/workflow.js";

type Props = {
  db: Db;
};

export const archive = async ({ db }: Props) => {
  const result = db.getJson();
  if (!result?.user_id) return;
  console.log(`${result.user_id} のデータを取得します`);

  await workflow(result.user_id, result.archive_dir);
};
