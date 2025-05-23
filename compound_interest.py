# DATE: 5-6-2025
# Compound Interest

while True:
    principal = input("\nP = ")

    if principal == 'q':
        print('\n')
        break
    
    p = float(principal)
    rate = float(input("r = "))
    r = rate/100
    n = float(input("n = "))
    t = float(input("t = "))

    a = p*((1+(r/n))**(n*t))
    a = round(a, 2)

    print(f"Future value = ${a:,}")
    # print(f"Monthly payment: ${round(a/(t*12), 2)}")

