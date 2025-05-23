# Calculate the values of a circle by knowing just one of the values.

pi = 3.1415926536

print("\nEnter 'q' at any time when you are finished.")

while True:
    print("\nGiven a circle with values for radius, diameter, and circumference.")

    radius = input("\nWhat is the radius? ")
    if radius == 'q':
        break

    diameter = input("What is the diameter? ")
    if diameter == 'q':
        break

    circumference = input("What is the circumference? ")
    if circumference == 'q':
        break
    
    if radius:
        radius = float(radius)
        diameter = float(2 * radius)
        circumference = float(diameter * pi)

        diameter = round(diameter, 2)
        radius = round(radius, 2)
        circumference = round(circumference, 2)

        print("---------------------------------------------------------------")
        print(f"\nGiven a circle with radius = {radius:,}")
        print(f"                  diameter = {diameter:,}")
        print(f"             circumference = {circumference:,}\n")
        print("---------------------------------------------------------------")
        continue

    if diameter:
        diameter = float(diameter)
        radius = float(diameter / 2)
        circumference = float(diameter * pi)

        diameter = round(diameter, 2)
        radius = round(radius, 2)
        circumference = round(circumference, 2)

        print("---------------------------------------------------------------")
        print(f"\nGiven a circle with diameter = {diameter:,}")
        print(f"                      radius = {radius:,}")
        print(f"               circumference = {circumference:,}\n")
        print("---------------------------------------------------------------")
        continue

    if circumference:
        circumference = float(circumference)
        radius = float((circumference / pi) / 2)
        diameter = float(circumference / pi)

        diameter = round(diameter, 2)
        radius = round(radius, 2)
        circumference = round(circumference, 2)

        print("---------------------------------------------------------------")
        print(f"\nGiven a circle with circumference = {circumference:,}")
        print(f"                           radius = {radius:,}")
        print(f"                         diameter = {diameter:,}\n")
        print("---------------------------------------------------------------")
        continue
