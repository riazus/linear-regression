import re

def get_thetas():
    lines = []
    try:
        with open("thetas.txt") as file:
            for line in file:
                lines.append(line)
    except:
        return

    if len(lines) != 2:
        print("thetas.txt has an error")
        print("Thetas in file are wrong ! Program is using 0 instead")
        return

    try:
        thetaZero = float(re.search(r'(?<=:)(.*?)(?=\n)', lines[0]).group(1))
        thetaOne = float(re.search(r'(?<=:)(.*?)(?=\n)', lines[1]).group(1))
    except:
        print("Thetas in file are wrong ! Program is using 0 instead")
        return

    return (thetaZero, thetaOne)


def main():
    try:
        mileage = int(input("Enter the mileage: "))
    except:
        print("The mileage is not a number !")
        exit()
    if mileage < 0:
        print("The mileage cannot be negative !")
        exit()
    thetaZero, thetaOne = get_thetas()
    estimatePrice = thetaZero + thetaOne * mileage
    print("The estimation is :", estimatePrice)

if __name__ == "__main__":
    main()