import fs from "fs";
import path from "path";
import { Db } from "../types/DatabaseService";
import { fetchCode } from "../utils/fetchCode.js";

type Props = {
  db: Db;
};

export const run = async ({ db }: Props) => {
  const code = await fetchCode();
  const archiveDir = path.join(db.getArchiveDir() || process.cwd(), "atcoder.jp");
  if (!fs.existsSync(archiveDir)) {
    fs.mkdirSync(archiveDir);
  }
  fs.writeFileSync(path.join(archiveDir, "test.py"), code);
};
