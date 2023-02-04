from datetime import datetime
from classes.comment import Comment
from PIL import Image


class Post():

    ID = 0

    def __init__(self, image: str, description: str, tags: list[str]):
        ID += 1
        self.id = ID
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.image = image  # image as url
        self.description = description
        self.tags = tags
        self.likes = 0
        self.comments = []

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
