import { Config, RegistarConfig } from "../../src/types/DatabaseService";

const INITIAL_CONFIG_STATE: { config: Config } = {
  config: { user_id: "", archive_dir: "", github_email: "", github_id: "" },
};

export class DbService {
  getConfigDir(): string {
    return "";
  }

  setConfig(configs: RegistarConfig) {
    return configs;
  }
  getJson(): Config {
    return INITIAL_CONFIG_STATE.config;
  }
}
