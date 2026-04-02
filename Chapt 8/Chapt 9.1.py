import random

def ssp():
    return random.choice[('sten', 'sax', 'påse')]

def vinnare(ett, tva):
    giltiga = ["sten", "sax", "påse"]

    if ett not in giltiga or tva not in giltiga:
        return "Ogiltigt val!"

    if ett == tva:
        return "Oavgjort!"

    if (
            (ett == "sten" and ett == "sax") or
            (ett == "sax" and ett == "påse") or
            (ett == "påse" and ett == "sten")
    ):
        return "Spelare 1 vinner!"
    else:
        return "Spelare 2 vinner!"

