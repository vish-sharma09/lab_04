class FlightTable:
    def __init__(self):
        self.data = {
            "AI161E90": {"From": "BLR", "To": "BOM", "Price": 5600},
            "BR161F91": {"From": "BOM", "To": "BBI", "Price": 6750},
            "AI161F99": {"From": "BBI", "To": "BLR", "Price": 8210},
            "VS171E20": {"From": "JLR", "To": "BBI", "Price": 5500},
            "AS171G30": {"From": "HYD", "To": "JLR", "Price": 4400},
            "AI131F49": {"From": "HYD", "To": "BOM", "Price": 3499},
        }
        self.city_mapping = {
            "BLR": "Bengaluru",
            "BOM": "Mumbai",
            "BBI": "Bhubaneswar",
            "HYD": "Hyderabad",
            "JLR": "Jabalpur",
        }

    def print_flight_info(self, flight_id):
        if flight_id in self.data:
            flight = self.data[flight_id]
            print("Flight ID:", flight_id)
            print("From:", self.city_mapping[flight["From"]])
            print("To:", self.city_mapping[flight["To"]])
            print("Price:", flight["Price"])
            print()
        else:
            print("Flight ID not found.\n")

    def search_by_city(self, city):
        print("Flights for", self.city_mapping[city] + ":")
        for flight_id, flight in self.data.items():
            if flight["From"] == city or flight["To"] == city:
                self.print_flight_info(flight_id)

    def search_by_from_city(self, from_city):
        print("Flights from", self.city_mapping[from_city] + ":")
        for flight_id, flight in self.data.items():
            if flight["From"] == from_city:
                self.print_flight_info(flight_id)

    def search_between_cities(self, from_city, to_city):
        print("Flights from", self.city_mapping[from_city], "to", self.city_mapping[to_city] + ":")
        for flight_id, flight in self.data.items():
            if flight["From"] == from_city and flight["To"] == to_city:
                self.print_flight_info(flight_id)


flight_table = FlightTable()

while True:
    print("Search options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        city = input("Enter city code (e.g., BLR, BOM, BBI, HYD, JLR): ")
        flight_table.search_by_city(city)
    elif choice == "2":
        from_city = input("Enter departure city code: ")
        flight_table.search_by_from_city(from_city)
    elif choice == "3":
        from_city = input("Enter departure city code: ")
        to_city = input("Enter arrival city code: ")
        flight_table.search_between_cities(from_city, to_city)
    elif choice == "4":
        print("THANK YOU FOR USING OUR SERVICES")
        break
    else:
        print("Invalid choice. Please select a valid option.\n")