import fs from "fs";
import path from "path";
import type { DbService } from "../utils/database.js";
import { getCode } from "../utils/getCode.js";

type Props = {
  db: DbService;
};

export const run = async ({ db }: Props) => {
  const code = await getCode();
  const archiveDir = path.join(db.getArchiveDir() || process.cwd(), "atcoder.jp");
  if (!fs.existsSync(archiveDir)) {
    fs.mkdirSync(archiveDir);
  }
  fs.writeFileSync(path.join(archiveDir, "test.py"), code);
};
