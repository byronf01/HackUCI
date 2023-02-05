import os 
from pathlib import Path

class Comment(object):
    def __init__(self, text, postID, id=0, ):

        nf = os.path.join(
            os.path.dirname(__file__), "..", "classes", "currentpostid.py"
        )
        new_path = Path(nf)

        ID = int(open(new_path, "r").read())
        if ID == None:
            raise ValueError("No ID currently in currentid.py")
        self.id = ID
        ID += 1
        with open(new_path, "w") as f:
            f.write(str(ID))
        
        self.text = text
        self.postID = postID
        self.likes = 0

    def changeLikes(self, liked: bool):
        if liked:
            self.likes += 1
        else:
            self.likes -= 1

    def returnComment(self):
        return self.text

    def toString(self):
        s = ""
        s += f"ID: {self.id}\n"
        s += f"Text: {self.text}\n"
        s += f"Post ID: {self.postID}\n"
        s += f"Likes: {self.likes}\n"
        return s