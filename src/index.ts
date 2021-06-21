import { workflow } from "./utils/workflow.js";

export default (async () => {
  if (process.env.NODE_ENV !== "production") {
    (await import("dotenv")).config();
  }
  const id = process.env.USER_ID;
  if (id) await workflow(id);
  else console.error("idが設定されていません");
})();
