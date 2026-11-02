import pytest
from pydantic import ValidationError
from app.utils.geo import haversine
from app.schemas.location import DistanceRequest

def test_zero_distance():
    """Тест 1: Нулевое расстояние (точка сама до себя)"""
    lat, lon = 55.7558, 37.6173
    distance = haversine(lat, lon, lat, lon)
    # Используем pytest.approx, чтобы избежать проблем с плавающей точкой
    assert distance == pytest.approx(0.0, abs=1e-5)

def test_latitude_degree_distance():
    """
    Тест 2: Приблизительно 111 км на 1 градус широты.
    Берем две точки на одном меридиане с разницей ровно в 1 градус по широте.
    """
    lat1, lon1 = 55.0, 37.0
    lat2, lon2 = 56.0, 37.0  # Разница ровно 1 градус по широте
    
    distance = haversine(lat1, lon1, lat2, lon2)
    
    # Окружность Земли примерно 40 000 км / 360 градусов ≈ 111.19 км
    assert 110.0 <= distance <= 112.5

def test_symmetry():
    """
    Тест 3: Симметрия.
    Расстояние из точки А в точку Б должно быть равно расстоянию из Б в А.
    """
    moscow = (55.7558, 37.6173)
    spb = (59.9343, 30.3351)
    
    dist_ab = haversine(moscow[0], moscow[1], spb[0], spb[1])
    dist_ba = haversine(spb[0], spb[1], moscow[0], moscow[1])
    
    assert dist_ab == pytest.approx(dist_ba, rel=1e-9)

def test_invalid_coordinates_validation():
    """
    Тест 4: Неверные координаты.
    Проверяем, что Pydantic-схема DistanceRequest выбрасывает ошибку,
    если передать широту больше 90 или долготу больше 180.
    """
    # Неправильная широта (95 градусов вместо максимума 90)
    with pytest.raises(ValidationError):
        DistanceRequest(lat1=95.0, lon1=37.0, lat2=55.0, lon2=37.0)
        
    # Неправильная долгота (-200 градусов вместо минимума -180)
    with pytest.raises(ValidationError):
        DistanceRequest(lat1=55.0, lon1=-200.0, lat2=55.0, lon2=37.0)