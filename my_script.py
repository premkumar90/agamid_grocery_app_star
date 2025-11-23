# list_a = [1,"apple",3.5]
# list_b = ["banana","tomato"]
# list_a.insert(1,"banana")
# print(list_a)
# my_tuple = (10,20,"orange")
# my_grand_tuple = my_tuple + (30,40)
# print(my_grand_tuple)

movies = ["Inception", "Interstellar","The Prestige", "Dunkirk","The Dark Knight"]
movies.append("Memento")
print(movies)
movies.remove("Dunkirk")
print(movies)

numbers = [2,3,5,7,11,13]
print(numbers[4:])
colors = ["red","blue","green"]
colors.insert(1,"yellow")
print(colors)
colors.append("purple")
print(colors)

dimensions = (3,5,7)
print(dimensions[1])
fruits = ("apple","banana")
vegetables = ("carrot","lettuce")
groceries = fruits + vegetables 
print(groceries)
