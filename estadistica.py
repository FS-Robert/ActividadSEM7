import statistics

# Ejemplo de uso del módulo statistics

datos = [20, 40, 60, 80, 100]

media = statistics.mean(datos)
print("La media es:", media)

mediana = statistics.median(datos)
print("La mediana es:", mediana)

desviacion = statistics.stdev(datos)
print("La desviación estándar es:", desviacion)
