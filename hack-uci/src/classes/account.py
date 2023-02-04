from random import randint

class Account(object):
    def __init__(self, username: str, password: str, pfp: str, bio: str, followers: int, posts=[]):
        self.id = randint(1000000,9999999)
        self.username = username
        self.password = password
        self.pfp = pfp
        self.bio = bio
        self.followers = 0
        self.posts = posts
    
    def login(self, username, password) -> bool:
        if username == self.username and password == self.password:
            return True 
        return False

    def changeUsername(self, new):
        self.username = new

    def changePassword(self, new):
        self.password = new

    def changePFP(self, new):
        self.pfp = new

    def changeBio(self, new):
        self.bio = new

    def changeFollowers(self, follow: bool):
        if follow: self.followers += 1
        else: self.followers -= 1

    def editPosts(self, id: int):
        if id in self.posts:
            self.posts.remove(id)
        else:
            self.posts.append(id)
            