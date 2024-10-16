codes = [
    7419,
    47086,
    1725,
    58050,
    42534,
    1725,
    38066,
    38066,
    7355,
    9314,
    45732,
    55187,
    47406,
    77399,
    56234,
    77306,
    77053,
    57166,
    1332,
    76024,
    49207,
    38066,
    3883,
    2534,
    2534,
    1725
]
items = [
    'Milk Light 3L',
    'Long Grain Rice 2kg',
    'Eco Friendly Bag',
    'GoldenVale Quick Oats 7',
    'Chk Drumsticks 2kg',
    'Eco Friendly Bag',
    'Tomatoes Diced 400g',
    'Tomatoes Diced 400g',
    'Bacon Middle 1kg',
    'Eggs Cage 700g',
    'Frz Mixed Vegatables 1',
    'Spaghetti 500g',
    'Apct/PearHlves Aus 825',
    'To Potatoes Brushed 3k',
    '2 Star Beef Mince 500g',
    'Onions Brown 1kg',
    'Broccoli per kg',
    'Marg Original Spread 5',
    'Dried Sultanas 1kg',
    'Royal Gala Apples per',
    'Popcorn Microwave',
    'Tomatoes Diced 400g',
    'Flour Plain 1kg',
    'White Slc 650g Brd',
    'White Slc 650g Brd',
    'Eco Friendly Bag'
]
prices = [
    2.99,
    2.79,
    0.15,
    1.08,
    5.99,
    0.15,
    0.60,
    0.60,
    7.69,
    2.79,
    1.59,
    0.65,
    2.49,
    3.49,
    3.39,
    1.99,
    4.49,
    1.79,
    3.99,
    1.99,
    0.89,
    0.60,
    0.75,
    0.99,
    0.99,
    0.15
]
weight = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0.580,
    0,
    0,
    0.855,
    0,
    0,
    0,
    0,
    0,
]

length = 0
for item in items:
    if len(item) > length:
        length = len(item)

#print(f"{'Item':{length}}{'Price':>5}")
print(f"{'$':>{6+length+4}}")
for i in range(len(items)):
    if items[i].find(" per") != -1:
        print(f"{codes[i]:<6}{items[i]:{length}}{prices[i]*weight[i]:5.2f}")
        print(f"{weight[i]} Net @ {prices[i]}/kg")
    else:
        print(f"{codes[i]:<6}{items[i]:{length}}{prices[i]:5.2f}")