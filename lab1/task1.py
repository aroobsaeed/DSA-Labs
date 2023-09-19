rivers = [{"name": "Nile", "length": 4157},
          {"name": "Yangtze", "length": 3434},
          {"name": "Murray-Darling", "length": 2310},
          {"name": "Volga", "length": 2290},
          {"name": "Mississippi", "length": 2540},
          {"name": "Amazon", "length": 3915}]

#Task 1
for name in rivers: print(name["name"])


total = 0
for length in rivers:
    total += length["length"]
print("total length :",total)


for name in rivers:
    if name["name"].startswith("M"):
        print(name)
for i in range(len(rivers)):
    print(rivers[i]["name"])
    print("Length in kilometers of", rivers[i]["name"], rivers[i]["length"]*1.6)
