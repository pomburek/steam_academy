import datetime

class Blat:
    kolor = "biały"

    def __init__(self, kolor):
        self.kolor = kolor

    def pomaluj(self, kolor):
        self.kolor = kolor

    def __str__(self):
        return "Biurko w kolorze " + self.kolor

class Biurko:
    blat = None
