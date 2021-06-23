import * as fs from "fs";
import { JSONFileSync, LowSync } from "lowdb";
import path from "path";

export type ConfigSchema = {
  github_id: string;
  github_email: string;
  user_id: string;
  archive_dir: string;
};

export type RegistarConfigSchema = {
  github_id?: string;
  github_email?: string;
  user_id?: string;
  archive_dir?: string;
};

const INITIAL_CONFIG_STATE: { config: ConfigSchema } = {
  config: { user_id: "", archive_dir: "", github_email: "", github_id: "" },
};

const rootPath = process.env[process.platform === "win32" ? "USERPROFILE" : "HOME"] || "";

const configDir = path.join(rootPath, ".a3/");
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

  setConfig(configs: RegistarConfigSchema) {
    this.database.read();
    if (this.database.data?.config) {
      const beforeConfigs = this.database.data.config as ConfigSchema;
      this.database.data.config = {
        ...beforeConfigs,
        ...configs,
      };
      this.database.write();

      return configs;
    }
    return undefined;
  }
}
