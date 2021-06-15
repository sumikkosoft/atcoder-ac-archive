import { workflow } from "./workflow";

export default (async () => {
  if (process.env.NODE_ENV !== "production") {
    (await import("dotenv")).config();
  }
  workflow();
})();
