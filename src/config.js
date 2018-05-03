/* eslint-disable max-len */
/* jscs:disable maximumLineLength */
export const port = process.env.PORT;
export const host = process.env.WEBSITE_HOSTNAME || `localhost:${port}`;
const baseDirectory = '/';

export const config = {
  baseDirectory,
};
