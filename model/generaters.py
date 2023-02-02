import json
import random

facts_data = []
facts_list = [
    {"car_f": "something", "industry_f": "something"}
    ]

def initfact():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in facts_data:
        facts_list.append({"id": item_id, "results": item})
        item_id += 1

def getfact():
    return (facts_data)

def getfact_c():
    return (facts_data[id])

def getrandom():
    return (random.choice(facts_data))

def printfact(car_f):
    print(car_f['id'], car_f['question'], "\n")


def countfacts():
    return len(facts_data)


if __name__ == "__main__": 
    initfact()  # initialize jokes

    # Random joke
    print("Random fact")
    printfact(getrandom())
    
    # Count of Jokes
    print("Jokes Count: " + str(countfacts()))