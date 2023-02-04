import json
import random

facts_data = []
facts_list = [
    {"car_f": "Tesla was originally named after Nikola Tesla, the inventor of alternating current.", "industry_f": "Nearly half the EVs in the world are in China."},
    {"car_f": "Tesla built its Gigafactory 3 in China to produce the Tesla Model 3 and Tesla Model Y for the Chinese market.", "industry_f": "Roughly 96 percent of EV owners would buy or lease another one"},
    {"car_f": "Nio has innovative battery swap solutions for charging your EV.", "industry_f": "EVs are more efficient. Up to 80 percent of the battery energy powers the vehicle, compared to 14% to 26 percent of the energy from a gasoline-powered car."},
    {"car_f": "Nio is a loss-making business currently ", "industry_f": "About 57 percent  of consumers avoid EVs because they worry about running out of charge but only 5 percent of owners have run out."},
    {"car_f": "Company name Rivian is inspired from CEO RJ Scaringe's time growing up in Florida", "industry_f": "Hybrid-Electric Vehicles (HEVs): HEVs combine a gas-powered engine with one (or more) electric motors. An HEV does not plug in; it collects energy through regenerative braking"},
    {"car_f": "Lucid air manufacturer Lucid motors was previously called Atieva", "industry_f": "Plug-In Hybrid-Electric Vehicles (PHEVs): Similar to an HEV, the main difference is that a PHEV is able to plug in to charge. The Prius also comes as a plug-in version."},
    {"car_f": "Rivian is designing vehicles tough enough to go off-road.", "industry_f": "Battery Electric Vehicles (BEVs): Also known as an all-electric car, it needs to be plugged in to recharge"},
    {"car_f": "A Tesla Roadster is faster than most sports cars, with an acceleration speed of 0 to 60 in 1.9 seconds. To compare, a Ferrari or Lamborghini accelerates from 0 to 62 in 2.8 to 2.9 seconds.", "industry_f": "he first electric vehicle was created in 1832."},
]

def initfact():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in facts_list:
        facts_data.append({"id": item_id, "results": item})
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