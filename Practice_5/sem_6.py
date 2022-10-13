
from collections import Counter


a = [1,1,1,1,1,2,3,4,5,5,5,2,4,3,6,7,7,8]

dd = Counter(a)

new_list = list()
for i,d in dd.items():
    if d == 1:
        new_list.append(i)
        
print(new_list)
