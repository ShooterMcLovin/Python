import sys


def main():
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        raise AssertionError("the arguments are bad")
    try:
        N = int(sys.argv[2])
        S = str(sys.argv[1])
        returnList = [wrd for wrd in S.split() if (lambda x: len(x) > N)(wrd)]
        print(returnList)

    except ValueError:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    main()
