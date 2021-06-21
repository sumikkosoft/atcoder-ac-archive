import * as fs from "fs";
import { JSONFileSync, LowSync } from "lowdb";
import path from "path";

export type ConfigSchema = {
  github_id: string;
  github_email: string;
  github_repository: string;
  user_id: string;
  archive_dir: string;
};

const INITIAL_CONFIG_STATE = {
  config: { user_id: "", archive_dir: "" },
};

const rootPath = process.env[process.platform === "win32" ? "USERPROFILE" : "HOME"] || "";

// 開発時はprocess.cwd() で管理する
const configDir = path.join(
  process.env.NODE_ENV !== "production" ? process.cwd() : rootPath,
  ".a3-cli/"
);
const configFile = path.join(configDir, "config.json");

export const isDb = () => {
  try {
    fs.accessSync(path.join(configFile));

    return true;
  } catch {
    return false;
  }
};

export class DbService {
  private readonly database!: LowSync<{ config: ConfigSchema }>;

  constructor() {
    this.database = this.init();
  }

  private init() {
    fs.mkdirSync(configDir, { recursive: true });

    try {
      fs.accessSync(path.join(configFile));
    } catch {
      const json = JSON.stringify(INITIAL_CONFIG_STATE, null, 2);
      fs.writeFileSync(configFile, json);
    }
    return new LowSync<{ config: ConfigSchema }>(new JSONFileSync(configFile));
  }

  getJson() {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config as ConfigSchema;
      return configs;
    }
    return undefined;
  }

  getUserId() {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config as ConfigSchema;
      return configs.user_id;
    }
    return undefined;
  }

  getArchiveDir() {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config as ConfigSchema;
      return configs.archive_dir;
    }
    return undefined;
  }

  getConfigDir() {
    return configDir;
  }

  setUserId(id: string) {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config as ConfigSchema;
      this.database.data.config = {
        ...configs,
        user_id: id,
      };
      this.database.write();

      return id;
    }
    return undefined;
  }

  setArchiveDir(dir: string) {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config as ConfigSchema;
      this.database.data.config = {
        ...configs,
        archive_dir: dir,
      };
      this.database.write();

      return dir;
    }
    return undefined;
  }

  setConfig(configs: ConfigSchema) {
    this.database.read();
    if (this.database.data?.config) {
      this.database.data.config = configs;
      this.database.write();

      return configs;
    }
    return undefined;
  }
}
