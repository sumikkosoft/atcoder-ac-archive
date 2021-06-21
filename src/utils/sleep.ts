export const sleep = (second: number) =>
  new Promise((resolve) => {
    setTimeout(() => {
      resolve("The request is successful.");
    }, 1000 * second);
  });
