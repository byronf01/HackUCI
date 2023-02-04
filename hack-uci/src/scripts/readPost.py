from pathlib import Path
import json
import os
import sys

ROOT_DIR = os.path.abspath(os.curdir)

from ..classes.post import Post


if __name__ == "__main__":

    newFile = ROOT_DIR + "/public/new_posts.json"
    new_path = Path(newFile)

    f = open(new_path)
    data = json.load(f)
    new_posts = dict()

    for post in data[0]:
        print(post)
