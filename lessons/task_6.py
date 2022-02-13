
while True:
    start = float(input("Number of kilometers: "))
    finish = float(input("Finish: "))
    day = 1
    if start <= 0 or finish < 0:
        print("результат должен быть больше 0")
    else:
        while start < finish:
            start += start * 0.1
            day += 1

        print(f"спортсен добьется результата за {day}")

    print(f"Результат будет достигнут за {day}")