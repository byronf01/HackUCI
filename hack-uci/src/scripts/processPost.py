from pathlib import Path
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.classes.post import Post

def read_post(): # returns dict of Posts
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

    return new_posts
    

def print_posts(posts: dict[Post]):
    for id, p in posts.items():
        print(str(id) + ": " + p.toString())

def write_posts(posts: dict[Post]):
    newFile = os.path.join(
        os.path.dirname(__file__), "..", "..", "public", "data.json"
    )
    new_path = Path(newFile)


    new_data = dict()
    for id, p in posts.items():
        new_data[id] = {"date": p.date, "image": p.image, "description": p.description, "tags": p.tags, "likes": p.likes, "comments": p.comments}

    
    all_posts = json.dumps(new_data, indent=4)
    with open(new_path, 'w') as storage:
        storage.write(all_posts)
    

if __name__ == "__main__":
    new_posts = read_post()
    # print_posts(new_posts)
    write_posts(new_posts)
    

    

    