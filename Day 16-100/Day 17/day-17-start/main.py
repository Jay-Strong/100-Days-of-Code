class User:
    def __init__(self, user_id: str, username: str) -> None:
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user: object) -> None:
        user.followers += 1
        self.following += 1


user1 = User(user_id="001", username="Jay")
user2 = User(user_id="002", username="Jack")

user1.follow(user=user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
# py main.py