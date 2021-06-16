import type { DbService } from "../utils/database";

type Props = {
  db: DbService;
  userId: string;
};

export const init = async ({ db, userId }: Props) => {
  const result = db.setUserId(userId);
  console.log(result);
};
