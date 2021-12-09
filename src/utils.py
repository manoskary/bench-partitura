import time

def helper_func(func1, func2, file, reps):
    list1 = list()
    list2 = list()
    for i in range(reps):
        start = time.time()
        func1(file)
        end = time.time()
        list1.append(end - start)

        start = time.time()
        func2(file)
        end = time.time()
        list2.append(end - start)

    avtime1 = sum(list1) / len(list1)
    avtime2 = sum(list2) / len(list2)
    return avtime1, avtime2