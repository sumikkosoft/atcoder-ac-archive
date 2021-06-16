import fs from "fs";
import path from "path";
import defaultJson from "../configs/defaultConfig.json";
import { JsonDbUtil } from "./jsonDb";

export type ConfigSchema = {
  user_id: string;
  archive_dir: string;
};

const rootPath = path.join(
  process.env[process.platform === "win32" ? "USERPROFILE" : "HOME"] || ""
);

const configTree = ".a3/config.json";

const checkPath = (configPath: string) => {
  try {
    fs.accessSync(path.join(configPath, ".a3"));
    fs.accessSync(path.join(configPath, configTree));
    return true;
  } catch {
    return false;
  }
};

export class DbService {
  public readonly configPath: string;
  private readonly database: JsonDbUtil;

  constructor(_configPath?: string) {
    // 開発時はprocess.cwd() で管理する
    this.configPath = process.cwd() || rootPath;

    if (checkPath(this.configPath)) {
      this.database = new JsonDbUtil(path.join(this.configPath, configTree));
    } else {
      fs.mkdirSync(path.join(this.configPath, ".a3"));
      fs.writeFileSync(path.join(this.configPath, configTree), JSON.stringify(defaultJson));
      this.database = new JsonDbUtil(path.join(this.configPath, configTree));
    }
  }

  getJson() {
    if (this.database.has("configs")) {
      const configs = this.database.get("configs") as ConfigSchema;
      return configs;
    }
    return undefined;
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
  getArchiveDir() {
    if (this.database.has("configs")) {
      const configs = this.database.get("configs") as ConfigSchema;
      return configs.archive_dir;
    }
    return undefined;
  }
  setArchiveDir(dir: string) {
    if (this.database.has("configs")) {
      const configs = this.database.get("configs") as ConfigSchema;
      this.database.set("configs", {
        ...configs,
        archiveDir: dir,
      });

      return dir;
    }
    return undefined;
  }
  setConfig(cnofigs: ConfigSchema) {
    if (this.database.has("configs")) {
      this.database.set("configs", {
        ...cnofigs,
      });

      return cnofigs;
    }
    return undefined;
  }
}
