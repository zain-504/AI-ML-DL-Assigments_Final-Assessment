mobiledict = {"Iphone":70000,"Camera": 12.5, "Mobile Size": 6.6}
print(mobiledict)
print(type(mobiledict))

for mo in mobiledict:
    print(mobiledict[mo])

print (mobiledict.keys())
print (mobiledict.values())
mobiledict["Mobile Size"] = 6.7
print(mobiledict)
mobiledict.update