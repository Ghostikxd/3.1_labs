height = float(input("Рост: "))
weight = float(input("Вес: "))
steps = float(input("Количество шагов: "))
activity_time = float(input("Время активности: "))
steplength = round(height/4 + 0.37,2)
distance = round(steplength*steps/100,2)
speed = distance/activity_time
calories = round(0.035 * weight + (speed*speed / height) * 0.029 * weight,2)
distance_km=round(distance/1000,2)
print("Расстояние в м" , distance)
print("Кол-во сожженных калорий", calories)
print("Дистанция в км" , distance_km)
if distance_km<2:
    print("Малая подвижность")
elif distance_km<4:
    print("Средняя подвижность")
else:
    print("Высокая подвижность")