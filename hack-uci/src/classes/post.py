import sys
sys.path.insert(0, '.')
import os 
from datetime import datetime
from src.classes.comment import Comment
from PIL import Image
from pathlib import Path

class Post():

    def __init__(self, date: str, image: str, description: str, tags: list[str], authorID: int, likes=0, comments=[]):
        # updates and checks current ID 
        newFile = os.path.join(
        os.path.dirname(__file__), "..", "classes", "currentid.py"
        )
        new_path = Path(newFile)
        
        ID = int(open(new_path, 'r').read())
        if ID == None:
            raise ValueError("No ID currently in currentid.py")
        self.id = ID
        ID += 1
        with open(new_path, 'w') as f:
            f.write(str(ID))


        if date == None:
            self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            self.date = date

        
        self.image = image  # image as url
        self.description = description
        self.tags = tags
        self.authorID = authorID
        if likes: self.likes = likes
        else: self.likes = 0
        if comments: self.comments = comments
        else: self.comments = []

    def __str__(self):
        return str([self.date, self.description, self.likes, self.comments])

    def changeLikes(self, liked=True):
        if liked:
            self.likes += 1
        else:
            self.likes -= 1

    def addComment(self, comment: Comment):
        self.comments.append(comment)

    def returnPostTime(self) -> str:
        return self.date

    def returnLikes(self) -> int:
        return self.likes

    def returnComments(self):
        return self.comments
    
    def toString(self):
        s = ""
        s += f"Date: {self.returnPostTime()}\n"
        s += f"Image: {self.image}\n"
        s += f"Description: {self.description}\n"
        s += f"Tags: {self.tags}\n"
        s += f"AuthorID: {self.authorID}\n"
        s += f"Likes: {self.returnLikes()}\n"
        s += f"Comments: {self.returnComments()}\n"
        return s
