print("What 2017 movie are you?")

Jumanji = 0  #Fantasy/Action 
WonderWoman = 0 #Fantasy/Science fiction
Johnwick2 = 0 #Crime film/Thriller

question1 = int(input("Which Characted did you relate to most? 1.Wonder Woman, 2.John Wick, 3.Spencer, 4.Bethany, 5.Fridge, 6.Martha, 7.Alex ======> "))
if question1 == 1:
    WonderWoman = WonderWoman + 1
if question1 == 2:
    Johnwick2 = Johnwick + 1
if question1 == 3 or question1 == 4 or question1 == 5 or question1 == 6 or question1 == 7:
    Jumanji = Jumanji + 1