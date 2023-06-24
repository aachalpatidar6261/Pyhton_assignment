# concatenate two dictionary

d1 = {1 : 100, 2:20.02}
d2= {3 : "red", 4 :"black"}
d1.update(d2)
print("concatenate two dictionary : ",d1)

# concatenate three dictionary
d3 = {"z":"john" , "y" : "cherry"}

d6 ={**d3, **d2, **d1}
print("concatenate three dictionary : ",d6)

d7 = d1 | d2 | d3
print("concatenate three dictionary : ",d7)