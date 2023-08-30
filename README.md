<p align="center">
  <a href="https://nickfausti.com">
    <img src="me.jpeg" height="96" style="border-radius: 100%;">
    <h3 align="center">Nick Fausti | Bascom Hunter Demo</h3>
  </a>
</p>

<p align="center">Next.js frontend with <a href="https://flask.palletsprojects.com/">Flask</a> as the API backend.</p>

<br/>

## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and Flask as the API backend. I will use the Next.js app to access Python AI libraries + time series data on the backend.

## How It Works

The Python/Flask server is mapped into to Next.js app under `/api/`.

This is implemented using [`next.config.js` rewrites](https://github.com/vercel/examples/blob/main/python/nextjs-flask/next.config.js) to map any request to `/api/:path*` to the Flask API, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:5328` port, which is where the Flask server is running.

In production, the Flask server is hosted as [Python serverless functions](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python) on Vercel.

## Demo

ADD DEMO LINK HERE

## Developing Locally

You can clone & create this repo with the following command

```bash
npx create-next-app nextjs-flask --example "https://github.com/ncfausti/bh-demo/tree/main/"
```

## Getting Started

First, install the dependencies:

```bash
npm install
# or
yarn
# or
pnpm install
```

Then, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The Flask server will be running on [http://127.0.0.1:5328](http://127.0.0.1:5328) – feel free to change the port in `package.json` (you'll also need to update it in `next.config.js`).

## Learn More

To learn more take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/) - learn about Flask features and API.
- [InfluxDB Documentation](https://www.influxdata.com/blog/getting-started-influxdb-grafana/) - learn about getting started with InfluxDB.
