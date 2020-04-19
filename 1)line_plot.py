import pandas as pd
import matplotlib.pyplot as plt
#importing libraries

df =pd.read_csv("iris.csv")
#importing csv file

versicolor=df[df.Species=="Iris-versicolor"]
#versicolor species
virginica=df[df.Species=="Iris-virginica"]
#virginica species



plt.plot(versicolor.Id  ,versicolor.PetalLengthCm,  
         color="green",label="versicolor")
#x axis is Id  and y axis is PetalLengthCm of versicolor
plt.plot(virginica.Id,virginica.PetalLengthCm,
         color="blue",label="virginica")
#x axis is Id  and y axis is PetalLengthCm of virginica

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")  
plt.legend() #puts label into plot
plt.grid() 
plt.title('Line Plot')  #title of plot
plt.show()





#%%