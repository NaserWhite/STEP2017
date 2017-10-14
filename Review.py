age = int(input("Enter your age => "))
                                       # 30 < 3 = False
if age < 3:
    print("Toddler")
                                       # 30 > 20 = True and 30 < 30 = False ----- True and False --- False
elif age > 20 and age < 30:
    print("You're in your 20's")                                    
                                       # 30 > 30 + True and 30 < 40 = True ----- True and True --- True
elif age > 30 and age < 40:
    print("You're i your 30's")