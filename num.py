number = 1234567
num = f'{number:,}'
if (num[-4:-3] == ','):
    num = f"{num[:-4]}_{num[-3:]}"

print(num)
