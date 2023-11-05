# Define the Vehicle class to represent individual vehicles
class Vehicle:
    def __init__(self, make, model, color, year, mileage):
        # Initialize attributes with the values passed in
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    # Method to update vehicle attributes
    def update_attributes(self, make=None, model=None, color=None, year=None, mileage=None):
        # Update attributes if new values are provided
        if make:
            self.__make = make
        if model:
            self.__model = model
        if color:
            self.__color = color
        if year:
            self.__year = year
        if mileage:
            self.__mileage = mileage

    # String representation of the Vehicle object
    def __str__(self):
        return f"{self.__make}, {self.__model}, {self.__color}, {self.__year}, {self.__mileage}"


# Define the VehicleInventory class to manage a collection of vehicles
class VehicleInventory:
    def __init__(self):
        # Initialize an empty list to store vehicles
        self.__vehicles = []

    # Method to add a new vehicle to the inventory
    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    # Method to remove a vehicle from the inventory by its index
    def remove_vehicle(self, index):
        if 0 <= index < len(self.__vehicles):
            del self.__vehicles[index]

    # Method to update a vehicle's attributes by its index
    def update_vehicle(self, index, **kwargs):
        if 0 <= index < len(self.__vehicles):
            self.__vehicles[index].update_attributes(**kwargs)

    # Method to save the vehicle inventory to a text file
    def save_to_file(self):
        with open("vehicle_inventory.txt", "w") as f:
            for vehicle in self.__vehicles:
                f.write(str(vehicle) + '\n')

    # String representation of the VehicleInventory object
    def __str__(self):
        return "\n".join(str(vehicle) for vehicle in self.__vehicles)


# Main program
if __name__ == "__main__":
    # Create a new VehicleInventory object
    inventory = VehicleInventory()
    
    while True:
        # Display the menu to the user
        print("1: Add a new vehicle")
        print("2: Remove a vehicle")
        print("3: Update vehicle attributes")
        print("4: Display all vehicles")
        print("5: Save to file and exit")
        
        # Get the user's choice
        choice = input("Enter your choice: ")

        # Perform the appropriate action based on the user's choice
        if choice == '1':
            make = input("Enter make: ")
            model = input("Enter model: ")
            color = input("Enter color: ")
            year = int(input("Enter year: "))
            mileage = int(input("Enter mileage: "))
            vehicle = Vehicle(make, model, color, year, mileage)
            inventory.add_vehicle(vehicle)
        elif choice == '2':
            print(inventory)
            index = int(input("Enter index of vehicle to remove: "))
            inventory.remove_vehicle(index)
        elif choice == '3':
            print(inventory)
            index = int(input("Enter index of vehicle to update: "))
            make = input("Enter new make (leave empty to keep current): ")
            model = input("Enter new model (leave empty to keep current): ")
            color = input("Enter new color (leave empty to keep current): ")
            year = input("Enter new year (leave empty to keep current): ")
            mileage = input("Enter new mileage (leave empty to keep current): ")

            kwargs = {}
            if make:
                kwargs['make'] = make
            if model:
                kwargs['model'] = model
            if color:
                kwargs['color'] = color
            if year:
                kwargs['year'] = int(year)
            if mileage:
                kwargs['mileage'] = int(mileage)
                
            inventory.update_vehicle(index, **kwargs)
        elif choice == '4':
            print(inventory)
        elif choice == '5':
            # Save to file and exit
            inventory.save_to_file()
            break