import os
import json
from classes.post import Post
from pathlib import Path

ROOT_DIR = os.path.abspath(os.curdir)

if __name__ == "__main__":

    newPost = Post("Went to ShareteaUCI today! ")
    foo = ROOT_DIR + "/public/data.json"
    new_path = Path(foo)

    with open(new_path, "w") as outfile:
        json.dump(newPost.__dict__, outfile)
