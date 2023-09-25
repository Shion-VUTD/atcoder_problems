from collections import OrderedDict

s_1 = input()
s_2 = input()

dict_1 = OrderedDict(0)
for c in s_1:
  dict_1[c] += 1
for c in s_2:
  dict_2[c] += 1
  
print(dict_1, dict_2)
  