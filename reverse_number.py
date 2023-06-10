
def convert(num):
    num_list = [int(i) for i in str(num)]
    return num_list[::-1]

print(convert(5867321))