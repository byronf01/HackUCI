class Comment(object):
    def __init__(self, text):
        self.text = text
        self.likes = 0

    def changeLikes(self, liked: bool):
        if liked:
            self.likes += 1
        else:
            self.likes -= 1

    def returnComment(self):
        return self.text
