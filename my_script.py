# list_a = [1,"apple",3.5]
# list_b = ["banana","tomato"]
# list_a.insert(1,"banana")
# print(list_a)
# my_tuple = (10,20,"orange")
# my_grand_tuple = my_tuple + (30,40)
# print(my_grand_tuple)

# movies = ["Inception", "Interstellar","The Prestige", "Dunkirk","The Dark Knight"]
# movies.append("Memento")
# print(movies)
# movies.remove("Dunkirk")
# print(movies)

# numbers = [2,3,5,7,11,13]
# print(numbers[4:])
# colors = ["red","blue","green"]
# colors.insert(1,"yellow")
# print(colors)
# colors.append("purple")
# print(colors)

# dimensions = (3,5,7)
# print(dimensions[1])
# fruits = ("apple","banana")
# vegetables = ("carrot","lettuce")
# groceries = fruits + vegetables 
# print(groceries)

apples_tuple = ("apples",0.50,5)
banana_tuple = ("banana",0.80,6)
kiwi_tuple = ("kiwi",0.70,7)
grocery_list = []
grocery_list.append(apples_tuple)
print(grocery_list)
grocery_list.append(banana_tuple)
grocery_list.append(kiwi_tuple)
print(grocery_list)

print(f"Total cost of {apples_tuple[0]} : ${round(apples_tuple[1]*apples_tuple[2],3)}")
print(f"Total cost of {banana_tuple[0]} : ${round(banana_tuple[1]*banana_tuple[2],3)}")
print(f"Total cost of {kiwi_tuple[0]} : ${round(kiwi_tuple[1]*kiwi_tuple[2],3)}")

apple_dict = {"name":"apple","price":0.50,"quantity":5}
banana_dict = {"name":"banana","price":0.80,"quantity":6}
kiwi_dict = {"name":"kiwi","price":0.70,"quantity":7}
apple_dict["total_cost"] = round(apple_dict["price"]*apple_dict["quantity"],3)
banana_dict["total_cost"] = round(banana_dict["price"]*banana_dict["quantity"],3)
kiwi_dict["total_cost"] = round(kiwi_dict["price"]*kiwi_dict["quantity"],3)

print(f"Total cost of {apple_dict['name']}s : ${apple_dict['total_cost']}")
print(f"Total cost of {banana_dict['name']}s : ${banana_dict['total_cost']}")
print(f"Total cost of {kiwi_dict['name']}s : ${kiwi_dict['total_cost']}")

num_list = [16,47,1,3,5,9,15,2]
print(num_list[1:])
print(num_list[:3])
print(num_list[-3])
num_list.sort(reverse=True)
print(num_list)
print(len(num_list))

dairy_products = {"milk","butter","cream","yogurt","cheese"}
desserts = {"jello","chocolate","candy","cookies","muffins"}
dairy_products.add("ice_cream")
desserts.add("ice_cream")
print(dairy_products)
print(desserts)
dairy_products.discard("butter")
desserts.discard("jello")
print(dairy_products)
print(desserts)
inter_set = dairy_products.intersection(desserts)
print(inter_set)
# apple_dict.append("total_cost":)
# price_list = []
# price_list.append(apple_dict["price"])
# price_list.append(banana_dict["price"])
# price_list.append(kiwi_dict["price"])
# quantity_list = []
# quantity_list.append(apple_dict["quantity"])
# quantity_list.append(banana_dict["quantity"])
# quantity_list.append(kiwi_dict["quantity"])



#round(<The float you want to round off>,<number of decimal places>)

