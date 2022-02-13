time_in_sec = int(input("Enter your time in sec: "))
hour = time_in_sec // 3600
time = time_in_sec % 3600
minutes = time // 60
sec = time % 60

print(f'Time in sec {hour:02d}:{minutes:02d}:{sec:02d}')


# // - уменьшение на последнюю цифру
# % - отделяем на последнюю цифру
