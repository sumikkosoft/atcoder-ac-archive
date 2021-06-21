import o from "open";
import { Db } from "../types/DatabaseService";

type Props = {
  db: Db;
};

export const open = ({ db }: Props) => {
  const dir = db.getConfigDir();
  o(dir);
};
