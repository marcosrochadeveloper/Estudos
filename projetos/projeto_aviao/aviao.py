#velocidade_media 850km/h

# 1km = 4.235294117647059 segundos

tempo1km = 4.235294117647059

def flight_plan(combustivel, pontos, end):
    num_stops = 0
    stops = []
    total_time = 0
    total_fuel = combustivel
    total_cost = 0
    total_km = 0

    while total_km < end:
        for num, ponto in enumerate(pontos):
            if len(pontos) > num:
                litros_necessarios = int((pontos[num][1] + pontos[num+1][1])*2)
            else:
                litros_necessarios = int(pontos[num][1]*2)
            combustivel = 200
            if litros_necessarios > 200:
                # AQUI VAI DEFINIR SE VAI PRECISAR PARAR
                distancia = ponto[1]
                while distancia >= 0:
                    combustivel -= 2
                    distancia -= 1
                    total_time += tempo1km
                    total_km += 1
                total_time += 15*60
                num_stops += 1
                stops.append(ponto[0])
                total_fuel += 200 - combustivel
                total_cost += (200 - combustivel)*6


    resultado = [
        ("num_stops", num_stops),
        ("stops", stops),
        ("total_time", total_time),
        ("total_fuel", total_fuel),
        ("total_cost", total_cost)
    ]
    for i in resultado:
        print(i)

fuel = 200

refuel_points = [
    ("WP1", 80, 15),
    ("WP2", 60, 15),
    ("WP3", 50, 15),
    ("WP4", 70, 15)
]

end_distance = int(input("Qual a distância do ponto inicial?"))


flight_plan(fuel, refuel_points, end_distance)


# - Seu tanque tem capacidade de 200 litros.

# Exemplo de output esperado:
# {
#     "num_stops": 2,
#     "stops": ["WP1", "WP3"],
#     "total_time": 320,
#     "total_fuel": 450,
#     "total_cost": 2700
# }
