product_price = int(input("enter product price"))
if product_price >1000:
    print ("The price of the product is{}".format(product_price*0.8))
else:
    print ("The price of the product is{}".format(product_price*0.7))



product_price = int(input("enter the price"))
if product_price >3000:
    if product_price == 4000:
        print("congratulation you get the goa trip")
    print(f"the price of the product is {product_price *0.8}")
elif product_price >=2000 and product_price <=3000:
    if product_price ==2999:
        print("Congratulations you get additional gift")
    print (f"The price of the product is {product_price*0.7}")
elif product_price>100 and product_price<2000:
    print(f"The price of the product is {product_price*0.6}")
else:
    print("lets drink tea")
    print("I will also be there")
