from keras.models import Sequential
from keras.layers import SimpleRNN, LSTM, Dense, RepeatVector
from keras.layers import TimeDistributed
from keras.models import load_model

import csv
import numpy as np
import matplotlib.pyplot as plt

#options
TRAINING_DATA_PATH = 'D:\\deeplearning\\Subway\\Subway_dataset\\TF_input\\'
TIME_STEP = 3
NUMBER_OF_STATIONS = 110
NUMBER_OF_HIDDEN_NODE = 550
NUMBER_OF_EPOCH = 100
BATCH_SIZE = 19

def load_data(data_file_name):
    try:
        csv_file = open(TRAINING_DATA_PATH + data_file_name)
        csv_reader = csv.reader(csv_file)
        data = [row for row in csv_reader]
        return data
    except:
        FileNotFoundError


def split_data(data, train_data_percent = 1.0):
    num_rows = len(data)
    train_feature, train_label = [], []
    validation_feature, validation_label = [], []
    for idx, row in enumerate(data):
        if idx < num_rows * train_data_percent:
            train_feature.append(row[0:110])
            train_label.append(row[110:220])
        else:
            validation_feature.append(row[0:330])
            validation_label.append(row[330:660])
    return train_feature, train_label, validation_feature, validation_label

data = load_data('t_t+1_singledata.csv')
X_train, Y_train, X_test, Y_test = split_data(data)
X_train = np.asarray(X_train).reshape(-1, NUMBER_OF_STATIONS).astype('float')
Y_train = np.asarray(Y_train).reshape(-1, NUMBER_OF_STATIONS).astype('float')

#Keras model
model = Sequential()
model.add(Dense(units=NUMBER_OF_HIDDEN_NODE, input_dim=NUMBER_OF_STATIONS, activation='relu'))
model.add(Dense(units=NUMBER_OF_HIDDEN_NODE, input_dim=NUMBER_OF_HIDDEN_NODE, activation='relu'))
model.add(Dense(units=NUMBER_OF_HIDDEN_NODE, input_dim=NUMBER_OF_HIDDEN_NODE, activation='relu'))
model.add(Dense(units=NUMBER_OF_STATIONS, input_dim=NUMBER_OF_HIDDEN_NODE, activation='relu'))
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
'''
plt.plot(Y_train.flatten(), 'ro-', label="target")
plt.plot(model.predict(X_train[,:,:]).flatten(), 'bs-', label="output")
plt.legend()
plt.title("Before training")
plt.show()
'''

history = model.fit(X_train, Y_train, nb_epoch=NUMBER_OF_EPOCH, batch_size=BATCH_SIZE)
plt.plot(history.history["loss"])
plt.title("Loss")
plt.show()

model.save('Subway_keras_model.h5')

