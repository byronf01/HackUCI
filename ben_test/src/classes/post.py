import sys
sys.path.insert(0, '.')

from datetime import datetime
from src.classes.comment import Comment
from PIL import Image

class Post():

    ID = 0

    def __init__(self, date: str, image: str, description: str, tags: list[str], likes=0, comments=[]):
        Post.ID += 1
        self.id = Post.ID
        if date == None:
            self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            self.date = date
        self.image = image  # image as url
        self.description = description
        self.tags = tags
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

if __name__ == "__main__":
    print("bruh")