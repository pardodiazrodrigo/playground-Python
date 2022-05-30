# list = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti","pudding"]

food[0] = "sushi"

#food.append("ice cream")
#food.remove("hotdog")
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()

for x in food:
    print(x)


# 2D lists = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]

print(food[0][0])