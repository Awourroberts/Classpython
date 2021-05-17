class Dog:
    puppy="Ash"
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def barks(self):
        return f"Hello,{self.name}barks in low tone"

    def change_gender(self):
        return f"Hello, {self.name} was change to female {self.gender}"
