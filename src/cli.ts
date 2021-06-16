#!/usr/bin/env node

import { program } from "commander";
import pjson from "pjson";
import updateNotifier from "update-notifier";
import * as commands from "./commands";
import { DbService } from "./utils/database";

const initializeDb = () => {
  const db = new DbService();
  return db;
};

program
  .command("init")
  .description("初期化します")
  .action(() => {
    const db = initializeDb();
    commands.init({ db });
  });

program
  .command("run")
  .description("ソースコードを取得します")
  .action(() => {
    const db = initializeDb();
    if (db.getUserId()) {
      commands.run({ db });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });

const config = program
  .command("config")
  .description("コンフィグの確認・設定")
  .action(() => {
    const db = initializeDb();
    if (db.getUserId()) {
      commands.config({ db });
      config.help();
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });
config
  .command("user.id <USER_ID>")
  .description("登録しているuserIdを変更します")
  .action((userId: string) => {
    const db = initializeDb();
    if (db.getUserId()) {
      commands.config({ db, userId });
    } else {
      console.error("`a3 init` で初期化してください");
    }
  });
config
  .command("archive.dir <ARCHIVE_DIR>")
  .description("登録しているarchiveDirを変更します")
  .action((archiveDir: string) => {
    const db = initializeDb();
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

export default (() => {
  updateNotifier({ pkg: pjson }).notify();

  program
    .name("a3")
    .usage("[command]")
    .version(pjson.version, "-v, --version", "a3-cliのバージョンを表示します")
    .helpOption("-h, --help", "コマンド一覧を表示します")
    .parse(process.argv);
})();
