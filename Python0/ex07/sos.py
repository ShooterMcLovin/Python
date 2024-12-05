import sys


NESTED_MORSE = { 'A':'.-',
                'B':'-...',
                'C':'-.-.',
                'D':'-..',
                'E':'.',
                'F':'..-.',
                'G':'--.',
                'H':'....',
                'I':'..',
                'J':'.---',
                'K':'-.-',
                'L':'.-..',
                'M':'--',
                'N':'-.',
                'O':'---',
                'P':'.--.',
                'Q':'--.-',
                'R':'.-.',
                'S':'...',
                'T':'-',
                'U':'..-',
                'V':'...-',
                'W':'.--',
                'X':'-..-',
                'Y':'-.--',
                'Z':'--..',
                '1':'.----',
                '2':'..---',
                '3':'...--',
                '4':'....-',
                '5':'.....',
                '6':'-....',
                '7':'--...',
                '8':'---..',
                '9':'----.',
                '0':'-----',
                ', ':'--..--',
                '.':'.-.-.-',
                '?':'..--..',
                '/':'-..-.',
                '-':'-....-',
                '(':'-.--.',
                ')':'-.--.-',
                ' ':'/'}

def main():
    if len(sys.argv) != 2:
        raise AssertionError("the number of arguments is bad")
    try:
        phrase = sys.argv[1]
        converted = ('')
        for char in phrase:
            if not NESTED_MORSE[char.upper()]:
                raise AssertionError("the arguments are bad")
            else:
                converted += NESTED_MORSE[char.upper()]
                converted += " "
        print(converted)
    except:
        raise AssertionError("the arguments are bad")

if __name__ == "__main__":
    main()