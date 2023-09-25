num_a = int(input())
a_list = list(map(int, input().split()))
num_b = int(input())
b_list = list(map(int, input().split()))
x = int(input())

ans_list = ['unknown'] * (x+1)
ans_list[0] = 'true'

for step in b_list:
  ans_list[step] = 'false'
  
for i in range(x+1):
  if ans_list[i] != 'unknown':
    continue

  is_true = False
  for proceed_step in a_list:
    if (i - proceed_step) >= 0 and ans_list[i - proceed_step] == 'true':
      is_true = True
      ans_list[i] = 'true'
      break
  if is_true == False:
    ans_list[i] = 'false'

#print(ans_list)

if ans_list[-1] == 'true':
    print('Yes')
else:
    print('No')
