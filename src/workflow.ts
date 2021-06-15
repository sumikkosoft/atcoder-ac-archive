import path from "path";

export const workflow = () => {
  console.log("start workflow");

  const current = path.join(process.cwd());

  console.log(current);
};
