### API - GUI Quizz APP ###

### Type Hints and arrows ###

""" (variable name : type to be expected) """
""" -> bool This refers to the expected data type output of a function """


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
