import fs from "fs";
import path from "path";
import JsonDb from "simple-json-db";
import defaultJson from "../configs/defaultConfig.json";

export type ConfigSchema = {
  user_id: string;
  archive_dir: string;
};

const rootPath = path.join(
  process.env[process.platform === "win32" ? "USERPROFILE" : "HOME"] || "",
  ".a3/config."
);

export class DbService {
  public readonly configPath: string;
  private readonly database: JsonDb;

  constructor() {
    this.configPath = path.join(process.cwd(), "config.json") || rootPath;
    if (fs.existsSync(this.configPath)) {
      this.database = new JsonDb(this.configPath);
    } else {
      fs.writeFileSync(this.configPath, JSON.stringify(defaultJson));
      this.database = new JsonDb(this.configPath);
    }
  }
  getUserId() {
    if (this.database.has("configs")) {
      const configs = this.database.get("configs") as ConfigSchema;
      return configs.user_id;
    }
    return undefined;
  }
  setUserId(id: string) {
    if (this.database.has("configs")) {
      const configs = this.database.get("configs") as ConfigSchema;
      this.database.set("configs", {
        ...configs,
        user_id: id,
      });

      return id;
    }
    return undefined;
  }
}
