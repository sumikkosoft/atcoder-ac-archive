#!/usr/bin/env node

import { program } from "commander";
import fs from "fs";
import path from "path";
import updateNotifier from "update-notifier";
import { fileURLToPath } from "url";
import * as commands from "./commands/index.js";
import { DbService, isDb } from "./utils/databaseService.js";

program
  .command("init")
  .description("初期設定")
  .action(() => {
    commands.init({ db: new DbService() });
  });

program
  .command("archive")
  .description("ソースコード取得の実行")
  .action(() => {
    if (isDb()) {
      commands.archive({ db: new DbService() });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });

const config = program
  .command("config")
  .description("コンフィグの確認・設定")
  .action(() => {
    if (isDb()) {
      commands.config({ db: new DbService() });
      config.help();
    } else {
      console.error("`a3 init` で初期化してください");
    }
  })
  .helpOption("-h, --help", "コマンド一覧を表示")
  .showHelpAfterError("`a3 config --help` でコマンドリストを確認してください");
config
  .command("user.id <USER_ID>")
  .description("登録しているuserIdを変更")
  .action((userId: string) => {
    if (isDb()) {
      commands.config({ db: new DbService(), userId });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });
config
  .command("archive.dir <ARCHIVE_DIR>")
  .description("登録しているarchiveDirを変更")
  .action((archiveDir: string) => {
    if (isDb()) {
      commands.config({ db: new DbService(), archiveDir });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });
config
  .command("gh.id <GITHUB_ID>")
  .description("登録しているgithubIdを変更")
  .action((ghId: string) => {
    if (isDb()) {
      commands.config({ db: new DbService(), ghId });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });
config
  .command("gh.email <GITHUB_EMAIL>")
  .description("登録しているgithubEmailを変更")
  .action((ghEmail: string) => {
    if (isDb()) {
      commands.config({ db: new DbService(), ghEmail });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });
config
  .command("gh.repo <GITHUB_REPOSITORY>")
  .description("登録しているgithubRepositoryを変更")
  .action((ghRepository: string) => {
    if (isDb()) {
      commands.config({ db: new DbService(), ghRepository });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });
config
  .command("open")
  .description("設定ファイルを保存しているディレクトリを開きます")
  .action(() => {
    if (isDb()) {
      commands.open({ db: new DbService() });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });

program.on("command:*", () => {
  console.error(
    "Invalid command: %s\n`a3 --help` でコマンドリストを確認してください",
    program.args.join(" ")
  );
});
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const cli = async (argv: string[]) => {
  const packageJson = JSON.parse(
    fs.readFileSync(path.resolve(__dirname, "../package.json")).toString()
  );

  updateNotifier({ pkg: packageJson }).notify();

  program
    .name("a3")
    .usage("[command]")
    .version(packageJson.version, "-v, --version", "a3-cliのバージョンを表示")
    .helpOption("-h, --help", "コマンド一覧を表示");

  await program.parseAsync(argv);
};

cli(process.argv);
