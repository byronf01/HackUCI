from datetime import datetime
from classes.comment import Comment


class Post():

    def __init__(self, description):
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.description = description
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
