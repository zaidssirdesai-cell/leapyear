import sys

def leapyear(year):
    if (year % 400) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

if __name__ == "__main__":
    y = 2016
    print(sys.argv[1])
    print(sys.argv[0])