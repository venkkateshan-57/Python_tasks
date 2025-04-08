mark={'John':98,'Jack':89,'Rose':90,'Jim':85,'Alan':95}
name=input("Enter the Name: " ).capitalize()
if name in mark:
    print(f"{name}'s mark is ", mark[name])
else:
    print(f"The entered name {name} is not found\nPlease enter a valid name")