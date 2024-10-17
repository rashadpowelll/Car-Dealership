class Car:
    def __init__(self,make,model,year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        return f"{self.year} {self.make} {self.model} {self.price}"


class Dealership:
    def __init__(self):
        self.inventory = []
    def add_car(self,car):
        self.inventory.append(car)
    
    def view_inventory(self):
        if len(self.inventory == 0):
            print("No cars in inventory")
        else:
            for i, car in enumerate(self.inventory,1):
                print(f"{i}. {car.display_info()}")

    def search_car(self, make=None, model=None, year=None):
        results =[]
        for car in self.inventory:
            if (make and car.make.lower() ==make.lower()) or \
                (model and car.model.lower() == model.lower())\
                (year and car.year == year):
                results.append(car)

        if results:
            for i, car in enumerate(results, 1):
                print(f"{i}. {car.display_info()}")
            else:
                print("No cars matched your search.")
            
    def sell_car(self,index):
        if 0 <= index <len(self.inventory):
            sold_car = self.inventory.pop(index)
            print(f"Sold {sold_car.display_info()}")
        else:
            print("Invalid car index.")

def dealership_menu():
    dealership = Dealership()

    while True:
        print("n--- Car Dealership Menu")
        print("1. Add a car to inventory")
        print("2. View Inventory")
        print("3. Search for car")
        print("4. Sell a car")
        print("5. Exit")

        choice = input("Choose an option between 1-5: ")

        if choice == "1":
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = input("Enter car year: ")
            price = input("Enter car price: ")
            car = Car(make, model, year, price)
            dealership.add_car(car)
            print(f"Added {car.display_info()} to the inventory.")

        elif choice == "2":
            dealership.view_inventory()

        elif choice == "3":
            make = input("Enter make to search (or leave blank): ")
            model = input("Enter model to search for (or leave blank)")
            year = input("Enter year to search for (or leave blank) ")
            year = int(year) if year else None 
            dealership.search_car(make, model, year)

        elif choice == "4":
            dealership.view_inventory()
            index = input(input("Enter the number of the car to sell: "))
            dealership.sell_car(index)

        elif choice == "5":
            print("Exiting the program")
            break

        else:
            print("Invalid choice, Please Try Again! ")


dealership_menu()