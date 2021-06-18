import * as fs from "fs";
import { JSONFileSync, LowSync } from "lowdb";
import { createRequire } from "module";
import path from "path";
import * as url from "url";

const require = createRequire(import.meta.url);
const __filename = url.fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export type ConfigSchema = {
  user_id: string;
  archive_dir: string;
};

const rootPath = path.join(
  process.env[process.platform === "win32" ? "USERPROFILE" : "HOME"] || ""
);

export class DbService {
  public readonly configPath: string;
  private readonly database: LowSync<{ config: ConfigSchema[] }>;

  constructor() {
    // 開発時はprocess.cwd() で管理する
    this.configPath = process.cwd() || rootPath || __dirname;
    fs.mkdirSync(path.join(this.configPath, ".a3/"), { recursive: true });

    try {
      fs.accessSync(path.join(this.configPath, ".a3/config.json"));
    } catch {
      const json = JSON.stringify(require("../configs/defaultConfig.json"), null, 2);
      fs.writeFileSync(path.join(this.configPath, ".a3/config.json"), json);
    }

    this.database = new LowSync<{ config: ConfigSchema[] }>(
      new JSONFileSync(path.join(this.configPath, ".a3/config.json"))
    );
  }

  getJson() {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config[0] as ConfigSchema;
      return configs;
    }
    return undefined;
  }

  getUserId() {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config[0] as ConfigSchema;
      return configs.user_id;
    }
    return undefined;
  }

  getArchiveDir() {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config[0] as ConfigSchema;
      return configs.archive_dir;
    }
    return undefined;
  }

  setUserId(id: string) {
    this.database.read();
    if (this.database.data?.config) {
      const configs = this.database.data.config[0] as ConfigSchema;
      this.database.data.config[0] = {
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
      const configs = this.database.data.config[0] as ConfigSchema;
      this.database.data.config[0] = {
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
    console.log(this.database.data);
    if (this.database.data?.config) {
      this.database.data.config[0] = configs;
      this.database.write();

      return configs;
    }
    return undefined;
  }
}
