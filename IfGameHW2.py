try:
    gross = float(input("Give me your salary: "))
    children = int(input("Tell me how many children: "))

    if gross < 1000:
        tax_rate = 0.10
    elif gross < 2000:
        tax_rate = 0.12
    elif gross < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    if gross < 2000:
        tax_rate -= 0.01 * children
    else:
        tax_rate -= 0.005 * children

    # Tax rate cannot be negative
    if tax_rate < 0:
        tax_rate = 0

    net = gross * (1 - tax_rate)
    print("Your net salary is:", net)

except:
    print("NO, please give me numbers only")
