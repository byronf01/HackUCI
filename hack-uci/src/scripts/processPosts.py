from pathlib import Path
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.classes.post import Post


def read_new():  # returns dict of Posts
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
            p["authorID"],
            p["likes"],
            p["comments"],
        )
        new_posts[new_post.id] = new_post

    return new_posts


def get_old():  # returns dict of Posts
    newFile = os.path.join(os.path.dirname(__file__), "..", "..", "public", "data.py")
    new_path = Path(newFile)

    with open(new_path, "r") as f:
        adict = f.read()
    if adict == "":
        return dict()
    adict = eval(adict)

    old_data = dict()

    for id, p in adict.items():
        post = Post(
            p["date"],
            p["image"],
            p["description"],
            p["tags"],
            p["authorID"],
            p["likes"],
            p["comments"],
        )
        old_data[int(id)] = post

    return old_data


def print_posts(posts: dict[Post]):
    for id, p in posts.items():
        print(str(id) + ": " + p.toString())


def write_data(posts: dict[Post]):
    newFile = os.path.join(os.path.dirname(__file__), "..", "..", "public", "data.json")
    new_path = Path(newFile)
    new_data = dict()

    for id, p in posts.items():
        new_data[id] = {
            "date": p.date,
            "image": p.image,
            "description": p.description,
            "tags": p.tags,
            "authorID": p.authorID,
            "likes": p.likes,
            "comments": p.comments,
        }
    all_posts = json.dumps(new_data, indent=4)
    # write final changes to data.json
    with open(new_path, "w") as storage:
        storage.write(all_posts)

    secondFile = os.path.join(
        os.path.dirname(__file__), "..", "..", "public", "data.py"
    )
    data = Path(secondFile)
    # write final changes to data.py
    with open(data, "w") as f:
        f.write(str(new_data))


if __name__ == "__main__":
    new_changes = read_new()
    # print_posts(new_changes)
    old = get_old()
    if old:
        old.update(new_changes)
    else:
        old = new_changes
    write_data(old)
