learning_rate = 0.01
epochs = 1000   
model_name = "model"
is_training = True

print("learning_rate =",learning_rate, " type:", type(learning_rate))
print("epochs =",epochs, "type:", type(epochs))
print("model_name = ",model_name, "type:", type(model_name))
print("is_training =",is_training, "type:", type(is_training))


new_lr = learning_rate * 2
print(new_lr, type(new_lr))

new_lr =int(learning_rate )
print(new_lr, type(new_lr))

epochs_as_float = float(epochs)
print(epochs_as_float, type(epochs_as_float))

new_model_name = "Atharva" + model_name
print(new_model_name, type(new_model_name))

is_done = not is_training
print(is_done, type(is_done))