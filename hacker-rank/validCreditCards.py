"""
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.

"""

times = int(input())

def is_valid(card):
    print("Valid") if len(card) >= 16 and (
                card[0] in ['4','5','6']) and (
                card.isnumeric()) else print("Invalid")

while times:
    times -= 1
    card = input()
    if "-" in card:
        card = card.split("-")
        if all([True if len(card[i]) == 4 else False for i in range(len(card))]):
            card = "".join(card)
            is_valid(card)
        else:
            print("Invalid")
    else:
        is_valid(card)
