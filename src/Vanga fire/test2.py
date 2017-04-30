from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import model_from_json

# Загружаем данные об архитектуре сети
import numpy

json_file = open("model1.json", "r")
loaded_model_json = json_file.read()
json_file.close()
# Создаем модель
loaded_model = model_from_json(loaded_model_json)
# Загружаем сохраненные веса в модель
loaded_model.load_weights("model1.h5")
print("Загрузка сети завершена")

loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


data = numpy.loadtxt("t.csv", delimiter=",")
predict = loaded_model.predict(data)
#
#
print(predict)