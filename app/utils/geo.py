import math

'''
расчет дистанции между двумя координатами в ховерсайн
'''
def haversine(lat1, lon1, lat2, lon2):
    # Радиус Земли в километрах (можно изменить на 3956 для миль)
    R = 6371.0
    
    # Переводим градусы в радианы
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    # Применяем формулу Хаверсина
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Итоговое расстояние в километрах
    distance = R * c
    return distance
