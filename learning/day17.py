class User:
    def __init__(self, user_id,username): #initialization
        #print("it runs each time when a new obj is created")
        self.id = user_id #attributes
        self.username = username
        self.follower = 0
        self.following = 0
    def follow(self,user): #methods
        user.follower +=1
        self.following +=1
        
user_1 = User("777","Mahi")
'''user_1.id ="777" 
user_1.username ="Mahi"
print(user_1.username)'''

user_2 = User("111","Gupta")
'''user_2.id="111"
user_2.username="Gupta"
print(user_2.id)'''

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
