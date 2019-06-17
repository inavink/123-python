# Program to remove item from the list
countryName = ["India","USA","England","Nepal","Bhutan","Pakistan"]
print("Here is the list of countryName\n")
for cont in countryName:
    print(cont)
print("\nNow, I am going to remove Pakistan from countryList")
countryName.remove("Pakistan")
print("Updated list of countryName:\n")
for cont1 in countryName:
    print(cont1)
