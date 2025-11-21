list = [{"a":1001, "b" : 1002},{"c":1002},{"v":1005},{"t":1001},{"y":1006}]
dic_unique=set(value for dic in list for value in dic.values())
print("unique value in dictionary : ",dic_unique)