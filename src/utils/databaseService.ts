import * as fs from "fs";
import { JSONFileSync, LowSync } from "lowdb";
import { createRequire } from "module";
import path from "path";

const require = createRequire(import.meta.url);

export type ConfigSchema = {
  user_id: string;
  archive_dir: string;
};

const rootPath = path.join(
  process.env[process.platform === "win32" ? "USERPROFILE" : "HOME"] || ""
);

export class DbService {
  public readonly configDir: string;
  public readonly configFile: string;
  private readonly database: LowSync<{ config: ConfigSchema }>;

  constructor() {
    // 開発時はprocess.cwd() で管理する
    this.configDir = path.join(
      process.env.NODE_ENV !== "production" ? process.cwd() : rootPath,
      ".a3/"
    );
    this.configFile = path.join(this.configDir, "config.json");

    fs.mkdirSync(this.configDir, { recursive: true });

    try {
      fs.accessSync(path.join(this.configFile));
    } catch {
      const json = JSON.stringify(require("../configs/defaultConfig.json"), null, 2);
      fs.writeFileSync(this.configFile, json);
    }

    this.database = new LowSync<{ config: ConfigSchema }>(new JSONFileSync(this.configFile));
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

  // getArchiveDir() {
  //   this.database.read();
  //   if (this.database.data?.config) {
  //     const configs = this.database.data.config as ConfigSchema;
  //     return configs.archive_dir;
  //   }
  //   return undefined;
  // }

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
