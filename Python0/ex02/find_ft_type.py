def all_thing_is_obj(object: any) -> int:
    if object.__class__ == list:
        print("List : <class 'list'>")
    elif object.__class__ == tuple:
        print("Tuple : <class 'tuple'>")
    elif object.__class__ == set:
        print("Set : <class 'set'>")
    elif object.__class__ == dict:
        print("Dict : <class 'dict'>")
    elif object.__class__ == str:
        print(object + " is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    
    return 42