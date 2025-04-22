from art import logo
print(logo)
print("Welcome to the Blind Auction Game!")


def find_max_bidder(bidder_dict):
    # ==========================================================================================
    max_bid = max(bidder_dict.values())
    for bidder_name, bidder_amount in bidding_info.items():
        if bidder_amount == max_bid:
            print(f"The winner is {bidder_name}, with a bid of ${bidder_amount:,}.")
    # ==========================================================================================
    # max_bid = 0
    # winner = ""
    # for person, amount in bidder_dict.items():
    #     if amount > max_bid:
    #         max_bid = amount
    #         winner = person
    # print(f"The winner is {winner}, with a bid of ${max_bid:,}.")
    # ==========================================================================================


bidding_info = {}
proceed = True
while proceed:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidding_info[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    while others != 'yes' and others != 'no':
        print("Invalid input.")
        others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if others == 'yes':
        print("\n" * 100)
    elif others == 'no':
        proceed = False
        find_max_bidder(bidding_info)
for key, val in bidding_info.items():
    print(f"{key}: ${val:,}")
