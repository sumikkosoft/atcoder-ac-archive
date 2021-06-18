#!/usr/bin/env node

import { program } from "commander";
import pjson from "pjson";
import updateNotifier from "update-notifier";
import * as commands from "./commands/index.js";
import { DbService } from "./utils/databaseService.js";

const db = new DbService();

program
  .command("init")
  .description("初期設定")
  .action(() => {
    commands.init({ db });
  });

program
  .command("archive")
  .description("ソースコード取得の実行")
  .action(() => {
    if (db.getUserId()) {
      commands.archive({ db });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });

const config = program
  .command("config")
  .description("コンフィグの確認・設定")
  .action(() => {
    if (db.getUserId()) {
      commands.config({ db });
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
    if (db.getUserId()) {
      commands.config({ db, userId });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });
config
  .command("archive.dir <ARCHIVE_DIR>")
  .description("登録しているarchiveDirを変更")
  .action((archiveDir: string) => {
    if (db.getUserId()) {
      commands.config({ db, archiveDir });
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

updateNotifier({ pkg: pjson }).notify();

program
  .name("a3")
  .usage("[command]")
  .version(pjson.version, "-v, --version", "a3-cliのバージョンを表示")
  .helpOption("-h, --help", "コマンド一覧を表示")
  .parse(process.argv);
