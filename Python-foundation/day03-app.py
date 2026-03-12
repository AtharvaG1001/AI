loss = 0.02
accuraccy = 0.95
learning_rate = 0.01

if loss > 0.5 :
    print("loss is high - keep training")
elif loss > 0.2:
    print("moderate loss - keep monitoring")
else:    
    print("low loss - model is converging")

if accuraccy >= 0.9:
        print("accuraccy is good ")
elif accuraccy >= 0.7:
        print("accuraccy is acceptable")
else:
         print("accuraccy-poor investigate model")

if loss < 0.3 and accuraccy > 0.9:
                print("model is ready to deploy")
else:
                print("model is not ready to deploy - keep training")
