from collections import Counter

data1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300},{'item': 'item1', 'amount': 750}]

result = Counter()
for i in data1:
    result[i["item"]] += i["amount"]
print(result)