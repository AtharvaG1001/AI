weight = 1
learning_rate = 0.1
gradient = 0.5

for i in range(10):
 weight =(weight - learning_rate * gradient)
 print("updated_weight:",weight)
 if weight < 0.5:
    print("warning")
 else:
    print("weight normal")



