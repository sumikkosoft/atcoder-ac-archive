import type { DbService } from "../utils/database.js";

type Props = {
  db: DbService;
  userId?: string;
  archiveDir?: string;
};

export const config = async ({ db, userId, archiveDir }: Props) => {
  if (userId) {
    const result = db.setUserId(userId);
    result ? console.log(result) : console.error("エラー");
  } else if (archiveDir) {
    const result = db.setUserId(archiveDir);
    result ? console.log(result) : console.error("エラー");
  } else {
    const result = db.getJson();
    result
      ? console.log(
          `configs:\n  user_id: ${result.user_id}\n  archive_dir: ${result.archive_dir}\n`
        )
      : console.error("エラー");
  }
};
