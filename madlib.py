# Date: 5-23-25

adj = input("\nadjective: ")
adj2 = input("adjective: ")
adj3 = input("adjective: ")
adj4 = input("adjective: ")
noun = input("a liquid: ")
verb = input("verbing: ")
verb2 = input("verbed: ")
verb3 = input("verbing: ")
verb4 = input("verb: ")
adverb = input("adverb: ")
famous_person = input("a famous person: ").title().strip()
animal = input("ocean animal: ")

madlib = f"\n    We all got to go {verb} in the ocean last week. It's {adj} how {adj2} the water was. We {verb2} all \n\
day without ever getting out of the {noun}. There were fish {verb3} all around us. We saw a few {adj3} crabs as \n\
well. Many of the people on the beach commented about my swimming. Some said that I swim like {famous_person}. \n\
That's quite the {adj4} compliment, I would say. I feel like I swim {adverb} fast, but I know I could never {verb4} \n\
faster than a {animal}.\n"

print(madlib)