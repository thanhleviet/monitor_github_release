This repo uses github action cronjob to frequently check release of some software. If there is a new release, it will notify via discord.

Github secrets:

- DISCORD_URL: discord webhook url
- DOCKERHUB_USERNAME: dockerhub username
- DOCKERHUB_TOKEN: dockerhub token key
- GH_TOKEN_KEY: github token key

![build-and-push-docker](https://github.com/thanhleviet/monitor_github_release/workflows/build-and-push-docker/badge.svg)