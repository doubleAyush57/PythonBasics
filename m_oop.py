class Dog():
    # constructor
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "BARK BARK")


aayush = Dog("aayush")
aayush.speak()
