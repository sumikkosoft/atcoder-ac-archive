import o from "open";

type Props = {
  dir: string;
};

export const open = ({ dir }: Props) => o(dir).then(() => true);
