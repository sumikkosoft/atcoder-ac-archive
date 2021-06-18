import axios from "axios";
import { load } from "cheerio";
import { UserInfo } from "../types/UserInfo";

export const requestAp = async (user_id: string, unix: number) => {
  const url = `https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=${user_id}&from_second=${unix}`;
  return axios
    .get<UserInfo[]>(url, { headers: { "Accept-Encoding": "gzip" } })
    .then(({ data }) => data);
};

const requestHtml = async ({ contest_id, id }: UserInfo) => {
  const url = `https://atcoder.jp/contests/${contest_id}/submissions/${id}`;
  const html = axios
    .get<string>(url, {
      headers: { "Content-Type": "text/html" },
      responseType: "text",
    })
    .then(({ data }) => data);

  return html;
};

const parseHtml = async (html: string) => {
  const $ = load(html);
  const submissionCode = $("#submission-code").text();

  return submissionCode;
};

export const fetchCode = async (submission: UserInfo) => {
  const html = await requestHtml(submission);
  const submissionCode = await parseHtml(html);
  return submissionCode;
};
