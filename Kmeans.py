

#importamos la biblioteca pandas
import pandas as pd
#importamos la biblioteca sklearn
from sklearn.cluster import KMeans
#Importamos dataset
from sklearn import datasets
#import matplot
import matplotlib.pyplot as plt

data  = pd.read_csv('all_data_info.csv')

# Filtramos la información de nuestro CSV
dataComparable = data[['pixelsx','pixelsy']]

dataPaint = pd.DataFrame(dataComparable)

"""
plt.scatter(dataPaint['pixelsx'],dataPaint['pixelsy'], c = 'blue')
plt.xlabel('size pixel x',fontsize = 10)
plt.ylabel('size pixel y',fontsize = 10)
"""

model = KMeans(n_clusters= 3, max_iter = 1000)
model.fit(dataPaint)

#Creamos nuestros labels
y_labels = model.labels_

#modelo de nuestras predicciones
y_kmeans = model.predict(dataPaint)
#print('predicciones:{}'.format(y_kmeans))

plt.scatter(dataPaint['pixelsx'],dataPaint['pixelsy'], c =y_kmeans, s =30)
plt.xlabel('pixelsx',fontsize = 10)
plt.ylabel('pixelsy',fontsize = 10)
