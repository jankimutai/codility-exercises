from collections import Counter
def most_common(data):
    counter = Counter(data)
    return counter.most_common(1)[0][0]
list1 = [1,2,3,4,7,7,7,7,2,1,1,3,4.8]
result = most_common(list1)
print(result)