import type { DbService } from "../utils/database";

type Props = {
  db: DbService;
  args?: { change: string };
};

export const config = async ({ db, args }: Props) => {
  console.log(db.getUserId());
  console.log(args);
};
