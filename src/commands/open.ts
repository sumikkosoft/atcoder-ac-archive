import o from "open";
import type { Db } from "../types/DatabaseService";

type Props = {
  db: Db;
};

export const openDir = (dir: string) => o(dir).then(() => true);

export const open = ({ db }: Props) => {
  const dir = db.getConfigDir();
  return openDir(dir);
};
