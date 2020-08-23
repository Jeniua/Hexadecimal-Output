def hex_output():
    decnum = 0
    hexnum = input("Enter a hex number to convert: ")

    for power, digit in enumerate(reversed(hexnum)):
        print(power,digit,'digit')
        decnum += int(digit) * (16 ** power)
        print(decnum)
    print(decnum)
hex_output()
