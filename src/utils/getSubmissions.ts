import axios from "axios";
import ora from "ora";
import type { UserInfo } from "../types/UserInfo";
import { sleep } from "./sleep.js";

export const requestAp = async (user_id: string, unix: number) => {
  const url = `https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=${user_id}&from_second=${unix}`;
  return axios
    .get<UserInfo[]>(url, { headers: { "Accept-Encoding": "gzip" } })
    .then(({ data }) => data);
};

export const getAllSubmissions = async (userId: string, lastUnix: number) => {
  // Atcoder Problems へリクエスト
  const getAllData = async (stack: UserInfo[], unix: number): Promise<UserInfo[]> => {
    const result = await requestAp(userId, unix + 1 || 0).then((data) =>
      data.filter((i) => i.result === "AC")
    );

    if (result.length) {
      const last_unix = result[result.length - 1].epoch_second;
      const spinner = ora("sleeping...zzz").start();
      await sleep(1);
      spinner.stop();
      spinner.clear();

      return getAllData(stack.concat(result), last_unix);
    } else {
      return stack;
    }
  };

  return getAllData([], lastUnix);
};
