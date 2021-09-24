# There is a party at SoftUni. Many guests are invited, and there are two types of them:
# Regular and VIP. When a guest comes, check if they exist in any of the two reservation lists.
# On the first line, you will receive the number of guests – N. On the following N lines,
# you will be receiving their reservation codes. All reservation codes are 8 characters long,
# and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END" command.
# In the end, print the number of the guests who did not come to the party and their reservation numbers.
# The VIP guests must be first. Both the VIP and the Regular guests must be sorted in ascending order.

# INPUT:
# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END

# OUTPUT:
# 2
# 7IK9Yo0h
# tSzE5t0p


# INPUT:
# 6
# m8rfQBvl
# fc1oZCE0
# UgffRkOn
# 7ugX7bm0
# 9CQBGUeJ
# 2FQZT3uC
# 2FQZT3uC
# 9CQBGUeJ
# fc1oZCE0
# END

# OUTPUT:
# 3
# 7ugX7bm0
# UgffRkOn
# m8rfQBvl

def is_vip(guest: str):
    if guest[0].isdigit():
        return True
    return False


number_of_guests = int(input())

guest_all = set()
guests_who_came = set()
for _ in range(number_of_guests):
    guest = input()
    guest_all.add(guest)

while True:
    guest = input()
    if guest == "END":
        break
    else:
        guests_who_came.add(guest)

set_with_guests_who_do_not_came = guest_all - guests_who_came
print(len(set_with_guests_who_do_not_came))

vip_guests = sorted([x for x in set_with_guests_who_do_not_came if is_vip(x)])
regular_guests = sorted([x for x in set_with_guests_who_do_not_came if not is_vip(x)])

for vip_guest in vip_guests:
    print(vip_guest)
for regular_guest in regular_guests:
    print(regular_guest)
