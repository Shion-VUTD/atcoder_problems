ha, wa = map(int, input().split())
a = []
for i in range(ha):
  a.append(input())

hb, wb = map(int, input().split())
b = []
for i in range(hb):
  b.append(input())

hx, wx = map(int, input().split())
x = []
for i in range(hx):
  x.append(input())

# 黒いところを切り出す

def crop_rec
inner_ha_start = 0
inner_ha_end = ha - 1
inner_wa_start = wa - 1 
inner_wa_end = 0

for i in range(ha):
  print(a[i])
  if a[i] != '.' * wa:
    break
  else:
    inner_ha_start = i + 1
for i in range(ha - 1, -1, -1):
  if a[i] != '.' * wa:
    break
  else:
    inner_ha_end = i - 1
      
for i in range(inner_ha_start, inner_ha_end + 1):
  inner_wa_start_tmp = 0
  inner_wa_end_tmp = wa

  for j in range(0, wa, 1):
    if a[i][j] == '#':
      break
    else:
      inner_wa_start_tmp = j + 1
  if inner_wa_start_tmp < inner_wa_start:
    inner_wa_start = inner_wa_start_tmp
      
  for j in range(wa-1, -1, -1):
    if a[i][j] == '#':
      break
    else:
      inner_wa_end_tmp = j - 1
    print(inner_wa_end_tmp)
  if inner_wa_end_tmp > inner_wa_end:
    inner_wa_end = inner_wa_end_tmp
  

print(inner_ha_start, inner_ha_end, inner_wa_start, inner_wa_end) 

  