number = int(input("enter number:"))
biggest_num = 0 # храним самое большое число
num = number #храним оставщуюся часть числа, в противном случае она перепишется в 0

while num > 0:
    digit = num % 10 # отделяем последнюю цифру
    if digit > biggest_num: #сравниваем с нашим максимумом
        biggest_num = digit
        if biggest_num == 9:
            break

    num = num // 10

print(f"Наибольшее число равно {biggest_num}")

# % - отделяем на последнюю цифру
# // - уменьшение на последнюю цифру