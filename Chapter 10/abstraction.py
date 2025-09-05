class Car:
    def __init__(self):
        self.acc=False
        self.brek=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("Car Started")


c1=Car()
c1.start()

    