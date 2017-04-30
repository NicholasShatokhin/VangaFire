import matplotlib.pyplot as plt
import pandas
from pandas.tools.plotting import scatter_matrix

url = "f.csv"
names = ['X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area']
data = pandas.read_csv(url, names=names)
data.hist()
plt.show()