trump = input().strip()
card1, card2 = input().split()

order = "6789TJQKA"

rank1, suit1 = card1[0], card1[1]
rank2, suit2 = card2[0], card2[1]

if suit1 == suit2:
    if order.index(rank1) > order.index(rank2):
        print("YES")
    else:
        print("NO")
elif suit1 == trump and suit2 != trump:
    print("YES")
else:
    print("NO")