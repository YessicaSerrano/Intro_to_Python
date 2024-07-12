class Carprocon:
    budget = 50000

    def __init__(self, budget=50000, make_model=None, price=None):
        self.budget = budget
        self.price = price
        self.model = make_model
        self.pros = []
        self.cons = []
        self.propoints = []
        self.conpoints = []

    def setcar(self, make_model, price):
        self.model = make_model
        self.price = price

    def setpro(self, pro, priority):
        self.pros.append(pro)
        self.propoints.append(priority)

    def setcon(self, con, priority):
        self.cons.append(con)
        self.conpoints.append(priority)

    def printit(self):
        print(f"Budget: ${self.budget}")
        print(f"Price: ${self.price}")
        print(f"Model: {self.model}")
        print("Pros:")
        for i in range(len(self.pros)):
            print(f"   {self.pros[i]} (Priority: {self.propoints[i]})")
        print("Cons:")
        for i in range(len(self.cons)):
            print(f"   {self.cons[i]} (Priority: {self.conpoints[i]})")

    def sum(self, points):
        return sum(points)

    def compare(self, c):
        ctotal = self.sum(c.propoints) - self.sum(c.conpoints)
        thistotal = self.sum(self.propoints) - self.sum(self.conpoints)

        print(f"Total pros for {c.model}: {self.sum(c.propoints)}")
        print(f"Total cons for {c.model}: {self.sum(c.conpoints)}")
        print(f"Total pros for {self.model}: {self.sum(self.propoints)}")
        print(f"Total cons for {self.model}: {self.sum(self.conpoints)}")

        print(f"\n{c.model} total score: {ctotal}")
        print(f"{self.model} total score: {thistotal}")

        if ctotal > thistotal:
            print(f"\nConclusion, you should buy {c.model}")
        elif thistotal > ctotal:
            print(f"\nConclusion, you should buy {self.model}")
        else:
            print("\nConclusion, either car is a good choice.")
def main():

    car1 = Carprocon()
    car1.setcar("Audi A4", 35000)
    car1.setpro("Advanced Technology", 9)
    car1.setpro("Sleek Design", 8)
    car1.setpro("Performance and Handling", 7)
    car1.setpro("Safety", 6)
    car1.setpro("Comfort", 5)
    car1.setcon("Fuel Consumption", 3)
    car1.setcon("Repair Cost", 4)
    car1.setcon("Trunk Space", 2)
    car1.setcon("Rear Seat Space", 1)
    car1.setcon("Warranty Limitations", 7)

    car2 = Carprocon()
    car2.setcar("Nissan Altima", 29000)
    car2.setpro("Fuel efficiency", 10)
    car2.setpro("Comfortable Ride", 9)
    car2.setpro("Advanced Safety Features", 8)
    car2.setpro("Modern Technology", 6)
    car2.setpro("Reliable Performance", 7)
    car2.setcon("Limited Engine Options", 1)
    car2.setcon("Interior Material Quality", 5)
    car2.setcon("Infotainment System", 4)
    car2.setcon("Road Noise", 2)
    car2.setcon("Resale Value", 3)


    print("Car 1:")
    car1.printit()

    print("\nCar 2:")
    car2.printit()

    print("\nComparison:")
    car2.compare(car1)

main()
