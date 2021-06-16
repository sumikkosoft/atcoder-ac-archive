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
  .command("init <USER_ID>")
  .description("register ID")
  .action((userId) => {
    const db = initializeDb();
    commands.init({ db, userId });
  });

program
  .command("run")
  .description("get your AC code")
  .action(() => {
    const db = initializeDb();
    commands.run({ db });
  });

program
  .command("config")
  .description("change your registered ID")
  .arguments("[]")
  .hook("preAction", (thisCommand, _actionCommand) => {
    thisCommand.help();
  })
  .action((a, b, c, d) => {
    console.log(a);
    console.log(b);
    console.log(c.name());
    console.log(d);
  });

program.on("command:*", () => {
  console.error(
    "Invalid command: %s\nUse `a3 --help` for a list of available commands.",
    program.args.join(" ")
  );
});

export default (() => {
  updateNotifier({ pkg: pjson }).notify();

  program
    .name("a3")
    .usage("[command]")
    .version(pjson.version, "-v, --version", "Show the a3-cli's version")
    .helpOption("-h, --help", "display help for command")
    .parse(process.argv);
})();
