class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print("Flight origin:", self.origin)
        print("Flight destination:", self.destination)
        print("Flight duration:", self.duration)

    def delay(self, minutes):
        self.duration += minutes

def main():
    f1 = Flight(origin="Argentina", destination="Mexico", duration=450)
    f1.print_info()
    f1.delay(100)
    f1.print_info()

    #f2 = Flight(origin="Mexico", destination="Madrid", duration=1250)
    #f2.print_info()

if __name__=="__main__":
    main()
