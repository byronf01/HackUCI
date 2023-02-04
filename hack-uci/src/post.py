from datetime import datetime
from comment import Comment

class Post():
    
    def __init__(self, description):
        self.date = datetime.now()
        self.description = description
        self.likes = 0
        self.comments = []

    def changeLikes(self, liked=True):
        if liked:
            self.likes += 1
        else:
            self.likes -= 1
    
    def addComment(self, comment: Comment):
        self.comments.append(comment)

    def returnPostTime(self) -> str:
        return self.date.strftime("%d/%m/%Y %H:%M:%S")
    
    def returnLikes(self) -> int:
        return self.likes

    def returnComments(self):
        return self.comments