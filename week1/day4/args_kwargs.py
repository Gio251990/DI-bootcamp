# *ARGS and **KWRANGS (just arguments, key word agrument)

friends = ["Ross", "Rachel", "Monica", "Joey", "Chandler", "Phoebe"]

def how_you_doing(*args):
    if args:
        for name in args:
            print(f"{name}, how you doing?")

(how_you_doing("Ross", "Rachel", "Monica", "Joey", "Chandler", "Phoebe"))


def user_info(**kwargs):
    print(kwargs)
    for value in kwargs.value():
        print(value)

user_info(name = "Ross", last_name = "Geller", age = 35, has_children = True, cheat_Rachel = True)