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

def getOld():
    nf = os.path.join(os.path.dirname(__file__), "..", "..", "public", "data.py") 
    np = Path(nf)

    with open(np, "r") as f:
        adict = f.read()
    
    temp = eval(adict)

    old_data = dict()

    for id, a in temp["accounts"].items():
        acc = Account(
            a["username"],
            a["password"],
            a["bio"],
            a["pfp"],
            a["followers"],
            a["posts"],
            id
        )
        old_data[int(id)] = acc

    return old_data

def print_accs(acc: dict[Account]):
    for id, a in acc.items():
        print(str(id) + ": " + a.toString())

def writeData(accounts: dict[Account]):
    nf = os.path.join(os.path.dirname(__file__), "..", "..", "public", "data.json") # change later
    np = Path(nf)
    new_data = dict()

    for id, a in accounts.items():
        new_data[id] = {
            "username": a.username,
            "password": a.password,
            "bio": a.bio,
            "pfp": a.pfp,
            "followers": a.followers,
            "joinDate": a.joinDate,
            "posts": a.posts,
        }
    all_accounts = json.dumps(new_data, indent=4)
    # print(all_accounts)

    # write final changes to data.json
    with open(np, "r") as f:
        data = json.load(f)
        data["accounts"] = new_data

    # print(data)

    os.remove(np)
    with open(np, 'w') as f:
        json.dump(data, f, indent=4)
    

    sec = os.path.join(
        os.path.dirname(__file__), "..", "..", "public", "data.py"  # CHANGE THIS LATER
    )
    data = Path(sec)

    # write final changes to data.py
    with open(data, "r") as f:
        adict = f.read()
        cur = eval(adict)
        cur["accounts"] = new_data
    
    os.remove(data)
    with open(data, 'w') as f:
        f.write(str(cur))


if __name__ == "__main__":
    new_users = getUsers()
    old_users = getOld()
    if old_users:
        old_users.update(new_users)
    else:
        old_users = new_users
    # print_accs(old_users)
    writeData(old_users)