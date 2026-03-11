weight = 1
learning_rate = 0.1
gradient = 0.5

weight =(weight - learning_rate * gradient)
if weight < 0:print("updated_weight:",weight)
else: print("no weight update")

weight = ( weight - learning_rate) 
print("updated_weight:",weight)

weight = (weight - learning_rate)
print("updated_weight:",weight)

weight = (weight - learning_rate)
print("updated_weight:",weight)



