import tensorflow
from tensorflow.keras.layers import TextVectorization
import numpy as np
def code_1():
    training_data = np.array([["This is the 1st sample. okokok ok"], ["And here's the 2nd sample."]])
    print(training_data)
    print(type(training_data))
    # create a TextVectorization layer instance. It can be configured to either
    # return integer token indices, or a dense token representation(e.g. multi-hot or TF-IDF).
    # The text standaridization and text splitting algorithms are fully configurable.
    vectorizer = TextVectorization(output_mode="int")

    # calling 'adapt' on an array or dataset makes the layer generate a vocabulary
    # index for the data, which can then be reused when seeing new data.
    vectorizer.adapt(training_data)
    integer_data = vectorizer(training_data)
    print(integer_data)
    print(type(integer_data))

def code_2():
    # here we create a 1 * 2 matrix
    training_data = np.array([["This is the 1st sample."], ["And here's the 2nd sample."]])

    # here we create a vectorization template with the output mode as binary(0,1) and values range from 0-1 --> 2
    vectorizer = TextVectorization(output_mode="binary", ngrams=2)

    # here we insert our training data to the vectorized template
    vectorizer.adapt(training_data)

    # here we call the vectorizer to directly converted it to vectorized matrix
    integer_data = vectorizer(training_data)
    # print integer_data content
    print(integer_data)

    # print integer_data type info
    print(type(integer_data))

def code_3():
    # here generate an matrix
    # there is a little different here to figure out what does those parameters do in the randint method
    # i change large int into tiny value

    # the randint method is used to generate a random vallue matrix and the value's range should be in [0, 256]
    # and it generates a huge matrix with row = 2 -- the first param in size=(...)
    # and the column = 8
    # what's important is the it is a huge matrix and it is composed by a series of tiny matrix in which the
    # row = 7 which is the 3rd params in the size=(...) and the column value of the tiny matrix is the 3 which is the last param in the matrix
    # the first pramter of the randint
    training_data = np.random.randint(0, 256, size=(2, 8, 7, 3)).astype("float32")
    '''
    print(len(training_data[0]))
    print(len(training_data[1]))
    print(training_data)
    print(type(training_data))
    '''
    from tensorflow.keras.layers import Normalization
    normalizer = Normalization(axis=-1)

    # let the trainging data's row/col set to the normailizer
    normalizer.adapt(training_data)
    # here we try to normalized the data in the matrix
    # noramlized means all the items in the matrix sumed should be 1
    normalized_data = normalizer(training_data)
    print("var: %.4f" % np.var(normalized_data))
    print("mean: %.4f" % np.mean(normalized_data))
    print("sum: %.4f" % np.sum(normalized_data))
    arr = normalized_data[0][0]
    print(len(arr))
    print(len(arr[1]))
    sum = 0.0
    for x in range(len(normalized_data)):
        print("x value", x)
        for y in range(len(normalized_data[0])):
            print("y value", y)
            arr = normalized_data[x][y]
            for i in range (len(arr)):
                print("i value = ", i)
                for j in range(len(arr[0])):
                    print("j value = ", j)
                    sum += arr[i][j]
    print("sum = {}", sum)


def code_4():
    from tensorflow.keras.layers import CenterCrop
    from tensorflow.keras.layers import Rescaling

    # example image data, with values in the [0, 255] range
    training_data = np.random.randint(0, 256, size=(64, 200, 200, 3)).astype("float32")
    cropper = CenterCrop(height=150, width=150)
    scaler = Rescaling(scale=1.0 / 255)

    output_data = scaler(cropper(training_data))
    print("shape:", output_data.shape)
    print("min:", np.min(output_data))
    print("max:", np.max(output_data))

if __name__ == '__main__':
    #code_1()
    #code_2()
    #code_3()
    code_4()



