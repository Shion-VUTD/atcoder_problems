n = int(input())
s = set([])

for i in range(n):
    command, string = input().split()
    if command == 'find':
        if string in s:
            print('yes')
        else:
            print('no')
    if command == 'insert':
        s.add(string)

    
