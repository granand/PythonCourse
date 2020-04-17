# Dictionaries are unordered mappings for storing objects
# Dictionaries use a key-value pairing
# Key-Value pair allows users to quickly grab objects without needing to know the index location
# Unordered and cannot be sorted

my_dict = {}

my_dict={"first_name":"Anand","last_name":"Rengas"}
print(my_dict["first_name"])

prices_lookup = {"Apple":2.99,"Oranges":3.50,"Milk":3.09}
print(prices_lookup["Milk"])

d = {"k1":123,"k2":[0,1,2],"k3":{"insideKey":100}}
# returns 123
print(d["k1"])

# returns 1
print(d["k2"][1])

# returns 100
print(d["k3"]["insideKey"])

d1 = {"k1":100,"k2":200}
# returns {'k1': 100, 'k2': 200}
print(d1)

## Adding new values to the dictionary
d1["k3"] = 300
# returns  {'k1': 100, 'k2': 200, 'k3': 300}
print(d1)

## Overriding the values
d1["k1"] = "New Value"
# returns  {'k1': 'New Value', 'k2': 200, 'k3': 300}
print(d1)

# returns dict_keys(['k1', 'k2', 'k3'])
print(d1.keys())

# returns dict_values(['New Value', 200, 300])
print(d1.values())

# returns dict_items([('k1', 'New Value'), ('k2', 200), ('k3', 300)])
print(d1.items())

test1={1:"ONE",2:"TWO"}
# returns ONE
print(test1[1])