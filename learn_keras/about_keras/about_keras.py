'''
demo of sequential in keras
'''

import tensorflow
from tensorflow.keras.models import Sequential
model = Sequential()

'''
demo of stacking layers as easy as .add()

here let me add some explaniations(maybe not absolutely correct):
we all know that what we need to do in deep learning algorithm 
is use a large moutitule dataset to clean the 'model'

All the steps of machine leanring includes steps:
step-1:
> training the model by given training datasets (if it is a supervised learning model, the training datasets should contains 
multi-demension features, and the expected lables)
> after we got the trained model (model = parameters + math-formular) the formular we elected by previous experience, and the 
  parameters are 'trained' from the training dataset 
  
step-2:
> ok suppose we already got the trained model we wash from the dataset, the next step is try to evaluate the accuracy of the model 
> often we use the cost function or actually the loss function the dataset here we often use the other part of the training dataset(we often divided the 
training dataset into two parts one is the training dataset that used to wash model and the remained dataset will be taken as the testing dataset)
> after optimize(slightly) the parameters that minimize the loss function value we got a optimized model 


step-3:
> after we 'washed' and optimized the model, next step is to used our trained model to predict value by providing the input data value.
'''
from tensorflow.keras.layers import Dense
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))


'''
Example-3:
'''
model.compile(loss='categorical_crossentropy',
    optimizer='sgd',
    metrics=['accuracy'])

'''
Example-4
'''
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True))

'''
Example-5
after setting 
1. deep learning matrix size, algorithm model, layer size 
2. loss function method 
3. optimizer function (steps and thresholds)

next step is letting the training dataset in to wash/train the model .
'''
# here the x_train is the input dataset
# y_train is the expected output result it is a supervised training method
# epoches means how many times of the total loop
# and the batch_size means inner each loop how many times train
mode.fit(x_train, y_train, epochs=5, batch_size=32)

'''
Example-6
in this step is use your test dataset to evaluate the 
distance between input data's output value and the predicted output value 
what this step calculate is try to minimize the loss function output value 
which means the distance between your test dataset's output value and your model's output value 
to attach more closer to the global minimum. 
'''

# and here the batch_size means how many times of the loops/the iteration
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)


'''
Example-7

this code example shows how we use our trained model to predict based on the given input data
the model will execute batch_size times iteration and then output the prediction value
'''
classes = model.predict(x_test, batch_size=128)


'''
Example-8
GradientTape: 

we 
'''
import tensorflow as tf

# here we prepare an optimizer -- the core idea of a model's optimizer is try to calculate the model's gradient
# and step by step slash down by the model's gradient
# and the slash degree of the gradient formular we often called as the 'learning-rage'
# the steps cannot be too large --> this will cause we miss the global best solution
# and the steps cannot too small --> it will increase the iteration(batch tims) of the calculation
# -- waste of time and computing(GPU/CPU) resources

# and we all  know that in the mathematics every time we calculate gradient one formular
# is try to decompose the formular into a more lower dimensional formular and step by step on the lower math formular
# the modification degress is very slight than directly step by step move on the original formular in this way it change the
# modle's parameter very small which is smaller than the training step that's why we call it s the optimizer instead of the training


# prepare an optimizer
optimizer = tf.keras.optimizer.Adam()

# prepare a loss function loss_fun = calculate_distance(predict_value, expected_value)
loss_func = tf.keras.losses.kl_divergence

# iterate over the batch of a dataset
for inputs, targets in dataset:
    # open a gradient tape
    with tf.GradientType() as tape:
        # forward pass.
        predictions = model(inputs)
        # compute the loss value for this batch
        loss_value = loss_func(targets, predictions)

    # get gradients of loss wrt the weights
    gradients = tape.gradient(loss_value, model.trainable_weights)

    # update the weights of the model(weights are also called the parameters of the trained model)
    optimizer.apply_gradients(zip(gradients, model.trainable_weights))



if __name__ == '__main__':
    print('PyCharm')
    print(model)