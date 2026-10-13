import sys

def leapyear(year):
    if (year % 400 == 0):
        return "is a leap year"
    else:
        return "is not a leap year"

if __name__ == "__main__":
    y = 2016
    print(sys.argv[1])
    print(sys.argv[0])