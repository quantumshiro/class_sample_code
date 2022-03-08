class Greeting:
    def __init__(self, name):
        self.ownanme = name

    def english(self):
        print("Hello, " + self.ownanme)
    
    def espanol(self):
        print("Hola, " + self.ownanme)
    
    def japanese(self):
        print("Konnichiwa, " + self.ownanme)

def main():
    name = input("What is your name? ")
    greeting = Greeting(name)
    greeting.english()
    greeting.espanol()
    greeting.japanese()


if __name__ == "__main__":
    main()