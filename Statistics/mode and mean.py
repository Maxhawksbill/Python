import statistics

def Enter_array(arr):
    lst = list(arr.split(' '))

    #for i in range(0, len(lst)):
     #   lst[i] = int(lst[i])
    lst = [int(lst[i]) for i in range(0, len(lst))]
    if statistics.mode(lst) != statistics.mean(lst):
        r = 0
    else:
        r = 1
    return f'Result: {r}'


print(Enter_array(input('Enter: ')))