import fs from "fs";
import o from "open";

type Props = {
  dir: string;
};

export const open = ({ dir }: Props) => {
  fs.mkdirSync(dir, { recursive: true });

  return o(dir).then(() => true);
};
