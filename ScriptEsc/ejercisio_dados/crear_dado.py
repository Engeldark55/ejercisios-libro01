from main_dados import Die
from plotly.graph_objects import Bar , Layout
from plotly import offline

#visualizar tiradas de dado
resultados = []
n_range: int = 10000
for n_tiradas in range(n_range):
    dado: object = Die()
    tiradas = dado.roll()
    resultados.append(tiradas)
    
print(f"tiradas de dado, {resultados}")

#analizar r
frequencias = []
for valor in range(1, dado.lados+1):
    frecuencia = resultados.count(valor)
    frequencias.append(frecuencia)

print(f"contar tiadas del 1 a 6 , los resultados son: {frequencias}")

# visualizar resultados
x_values = list(range(1, dado.lados+1))
data = [Bar(x = x_values, y = frequencias)]

x_axis_config = {'title':'Resultados'}
y_axis_config = {'title':'frecuencias del resultado'}

my_layout = Layout(title=f'Resultados de un dado de 6 caras, lanzamientos de {n_range} veses', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')
