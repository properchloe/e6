import csv

with open("data/coffees.csv", 'r') as coffees:
    done = False
    while not done:
        this_reader = csv.reader(coffees, delimiter="\t")
        try:
            thing = next(this_reader)
            print(thing)
        except StopIteration:
            done = True
