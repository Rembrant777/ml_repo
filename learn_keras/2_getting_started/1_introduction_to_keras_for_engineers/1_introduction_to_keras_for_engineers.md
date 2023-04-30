# Introduction to Keras for Engineers 

## Setup

[Code-1](./1_introduction_to_keras_for_engineers.py)

## Introduction 
Are you a machine learning engineer looking to use Keras to ship deep-learning powered features in real products?
This guide will serve as your first introduction to core keras API concepts. 

In this guide, you will learn how to: 
* Prepare your data before training a model (by turning it into either NumPy arrays or tf.data.Dataset objects).
* Do data preprocessing, for instance feature normalization or vocabulary indexing.
* Build a model that turns your data into useful predictions, using the Keras Functional API.
* Train your model with the built-in Keras fit() method, while being mindful of checkpointing, metrics monitoring, and fault tolerance.
* Evaluate your model on a test data and how to use it for interference on new data. 
* Customize what fit() does, for instance to build a GAN.
* Speed up training by leveraging multiple GPUs. 
* Refine your model through hyperparameter tuning. 

At the end of this guide, you will get pointers to end-to-end examples to solidify these concepts: 

* Image classification 
* Text classification  
* Credit card fraud detection  

## Data loading & preprocessing 
Nerual networks don't process raw data, like text files, encoded JPEG image files, or CSV files. 
They process vectorized & standardized representations.

* Text files need to be read into string tensors, then split into words. Finally, the words need to be indexed & turned into integer tensors. 
* Images need to be read & decoded into integer tensors, then converted to floating point and normalized to small values(usually between 0 and 1).
* CSV data needs to be parsed, with numerical features converted to floating point tensors and categorical features indexed and converted to integer 
* tensors. Then each feature typically needs to be normalized to zero-mean and unit-variance. 
* Etc. 
Let's start with data loading.

## Data Loading 
Keras models accept three types of inputs:

* NumPy Arrays, just like Scikit-Learn and many other Python-based libraries. This is a good option if your data fits in memory.
* TensorFlow Dataset objects. Thsi is a high-performance options that is more suitable for datasets that do not fit in memory and that are streamed from disk or from a 
* distributed filesystem. 
* Python generators that yield batches of data (such as custom subclasses of the keras.utils.Sequence class).

Before you start training a model, you will need to make your data available as one of these formats. 
If you have a large dataset and your are training on GPU(s), consider using the Dataset objects, since they will 
take care of performance-critical details, such as: 
* Asynchronously preprocessing your data on CPU where your GPU is busy, and buffering it into a queue. 
* Prefecting data on GPU memory so it's immediately available when the GPU has finished processing the previous batch, so that you can reach full GPU utilization 

Keras features a range of utilities to help you turn raw data on disk into a Dataset: 
* tf.keras.utils.image_dataset_from_directory turns image files sorted into class-specific folders into a labeled dataset of image tensors. 
* tf.keras.utils.text_dataset_from_directory does the same for text files 


In addition, the TensorFlow tf.data includes other similar utilities, such as the tf.data.experimental.make_csv_dataset 
to load strucured data from CSV files. 

Example: obtaining a labeled dataset form image files on disk 
Suppose you have a image file sorted by class in different folders like this 


Then you can do this:[Code-2](./1_introduction_to_keras_for_engineers.py)

The label of a sample is the rank of its folder in alphanumeric order. Naturally, this can 
also be configured explicitly by passing, e.g. class_names=['class_a', 'class_b'],
in which case label 0 will be the class_a and 1 will be class_b.

Example: obtaining a labeled dataset from text files on disk
Likewise for text: if you have .txt documents sorted by class in different folders, you can do[Code-3](./1_introduction_to_keras_for_engineers.py)

## Data preprocessing with Keras 
Once your data is in the form of string/int/float NumpPy arrays, or a Dataset object(or Python generator) that 
yields batches of string/int/float tensors, it is time to preprocess the data. This can mean:
* Tokenization of string data, followed by token indexing.
* Feature normalization.
* Rescaling the data to small values(in general, input values to a neural network should be close to zero -- 
typically we expect either data with zero-mean and unit variance, or data in the [0, 1] range.)

### THe ideal machine learning model is end-to-end 
In general, you should seek to do data preprocessing as part of your model as much as possible, not via an external data 
preprocessing pipeline. THat's because external data preprocessing makes your models less portable 
when it's time to use them in production. Consider a model that preprocesses text: it uses a specific tokenization algorithm
and a specific vocabulary index. 
When you want to ship your model to model app or a java script app, you will need to recreate the exact same preprocessing setup in tht 
target language. This can get very tricky: any small discrepancy between the orignal pipeline and the one you recreate has the 
potential to completely invalidate you rodel, or at least severely degrade its performance. 

It would be much easier to be able to simply export an end-to-end model that already includes preprocessiong.
The ideal model should expect as input something as possible to raw data: 
an image model should expect RGB pixel values in the [0,255] range, and a text model should accept stirngs of utf-8 characters. 
That way, the consumer of the exported model doesn't have to know about the preprocessing pipeline.

### Using the Keras preprocessing layers 
In Keras, you do in model data preprocessing via preprocessing layers. This includes:
* Vectorizing raw strings of text via the TextVectorization layer 
* Feature normalization via the Normalization layer 
* Image rescaling, cropping, or image dat aargumentation 

The key advantage or using keras preprocessing layers is that they can be included directly into your model.
either during the training or after training, which makes your models portable. 

And some preprocesisng layers have a state: 
* TextVectorization holds an index mapping words or tokens to integer indicies 
* Normalization holds the mean and variance of your features. 

And the state of a preprocessing layer is obtained by calling the layer.adapt(data) on a sample of the training data(or all of it).

Here is the example: turning string into sequences of integer word indices 
[Code-4](./1_introduction_to_keras_for_engineers.py)


Here is the example: truing strings into sequences of one-hot encoded bigrams [Code-5](./1_introduction_to_keras_for_engineers.py)

### Building models with the Keras Functional API 
A layer is a simple input-output transformation(such as scaling & center-cropping transformations above).

For instance, here's a linear projection layer that maps its inputs to a 16-dimensional feature space:

```python 
dense = keras.layers.Dense(units=16)
```

A model is a directed acyclic graph of layers. You can think of a model as bigger layer that encompasses 
multiple subliyers and that can be trained via exposure to data.(just like the rdd in spark)

THe most common and most powerful way to build Keras models is the Functional API. TO build models with the Functional API, 
you start by specifying the shape(and optinally the dtype) of your inputs. 
If any dimension of your input can vary, you can specify it as None. For instance and input for 200 * 200 RGB image
would have shape(200, 200, 3), but an input for RGV image of any size would have shape(None, None,3).

```python 
# let's say we expect our inputs to be RGB images of arbitrary size 
inputs = keras.Input(shape=(None, None, 3))
```

After defining your inputs, you can chain layer transformations on top of your inputs, until your final output
```python 

from tensorflow.keras import layers 

# center-crop to 150*150
x = CenterCrop(height=150, width=150)(inputs)

# rescale images to [0,1]
x = Rescaling(scale=1.0 / 255)(x)

# apply some convolution and pooling layers 
x = layers.Conv2D(filters=32, kernel_size=(3,3), activation="relu")(x)
x = layers.MaxPooling2D(pool_size=(3,3))(x)
x = layers.Conv2D(filters=32, kernel_size=(3,3), activation="relu")(x)
x = layers.MaxPooling2D(pool_size=(3,3))(x)
x = layers.Conv2D(filters=32, kernel_size=(3,3), activation="relu")(x)

x = layers.GlobalAveragePooling2D(x)

num_classes = 10
output = layers.Dense(num_classes, activation="softmax")(x)
```

Once you have defined the directed acyclic graph of layers that turns your input(s) into your outputs, 
instantiate a Model object:
```python 
model = keras.Model(inputs=inputs, outputs=outputs)

# this model behaves basically like a bigger layer. you can call it on batches of data like this 
data = np.random.randint(0, 256, size=(64, 200, 200, 3)).astype("float32")
processed_data = model(data)
print(processed_data.shape)
```


