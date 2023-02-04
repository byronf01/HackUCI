from pathlib import Path
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.classes.post import Post

if __name__ == "__main__":

    newFile = os.path.join(
        os.path.dirname(__file__), "..", "..", "public", "new_posts.json"
    )
    new_path = Path(newFile)

    f = open(new_path)
    data = json.load(f)
    new_posts = dict()

    for p in data["posts"]:
        new_post = Post(
            p["date"],
            p["image"],
            p["description"],
            p["tags"],
            p["likes"],
            p["comments"],
        )
        new_posts[Post.ID] = new_post

    for id, p in new_posts.items():
        print(str(id) + ": " + p.description)
