# 04 Choose Your Own Adventure
print("Welcome to choose your adventure.")
def name():
    user_name = input("what is your name? enter: ")
    if user_name in ["Mira", "Old Eli", "Raven"]:
        user_name = input("Names are taken! Pick another name: ")
    return user_name;
user_name = name()
print(f"Meet the characters: \n{user_name.title()} -> you, \nMira -> Your brave friend, \n"
      f"Old Eli -> A mysterious groundskeeper, \nRaven -> A shady stranger. ")

print("")