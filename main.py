from models.city import City

if __name__ == '__main__':
    city = City("Lube")
    print("Picking random people:")
    city.get_random_person()
