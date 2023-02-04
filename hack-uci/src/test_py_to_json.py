import os
import json
import sys
from classes.post import Post


if __name__ == "__main__":
    sys.path.insert(0, '/classes/post.py')
    newPost = Post("Went to ShareteaUCI today! ")

    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'sample.json'), "w") as outfile:
        json.dump(newPost.__dict__, outfile)
