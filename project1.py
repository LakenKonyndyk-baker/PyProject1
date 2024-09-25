while True:
    S = input("Enter String: ")
    print(f"Checking String: '\033[34m{S}\033[0m'")
    print("\n")
    if (len(S)<=50):
        if any(char.isalnum() for char in S): # print True if S has any alphanumeric characters. Otherwise, print False. 
            print("Does S contain any alphanumeric characters? \033[92mTrue\033[0m")
        else:
            print("Does S contain any alphanumeric characters? \033[91mFalse\033[0m")
        if any(char.isalpha() for char in S): # print True if S has any alphabetical characters. Otherwise, print False. 
            print("Does S contain any alphabetical characters? \033[92mTrue\033[0m")
        else:
            print("Does S contain any alphabetical characters? \033[91mFalse\033[0m")
        if any(char.isdigit() for char in S): # print True if S has any digits. Otherwise, print False. 
            print("Does S contain any digits? \033[92mTrue\033[0m")
        else:
            print("Does S contain any digits? \033[91mFalse\033[0m")
        if any(char.islower() for char in S): # print True if S has any lowercase characters. Otherwise, print False. 
            print("Does S contain any lowercase characters? \033[92mTrue\033[0m")
        else:
            print("Does S contain any lowercase characters? \033[91mFalse\033[0m")
        if any(char.isupper() for char in S): # In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 
            print("Does S contain any uppercase characters? \033[92mTrue\033[0m")
        else:
            print("Does S contain any uppercase characters? \033[91mFalse\033[0m")
        print("Tests concluded.\n")
    else:
        print("String has more than 50 characters.\n")