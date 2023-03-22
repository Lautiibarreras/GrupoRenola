listaprecios = []
contador=0
suma=0

setups=[{"procesador": "i7 11700k", "ram":"fury 32GB","gpu":"RTX 3070 Ti","price":1699},
        {"procesador": "Ryzen 9 5900x","ram": "Fury 32GB","gpu": "Radeon Rx6500","price":1899},
        {"procesador": "Ryzen 7 5700G","ram":"hyperx 16GB","gpu": "Radeon Rx6500","price":1199},
        {"procesador":"i5 10400F","ram": "Hyperx 8GB", "gpu":"RTX 2060", "price": 1099}]

for i in range(len(setups)):
    precios = setups[i]['price']
    listaprecios.append(precios)

while contador<len(listaprecios):
    suma=suma+listaprecios[contador]
    contador=contador+1

print(suma)

