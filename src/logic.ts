import axios from "axios";
import fs from "fs";
import { lang2extension } from "lang2extension";

const ENDPOINT_URL = "https://kenkoooo.com/atcoder/atcoder-api/results?user=";
const USER_NAME = "chokudai";

export const logic = async () => {
  const json = await axios
    .get<UserData[]>(ENDPOINT_URL + USER_NAME, { headers: { "Accept-Encoding": "gzip" } })
    .then((response) => response.data);

  const tmp: {
    [contest_id: string]: {
      [problem_id: string]: {
        [language: string]: { id: number; epoch_second: number; extension: string }[];
      };
    };
  } = {};

  json.map((i) => {
    const extension = lang2extension(i.language);
    if (extension) {
      if (i.result == "AC") {
        if (tmp[i.contest_id] !== undefined) {
          if (tmp[i.contest_id][i.problem_id] !== undefined) {
            if (tmp[i.contest_id][i.problem_id][i.language] !== undefined) {
              tmp[i.contest_id][i.problem_id][i.language].push({
                id: i.id,
                epoch_second: i.epoch_second,
                extension,
              });
            } else {
              tmp[i.contest_id][i.problem_id][i.language] = [
                { id: i.id, epoch_second: i.epoch_second, extension },
              ];
            }
          } else {
            tmp[i.contest_id][i.problem_id] = {
              [i.language]: [{ id: i.id, epoch_second: i.epoch_second, extension }],
            };
          }
        } else {
          tmp[i.contest_id] = {
            [i.problem_id]: {
              [i.language]: [{ id: i.id, epoch_second: i.epoch_second, extension }],
            },
          };
        }
      }
    }
  });

  fs.writeFileSync("./test.json", JSON.stringify(tmp, null, 2));
};
