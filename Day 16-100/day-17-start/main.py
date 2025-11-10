class User:


    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        user.following += 1




user_1 = User("001", "angela")
user_2 = User("002", "Bobi")


user_1.follow(user_2)


