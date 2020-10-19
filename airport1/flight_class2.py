class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

    def print_info(self):
        print("Flight origin:", self.origin)
        print("Flight destination:", self.destination)
        print("Flight duration:", self.duration)
        print()
        print("Passengers:")
        for p in self.passengers:
            print(p.name, p.flight_id)

    def delay(self, minutes):
        self.duration += minutes

class Passenger:

    def __init__(self, name):
        self.name = name
        self.flight_id = 0

def main():
    f1 = Flight(origin="Argentina", destination="Mexico", duration=450)

    p1 = Passenger("Alejandro Moreno")
    p2 = Passenger("Liliana Suarez")

    f1.add_passenger(p1)
    f1.add_passenger(p2)

    f1.print_info()

if __name__=="__main__":
    main()
