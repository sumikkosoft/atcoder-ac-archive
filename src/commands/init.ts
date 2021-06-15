import { DbService } from "../utils/database";

export const init = async () => {
  const db = new DbService();
  if (db.getUserId()) {
    console.log(db.getUserId());
  } else {
    const result = db.setUserId("ivgtr");
    console.log(result);
  }
};
