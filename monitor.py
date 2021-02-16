#!/usr/bin/env python
import yaml
from github import Github
from tinydb import TinyDB, Query
import os
from discord_webhook import DiscordWebhook as DWH
DISCORD_URL = os.getenv("DISCORD_URL")

db = TinyDB('db.json')

if __name__ == "__main__":
    discord = DWH(url = DISCORD_URL)
    g = Github()
    with open("git_repos.yml") as yml_file:
        repos = yaml.load(yml_file, Loader=yaml.FullLoader)
        software = Query()
        for repo in repos:
            software_name = db.search(software.name == repo)
            #github
            rp = g.get_repo(repo)
            rls = rp.get_latest_release()
            if len(software_name) == 0:
                db.insert({'name': repo, 'version': rls.tag_name, 'date': str(rls.published_at)})
            else:
                if software_name[0]['version'] != rls.tag_name:
                    db.update({'version': rls.tag_name}, software.name == repo)
                    print(software_name[0].name)
                    discord.content = f"New realese: **{software.name}** *{rls.tag_name}* at {rls.published_at}"
                    discord.execute()
                else:
                    print(f"{repo} has no update. Its current version is {rls.tag_name} released on {rls.published_at}")
                    discord.content = f"**{repo}** has no update. Its current version is **{rls.tag_name}** released on {rls.published_at}"
                    discord.execute()
