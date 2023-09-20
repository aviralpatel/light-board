import numpy as np
import numpy.random
import math

testArr = numpy.random.randint(low=10, high=100, size=(7, 7))
print(testArr)
maxIndex = testArr.argmax()
print(maxIndex)
print(testArr.shape)
fullIndex = np.unravel_index(maxIndex, testArr.shape)
print(fullIndex)



def unravel(index, shape):
    index = index
    rows = shape[0]
    columns = shape[1]
    row = math.floor(index/columns)
    column = index%columns
    rLst = [row, column]
    return rLst

print(unravel(maxIndex, testArr.shape))