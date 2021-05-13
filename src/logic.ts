import axios from "axios";
import fs from "fs";

const ENDPOINT_URL = "https://kenkoooo.com/atcoder/atcoder-api/results?user=";
const USER_NAME = "ivgtr";

export const logic = async () => {
  const json = await axios
    .get<UserData[]>(ENDPOINT_URL + USER_NAME, { headers: { "Accept-Encoding": "gzip" } })
    .then((response) => response.data);

  const tmp: {
    [contest_id: string]: {
      [problem_id: string]: { [language: string]: { id: number; epoch_second: number }[] };
    };
  } = {};

  json.map((i) => {
    if (i.result == "AC") {
      if (tmp[i.contest_id] !== undefined) {
        if (tmp[i.contest_id][i.problem_id] !== undefined) {
          if (tmp[i.contest_id][i.problem_id][i.language] !== undefined) {
            tmp[i.contest_id][i.problem_id][i.language].push({
              id: i.id,
              epoch_second: i.epoch_second,
            });
          } else {
            tmp[i.contest_id][i.problem_id][i.language] = [
              { id: i.id, epoch_second: i.epoch_second },
            ];
          }
        } else {
          tmp[i.contest_id][i.problem_id] = {
            [i.language]: [{ id: i.id, epoch_second: i.epoch_second }],
          };
        }
      } else {
        tmp[i.contest_id] = {
          [i.problem_id]: { [i.language]: [{ id: i.id, epoch_second: i.epoch_second }] },
        };
      }
    }
  });

  fs.writeFileSync("./test.json", JSON.stringify(tmp, null, 2));
};
