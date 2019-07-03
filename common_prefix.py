n=int(input())
string=[input() for i in range(n)]
for i in range(len(min(string))):
  if string[0][i]==string[1][i]:
    print(string[0][i],end='')
  else:
    break
