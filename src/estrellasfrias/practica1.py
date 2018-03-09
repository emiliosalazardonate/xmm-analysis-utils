'''
Created on Mar 25, 2017

@author: esalazar
'''
from math import sqrt
def calculaMedia(velocidades, errores, orden):
        sumaPesos= 0
        sumaPonderada =0
        pesos = []
        for i in range (0, len(errores)):
            pesos.append(1./errores[i])
            sumaPesos = sumaPesos +1./errores[i]
        for i in range (0, len(velocidades)):
            sumaPonderada = sumaPonderada + velocidades[i]*pesos[i]
            
        for i in range (0, len(velocidades)):
            print "%s;%s;%s"%(orden[i],velocidades[i], errores[i])
        print ("Suma Ponderada Total: %s ")%(sumaPonderada/sumaPesos)
        print ("Error Total: %s ")%(1/sumaPesos)
        print ("----------------------")
if __name__ == '__main__':
    velocidades = [-11.6219, -11.0007 ,-11.7928 ,-12.5733 ,-12.2021,-12.4052,-12.8817,-12.0329,-11.0209,-12.0822]
    errores = [2.049  ,1.479  , 2.242  , 1.518  ,1.249  ,1.243  ,0.812  ,1.405  ,1.273, 0.862 ]
    orden = [21
,24
,33
,34
,36
,37
,40
,42
,43
,50]

    calculaMedia(velocidades, errores, orden)

    velocidades2 = [135.1047, 132.9363, 136.2209, 137.5989, 131.6694, 134.0183, 133.8846]
    errores2 = [4.398, 3.366, 4.130, 4.077, 3.738, 4.071,4.441]
    orden2 = [21
,24
,33
,34
,36
,37,40]
    calculaMedia(velocidades2, errores2,orden2)

    velocidades3 = [-29.1064,-21.9651,-32.7708,-34.8582 ,-30.1752,-30.2976,-25.8679]
    errores3 = [4.859, 5.700,4.935,6.368,7.169, 4.591,4.862]
    calculaMedia(velocidades3, errores3,orden2)
    

#     desviacionSuma = 0
#     for i in range (0, len(velocidades)):
#         desviacionSuma = desviacionSuma + (((-12.0448720306 - velocidades[i])*pesos[i])**2)
#     print(desviacionSuma)
#     desviacionSuma = desviacionSuma/10
#     desviacionSuma = sqrt(desviacionSuma) 
#     print(desviacionSuma)
    
    