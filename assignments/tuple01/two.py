#Immutable

product = ("laptop",50000,"Black","Samsung","Electronics")
print("Products are :",product)
print("second element : ",product[1])
print("Last 2 elements ", product[3:5])
if "Electronics" in product:
    print("Electronics present")
else:
    print("not present")
price = (1000,1500,1200,1100, 900) 
print("Occurance of 1000",price.count(1000))
print("maxm " , max(price))
print("minm " , min(price))
for a in price:
    print(a)
p_list = list(product)
p_list[2] = 55000
p_tuple = tuple(p_list)
print("Updated tuple" , p_tuple)
added_tuple = ("In Stock",)
p_tuple = p_tuple + added_tuple
print("new updated tuple", p_tuple)
p_list = list(p_tuple)
p_list.remove("Electronics")
p_tuple = tuple(p_list)
print("new updated tuple is ", p_tuple)
lName,lPrice,*rest = p_tuple
print("laptop name",lName)
print("laptop price",lPrice)
print("laptop other specs",rest)
prod1 = ("prod1",20000,"yellow")
prod2 = ("prod2",30000,"green")
prod3 = ("prod3",40000,"cyan")
nested_tuple = (prod1,prod2,prod3)
print("nested tuple ",nested_tuple)
print("second prod name ",nested_tuple[1][0])

