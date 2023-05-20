# -*- coding: utf-8 -*-
"""
Created on Fri May 19 11:02:57 2023

@author: Gabriel
"""

#criar listas e amarmazenar os dados das 4 zonas de sp
#adicionar os dados de potencia e tempo
#calcular a produçao de energia 
#usar i else para analisar se os valores estao abaixo do esperado
#usar while para parar qnd a energia estiver em niveis aceitos

#criar lista
for v in range(4):
    
 lista = []

#adicionar valores de potencia e tempo

potencia = float(input('digite aqui o valor da potencia: '))

tempo = float(input('digite aqui o valor do tempo: '))

#calcular produçao de energia

produçao = potencia * tempo

#valor minimo em cada zona 
minimo = 6.43

#condicional if else para analisar a quantidade de enegia

protocolo = 'abaixo do esperaado' if produçao < minimo else 'esta certo'

#usando while

while(produçao < minimo):
    produçao += produçao
    
    if produçao == minimo:
        break
    print('consumo esta nos valores desejaados')
        