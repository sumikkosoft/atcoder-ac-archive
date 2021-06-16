import type { DbService } from "../utils/database";

type Props = {
  db: DbService;
};

export const run = ({ db }: Props) => {
  console.log(db.getUserId());
};
