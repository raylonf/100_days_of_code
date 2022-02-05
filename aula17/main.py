class User:
    
    def __init__(self, user_id, username):        
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print('New user have been created!')
    
    def follow(self, user):
        user.followers += 1
        self.following += 1       
    

user_1 = User(user_id= '001', username="Angela")
user_2 = User('002', 'Joaquim')


print(user_1)
print(user_1.username)
print(user_1.followers)
user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
user_1.username = 'Raylon'
print(user_1.username)