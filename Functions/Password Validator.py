def is_pass_valid(some_password):
    if len(some_password) < 6 or len(some_password) < 10:
        print("Password must be between 6 and 10 characters")
        return False
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    digits_counter = 0
    for character in some_password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        return False
    return True


password = input()
pass_is_valid = is_pass_valid(password)
if pass_is_valid:
    print("Password is valid")
else:
    print(is_pass_valid(password))