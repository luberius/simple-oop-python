from random import randrange
from .person import Person


class City:
    name = None
    people = list()

    def generate_people(self):
        names_file = open("data/names.txt", "r")
        for x in names_file:
            self.people.append(Person(x, randrange(1, 100)))

    def get_random_person(self):
        person = self.people[randrange(1, 100)]
        print("Name: %sAge: %d" % (person.name, person.age))
        return person

    def __init__(self, name):
        print("Welcome to %s city. This city has 100 populations" % name)
        self.name = name
        self.generate_people()
