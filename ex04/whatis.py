import sys

def main():
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided" if len(sys.argv) > 2 else "argument is missing")

    else:
        try:
            num = int(sys.argv[1])
            if num % 2 == 0:
                print(f"I'm Even.")
            else:
                print("I'm Odd.")
    
        except ValueError:
            raise AssertionError("argument is not an integer")

if __name__ == "__main__":
    main()