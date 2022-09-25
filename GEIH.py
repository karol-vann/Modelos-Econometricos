import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import linear_model

data= "C://Users//ACER//OneDrive//Documentos//university//Sexto Semestre//Semillero//Área - Características generales (Personas).xlsx"
data1=  "C://Users//ACER//OneDrive//Documentos//university//Sexto Semestre//Semillero//Área - Ocupados.xlsx"
cgenerales= pd.read_excel(data)
ocupados= pd.read_excel(data1)
#merge
dataB= cgenerales.merge(ocupados,how ="left",on=["DIRECTORIO","ORDEN"])
print(dataB)
dataB.info()
dataB=dataB[["DIRECTORIO","ORDEN","P6030S3","P6500","P6020","ESC","P6040"]]
print(dataB)

def age(x):
    return 2022-x
    #APLICAR FUNCION A DATAFRAME
dataB["P6030S3"]=dataB["P6030S3"].apply(age)
dataB["P6020"]=dataB["P6020"].replace([2.0],0)
dataB["exper"] = (dataB["P6030S3"]**2)
print(dataB)
#dropna
muestra_nan= dataB.dropna()
print(dataB)

#test hallar coef
y_test= muestra_nan["P6500"]
x_test= muestra_nan[["P6030S3","P6020","ESC","P6040","exper"]]

#train entrenar las variables
y_train= muestra_nan["P6500"]
x_train= muestra_nan[["P6030S3","P6020","ESC","P6040","exper"]]

#Regresion
reg=linear_model.LinearRegression()

#ajustar el modelo
reg.fit(x_train,y_train)
reg.predict(x_test)
print('b1 = ' + str(reg.coef_) + ', b0 = ' + str(reg.intercept_)+'Precisión = '+str(reg.score))
