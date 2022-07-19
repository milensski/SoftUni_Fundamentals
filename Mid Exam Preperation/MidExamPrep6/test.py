loot = "Pistol Coins Wood Silver Bronze Medallion Cup Gold".split()

print(loot[-3::])

for each in loot[-3::]:
    loot.remove(each)

print(loot)