first = int(input("Enter the first number: "))
last = int(input("Enter the last number: "))
while first < last:
    first += 1
    output = "0" + str(first)
    print(output)
    file = open("Numbers.txt", "a")
    file.write(output + "\n")
    file.close()
