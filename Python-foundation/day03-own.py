weight = 1.0
learning_rate = 0.1 
gradient = 0.5

for i in range(20):
    weight = (weight -learning_rate * gradient)
    compute_loss  = (weight ** 2)
    print("epooch no:", i)
    print("updated weight:" , weight)
    print("loss:", compute_loss)
    if compute_loss < 0.1:
        print("loss is low - model is converging")
    else:
        print("loss is high - keep training")
        break