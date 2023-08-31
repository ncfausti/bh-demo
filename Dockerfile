#  ---- Build NextJS App ----
# FROM node:16 AS builder
# WORKDIR /app
# COPY package.json pnpm-lock.yaml ./
# RUN npm install -g pnpm
# RUN pnpm install
# COPY ./app/ /app/app/
# COPY ./public/ /app/public/
# WORKDIR /app/app
# RUN pnpm run build

# # ---- Python API Backend ----
# FROM python:3.9
# WORKDIR /app

# # Copy the built Next.js app
# COPY --from=builder /app/.next ./.next
# COPY --from=builder /app/public ./public

# # Install Python dependencies
# COPY requirements.txt ./
# RUN pip install -r requirements.txt

# # Copy flask app
# COPY ./api ./api

# # Install dependencies for Next.js
# COPY package.json ./package.json
# # RUN npm install -g pnpm
# # RUN pnpm install

# # Environment variable for Flask
# ENV FLASK_APP=api/index

# # Expose the port the app runs on
# EXPOSE 3000
# EXPOSE 5328

# # Command to run the application
# CMD ["sh", "-c", "cd app && pnpm run start & FLASK_DEBUG=1 FLASK_RUN_PORT=5328 python3 -m flask run"]


#### WORKS FOR NEXTJS ONLY ####


FROM node:18-alpine AS base

# Install dependencies only when needed
FROM base AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Install dependencies based on the preferred package manager
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./
RUN \
    if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
    elif [ -f package-lock.json ]; then npm ci; \
    elif [ -f pnpm-lock.yaml ]; then yarn global add pnpm && pnpm i --frozen-lockfile; \
    else echo "Lockfile not found." && exit 1; \
    fi


# Rebuild the source code only when needed
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry during the build.
# ENV NEXT_TELEMETRY_DISABLED 1

RUN yarn build

# If using npm comment out above and use below instead
# RUN npm run build

# Production image, copy all the files and run next
FROM base AS runner
WORKDIR /app

ENV NODE_ENV production
# Uncomment the following line in case you want to disable telemetry during runtime.
# ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public

# Automatically leverage output traces to reduce image size
# https://nextjs.org/docs/advanced-features/output-file-tracing
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT 3000
# set hostname to localhost
ENV HOSTNAME "0.0.0.0"

CMD ["node", "server.js"]