import type { Db, RegistarConfig } from "../types/DatabaseService";

type Props = {
  db: Db;
  userId?: string;
  archiveDir?: string;
  ghId?: string;
  ghEmail?: string;
  ghRepository?: string;
};

export const config = async ({ db, userId, archiveDir, ghId, ghEmail, ghRepository }: Props) => {
  if (userId || archiveDir || ghId || ghEmail || ghRepository) {
    const configs: RegistarConfig = {};
    if (userId) configs.user_id = userId;
    if (archiveDir) configs.archive_dir = archiveDir;
    if (ghId) configs.github_id = ghId;
    if (ghEmail) configs.github_email = ghEmail;
    if (ghRepository) configs.github_repository = ghRepository;

    const result = db.setConfig(configs);
    result ? console.log(result) : console.error("エラー");
    return result;
  } else {
    const result = db.getJson();
    result
      ? console.log(
          `configs:\n  user_id: ${result.user_id}\n  archive_dir: ${result.archive_dir}\n  github_id: ${result.github_id}\n  github_email: ${result.github_email}\n  github_repository: ${result.github_repository}\n`
        )
      : console.error("エラー");
    return result;
  }
};
