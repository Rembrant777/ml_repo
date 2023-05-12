# About Keras 
Keras is a deep learning API written in Python, running on top of the machine learning platform [TensorFlow](). 
It was developed with a focus on enabling fast experimentation. Being able to go from idea 
to result as fast as possible is key to doing good research. 

Keras is:
* Simple: -- but not simplistic. Keras reduces developer cognitive load to free you to focus on the parts of the problem that really matter. 
* Flexible -- Keras adopts the principle of progressive disclosure of complexity: simple workflows should be quick and easy, while arbitrarily advanced workflows should be possible via a clear path that builds upon what you've already learned. 
* Powerful -- Keras provides industry-strength performance and scalability: it is used by organizations and companies including NASA, YouTube, or Waymo. 


## Keras & TensorFlow2 
TensorFlow2 is an end-to-end, open-source machine learning platform. You can think of it as an infrastructure layer 
for differentiable programming. It combines four key ability: 

* Efficiently executing low-level tensor operations on CPU, GPU, or TPU.
* Computing the gradient of arbitrary differentiable expressions.
* Scaling computation to many devices, such as clusters of hundreds of GPUs.
* Exporting programs("graphs") to external runtimes such as servers, browsers, mobile and embedded devices. 

Keras is the high-level API of the TensorFlow platform: an approachable, high-productive interface for solving machine 
learning problems, with a focus on modern deep learning. It provides essential abstractions and building blocks for developing 
and shipping machine learning solutions with high iteration velocity.

Keras empowers engineers and researchers to take full advantages of the scalability and cross-platform capabilities of the TensorFlow platform:
you can run Keras on TPU or on large clusters of GPUs, and you can export your Keras models to run in the browser or on a mobile device. 

## First contact with Keras 
The core data structures of Keras are layers and models. The simplest type of model is the 
`Sequential model`,which is a linear stack of layers. For more complex architectures, you should 
use the Keras functional API, which allows to build arbitrary graphs of layers, or write models entirely from scratch via subclassesing. 
Here is the [Example](./about_keras.py) 

Stacking layers is as easy as `.add()`
[Example](./about_keras.py)

Once your model looks good, configure its learning process with '.compile()'
[CodeExample-3](./about_keras.py)


And if you need to, you can further configure your optimizer. The keras philosophy 
is to keep simple things simple, while allowing the user to be fully in control when they 
need to (the ultimate control being the easy extensibility of the source code via subclassing).

[CodeExample-4](./about_keras.py)


And you can now iterate on your training data in batches
[CodeExample-5](./about_keras.py)


Evaluate your test loss and metrics in one line: 
[CodeExample-6](./about_keras.py)


Or generate prediction on new data:
[CodeExample-7](./about_keras.py)



What you just saw is the most elementary way to use Keras. 

However, Keras is also a highly-flexible framework suitable to iterate on state-of 
the art research ideas. Keras follows the principle of progressive disclosure of complexity: 
it makes it easy to get started, yet it makes it possible to handle arbitrarily advanced use cases, 
only requiring incremental learning at each step.

In much the same wayy that you were able to train & evaluate a simple neural network above in a few lines,
and you can use Keras to quickly develop new training procedures or exotic model architecutres. 
Here's a low-level training loop example, combining Keras functionality with the TensorFlow. 

[CodeExample-8](./about_keras.py)
