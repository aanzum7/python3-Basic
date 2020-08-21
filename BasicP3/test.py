inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for i in inventory:
    str1 = []
    str1 = i.split(", ")
    print("The store has {} {}, each for {} USD.".format(str1[1],str1[0],str1[2]))