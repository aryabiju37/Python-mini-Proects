class User:
    active_users = 0
    @classmethod
    def active_user(cls):
        return f"There are {cls.active_users} active users presently."

    @classmethod
    def from_string(cls,data_str):
        fname,lname,age = data_str.split(",")
        return cls(fname,lname,int(age))
   
   
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def initials(self):
        return f"{self.fname[0]}.{self.lname[0]}"

    def likes(self,thing):
        return f"{self.fname} likes {thing}"

    def is_senior(self):
        if self.age > 65:
            return "Senior"
        return "Not Senior"
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.fname}"

    def logout(self):
        User.active_users -= 1
        print(f"{self.fname} has left the chat")

    def __repr__(self):
        return f"{self.fname} {self.lname} is {self.age}"

class Moderator(User):
    total_mods=0
    def __init__(self,first,last,age,community):
        super().__init__(first,last,age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_activemods(cls):
        return f"There are currently {cls.total_mods} moderators"

    def remove_post(self):
        return f"{self.full_name()} removed a post from {self.community} community"

jasmine = Moderator("Jasmine","O'Connor",61,"Piano")
tom = User.from_string("tom,sprinkler,45")
tom = User.from_string("tom,sprinkler,45")
tom = User.from_string("tom,sprinkler,45")
jasmine = Moderator("Jasmine","O'Connor",61,"Piano")
print(User.active_user())
print(Moderator.display_activemods())



# print(jasmine.full_name())
# print(jasmine.community)
# print(tom)
# print(f"{tom.full_name()} is a {tom.is_senior()}")
# print(User.active_user())
# user1 = User("Sherlock","Holmes",30)
# user2 = User("Irene","Adler",26)
# user3=User("Mycroft","Holmes",67)
# print(User.active_user())
# print(user2.logout())
# print(User.active_user())
# print(user3.is_snior())
# print(user3.birthday())
# print(user3.age)

#****************************************************************#
# print(user2.full_name())
# print(user1.initials())
# print(user1.likes("Ice Cream"))
# print(f"{user1.fname}  {user1.lname} is {user1.age}")
# print("{fname} {lname} is {age} years old ".format(fname=user2.fname,lname=user2.lname,age=user2.age))