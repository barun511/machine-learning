from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

def get_input():
    numbers = int(input())
    input_array = []
    
    output_array = []
    for i in range(numbers):
        inputi,outputi = map(int,input().split())
        input_array.append(inputi)
        output_array.append(outputi)
    return input_array,output_array

input_array,output_array = get_input()

model = Sequential()
model.add(Dense(units=30, activation='relu', input_shape=(1,)))
model.add(Dense(units=30, activation='relu'))
model.add(Dense(units=1))
model.compile(optimizer='rmsprop',loss='mean_squared_error')
model.fit(input_array, output_array, epochs=100,batch_size=2)
numpy_input_array = np.array([2,3,5,7,9,10,100,13,55])
print("predictions for 2,3,5,7,9,10,100,13,55")
print(model.predict(numpy_input_array))
