import axios from "axios";
import { load } from "cheerio";

type SubmissionsData = {
  id: number;
  epoch_second: number;
  problem_id: string;
  contest_id: string;
  user_id: string;
  language: string;
  point: number;
  length: number;
  result: string;
  execution_time: number;
};

export const requestHtml = async (submissionsData: SubmissionsData) => {
  const url = `https://atcoder.jp/contests/${submissionsData.contest_id}/submissions/${submissionsData.id}`;
  const html = axios
    .get<string>(url, {
      headers: { "Content-Type": "text/html" },
      responseType: "text",
    })
    .then(({ data }) => data);

  return html;
};

export const parseHtml = async (html: string) => {
  const $ = load(html);
  const code = $("#submission-code").text();

  return code;
};

export const getCode = async () => {
  const sub: SubmissionsData = {
    id: 23310218,
    epoch_second: 1623230372,
    problem_id: "abc198_b",
    contest_id: "abc198",
    user_id: "ivgtr",
    language: "Python (3.8.2)",
    point: 200,
    length: 146,
    result: "AC",
    execution_time: 24,
  };
  const html = await requestHtml(sub);
  const code = await parseHtml(html);
  return code;
};
