from pathlib import Path
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.classes.post import Post


def read_new():  # returns dict of Posts and list of (authorID, postID)
    newFile = os.path.join(
        os.path.dirname(__file__), "..", "..", "public", "new_posts.json"
    )
    new_path = Path(newFile)

    f = open(new_path)
    data = json.load(f)
    new_posts = dict()
    post_id_to_acc_id = []

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
        post_id_to_acc_id.append((p["authorID"], new_post.id))

    return (new_posts, post_id_to_acc_id)


def get_old():  # returns dict of Posts
    newFile = os.path.join(os.path.dirname(__file__), "..", "..", "public", "data.py")
    new_path = Path(newFile)

    with open(new_path, "r") as f:
        adict = f.read()
    
    temp = eval(adict)

    old_data = dict()

    for id, p in temp["posts"].items():
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


def write_data(posts: dict[Post], new_pairs):
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
    
    # write final changes to data.json
    with open(new_path, "r") as f:
        data = json.load(f)
        data["posts"] = new_data
    # match post ids to accounts
    for authorID, postID in new_pairs:
        try:
            if postID in data["accounts"][str(authorID)]["posts"]: continue
            else: data["accounts"][str(authorID)]["posts"].append(postID)
        except:
            raise KeyError("No author exists for this post")
    
    os.remove(new_path)
    with open(new_path, "w") as f:
        json.dump(data, f, indent=4)

    secondFile = os.path.join(
        os.path.dirname(__file__), "..", "..", "public", "data.py"
    )
    np = Path(secondFile)
    # write final changes to data.py
    with open(np, "r") as f:
        adict = f.read()
        cur = eval(adict)
        cur["posts"] = new_data
    for authorID, postID in new_pairs:
        try:
            if postID in cur["accounts"][authorID]["posts"]: continue
            else: cur["accounts"][authorID]["posts"].append(postID)
        except:
            raise KeyError("No author exists for this post")
    os.remove(np)
    with open(np, 'w') as f:
        f.write(str(cur))


if __name__ == "__main__":
    new_changes, new_pairs = read_new()
    old = get_old()
    if old:
        old.update(new_changes)
    else:
        old = new_changes
    write_data(old, new_pairs)
