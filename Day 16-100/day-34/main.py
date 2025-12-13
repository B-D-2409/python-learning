
def police_check(age: int)-> bool: # You can use type to reduce  change from mistakes
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive


if police_check(19):
    print("You may pass.")

else:
    print("Pay a fine.")