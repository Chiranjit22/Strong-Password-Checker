def is_strong(password):
    msg = "Password must contain at least one "

    is_lower = any(c.islower() for c in password)
    is_upper = any(c.isupper() for c in password)
    is_digit = any(c.isdigit() for c in password)
    special_ch = set("#@$%&*+=?<>")
    is_special = any(c in special_ch for c in password)

    if is_lower:
        if is_upper:
            if is_digit:
                if is_special:
                    return True,"Your password is strong !!"
                else:
                    return False,msg+"special characters (#@$%&*+=?<>)"
            else:
                if is_special:
                    return False,msg+"digits"
                else:
                    return False,msg+"digits and special characters (#@$%&*+=?<>)"
        else:
            if is_digit:
                if is_special:
                    return False,msg+"uppercase"
                else:
                    return False,msg+"uppercase and special characters (#@$%&*+=?<>)"
            else:
                if is_special:
                    return False,msg+"uppercase and digit"
                else:
                    return False,msg+"uppercase , digit and special characters (#@$%&*+=?<>)"
    else:
        if is_upper:
            if is_digit:
                if is_special:
                    return False,msg+"lowercase"
                else:
                    return False,msg+"lowercase and special characters (#@$%&*+=?<>)"
            else:
                if is_special:
                    return False,msg+"lowercase and digit"
                else:
                    return False,msg+"lowercase, digit and special characters (#@$%&*+=?<>)"
        else:
            if is_digit:
                if is_special:
                    return False,msg+"lowercase and uppercase"
                else:
                    return False,msg+"lowercase, uppercase and special characters (#@$%&*+=?<>)"
            else:
                if is_special:
                    return False,msg+"lowercase, uppercase and digit"
                else:
                    return False,msg+"lowercase, uppercase, digit and special characters (#@$%&*+=?<>)"
                

#    if not is_lower:
#        return False,msg+"lowercase"
#    elif not is_upper:
#        return False,msg+"uppercase"
#    elif not is_digit:
#        return False,msg+"digits"
#    elif not is_special:
#        return False,msg+"special characters (#@$%&*+=?<>)"
#    else:
#        return True,"Your password is strong !!"

def call_checker():
    pwd = input("Re-enter your password: ")
    result = is_strong(pwd)
    print()
    print(result[1])
    if not result[0]:
        call_checker()

pwd = input("Enter your password:")
result = is_strong(pwd)
print()
print(result[1])
if not result[0]:
    call_checker()