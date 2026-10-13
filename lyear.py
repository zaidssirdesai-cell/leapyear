import sys

def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    year=int(sys.argv[1])
    print(sys.argv[0])