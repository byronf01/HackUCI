from pathlib import Path
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.classes.account import Account

def getUsers():
    nf = os.path.join(
        os.path.dirname(__file__), "..", "..", "public", "new_user.json"
    )
    np = Path(nf)
    f = open(np)
    data = json.load(f)
    new_users = dict() # dict by ID 

    for u in data["users"]:
        new_user = Account(
            u["username"],
            u["password"],
            u["bio"],
            u["pfp"],
            u["followers"],
            u["posts"],
        )
        new_users[new_user.id] = new_user

    return new_users


if __name__ == "__main__":
    new_users = getUsers()