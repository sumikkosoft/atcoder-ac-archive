#!/usr/bin/env node

import { program } from "commander";
import pjson from "pjson";
import updateNotifier from "update-notifier";
import * as commands from "./commands";

program.command("init").alias("i").description("register ID").action(commands.init);

program.command("run").alias("r").description("get your AC code").action(commands.run);

program
  .command("config")
  .alias("c")
  .option("-c, --change [USER_ID]", "Change a User ID", "")
  .description("change your registered ID")
  .action(commands.config);

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
