
def NULL_not_found(object: any) -> int:

    if object.__class__ == float: 
        print(f"Garlic: {object} {object.__class__}")

    elif object.__class__ == int:
        print(f"Zero: {object} {object.__class__}")

    elif object.__class__ == bool:
        print(f"Fake: {object} {object.__class__}")

    elif object.__class__ is str and object == '':
        print(f"Empty: {object} {object.__class__}")

    elif object.__class__ is None:
        print(f"Nothing: {object} {object.__class__}")
        
    else:
        print(f"Type not found")
        return 1
    return 0
