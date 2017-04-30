# Create your first MLP in Keras
import keras
from keras import optimizers
from partd import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Normalizer, StandardScaler
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization
import numpy

def get_y(dataSet):
    result = []
    for p in dataSet[:, 12]:
        if (p > 0):
            result.append(1)
        else:
            result.append(0)
    return result

def get_x(dataSet):
    return dataSet[:, 0:12]


# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
dataSetTrain = numpy.loadtxt("f2.csv", delimiter=",")

dataSetTest = numpy.loadtxt("t.csv", delimiter=",")

# split into input (X) and output (Y) variables

#
#
X_train = get_x(dataSetTrain)
Y_train = get_y(dataSetTrain)

X_test = get_x(dataSetTest)
Y_test = get_y(dataSetTest)

model = Sequential()
model.add(Dense(12, input_dim=12, activation='relu'))
model.add(BatchNormalization(axis=1))
model.add(Dense(36, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='mean_squared_logarithmic_error', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X_train, Y_train, epochs=50, batch_size=40)
# evaluate the model
scores = model.evaluate(X_train, Y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

# Оцениваем качество обучения модели на тестовых данных
scores = model.evaluate(X_test, Y_test, verbose=0)

print("Точность работы на тестовых данных: %.2f%%" % (scores[1] * 100))


# Сохраняем сеть для последующего использования
# Генерируем описание модели в формате json
model_json = model.to_json()
json_file = open("model1.json", "w")
# Записываем архитектуру сети в файл
json_file.write(model_json)
json_file.close()
# Записываем данные о весах в файл
model.save_weights("model1.h5")
print("Сохранение сети завершено")