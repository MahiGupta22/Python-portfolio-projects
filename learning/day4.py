#heads and tails
import random
random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails==0:
    print("heads")
else:
    print("tails")

#who pays the bill
friends=["Alice","Bob","Charlie","David","Emanuel"]
print(random.choice(friends))
