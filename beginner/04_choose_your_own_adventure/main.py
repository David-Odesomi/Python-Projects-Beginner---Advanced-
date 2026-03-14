# 04 Choose Your Own Adventure
import sys
import time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
slowprint("Welcome to choose your adventure.")
def name():
    user_name = input("what is your name? enter: ")
    if user_name in ["Mira", "Old Eli", "Raven"]:
        user_name = input("Names are taken! Pick another name: ")
    return user_name;
user_name = name()
slowprint(f"Meet the characters: \n{user_name.title()} -> you, \nMira -> Your brave friend, \n"
      f"Old Eli -> A mysterious groundskeeper, \nRaven -> A shady stranger. ")

def main_story():
    print("=" * 50)
    slowprint("        🏚️  THE ABANDONED MANOR")
    print("=" * 50)
    slowprint(f"\nMira: '{user_name}, I can't believe we're actually doing this. The manor has been empty for 30 years.'")
    slowprint(f"\n{user_name}: 'Relax. It's just an old house.'")
    slowprint("\nMira: 'Yeah… sure. Just an old house.'")
    input("\nPress Enter to continue...")


    slowprint("\n*You both push open the creaking front door. Inside, a lantern flickers.")
    slowprint("An old man sits in a rocking chair.*")

    slowprint("\nOld Eli: 'Didn't think anyone would come back here. Not after what happened.'")
    slowprint(f"\nMira: *whispering* '{user_name}… who is this guy?'")
    slowprint("\nOld Eli: 'Name's Eli. I've kept watch over this place for years. You shouldn't be here —")
    slowprint("but since you are, there's something you need to know. There's a locked room upstairs.")
    slowprint("I have the key… but so does someone else.'")
    input("\nPress Enter to continue...")

    slowprint("\n*A figure steps out from the shadows.*")

    slowprint("\nRaven: 'He means me. And unlike this old man, I'll actually show you what's inside.'")
    slowprint("\nOld Eli: 'Don't trust her. She's been trying to get into that room for years. Nothing good is behind that door.'")
    slowprint(f"\nRaven: 'He's lying. There's treasure in there — enough for all of us. Come with me, {user_name}.'")
    input("\nPress Enter to continue...")

    print("\n" + "-" * 50)
    slowprint("Who do you trust?")
    slowprint("  A) Trust Old Eli")
    slowprint("  B) Trust Raven")
    print("-" * 50)

    response_input = input("A or B?: ")
    if response_input == "A":
        side_story1()



main_story()

