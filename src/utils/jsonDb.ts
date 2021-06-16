import fs from "fs";

type JsonSchema = {
  [key: string]: any;
};

const validateJSON = (fileContent: string) => {
  try {
    JSON.parse(fileContent);
  } catch {
    throw new Error("Given filePath is not empty and its content is not valid JSON.");
  }
  return true;
};

export class JsonDbUtil {
  public readonly storage: JsonSchema;
  public readonly filePath: string;
  constructor(filePath: string) {
    this.filePath = filePath;
    this.storage = {};
    const stats = fs.statSync(filePath);

    try {
      fs.accessSync(filePath, fs.constants.R_OK | fs.constants.W_OK);
    } catch {
      throw new Error(`Cannot read & write on path "${filePath}". Check permissions!`);
    }

    if (stats.size > 0) {
      const data = fs.readFileSync(filePath, "utf-8");
      if (validateJSON(data)) this.storage = JSON.parse(data);
    }
  }
  has(key: string) {
    return Object.prototype.hasOwnProperty.call(this.storage, key);
  }
  get(key: string) {
    return this.has(key) ? this.storage[key] : undefined;
  }
  set(key: string, value: any) {
    this.storage[key] = value;
    this.sync();
  }
  sync() {
    fs.writeFileSync(this.filePath, JSON.stringify(this.storage, null, 2));
  }
}
