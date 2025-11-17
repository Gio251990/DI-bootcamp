from Exercise import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True
    

    def play(self, *args):
        names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(names)} all play together")

    def do_a_trick(self):
        import random
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

dog1 = PetDog("Rex", 5, 20)
dog2 = PetDog("Max", 2, 8)
dog3 = PetDog("Jack", 9, 26)

dog1.train()
dog2.train()
dog3.train()

dog1.play(dog2, dog3)

dog1.do_a_trick()
dog2.do_a_trick()
dog3.do_a_trick()