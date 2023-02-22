import sys

input = sys.stdin.readline
n = int(input())
cnt_ls = []
for i in range(n):
  n1, n2 = map(int, input().split(' '))
  ls = []
  ls = list(map(int, input().split(' ')))
  ls_s = []
  ls_s = list(sorted(ls, reverse=True))
  result = [[0 for _ in range(2)] for _ in range(n1)]
  for i in range(n1):
    result[i][0] = i
    result[i][1] = ls[i]
  i = 0
  while i < n1:
    if ls_s[i] != result[i][1]:
      num = result.pop(i)
      result.append(num)
    else:
      i += 1

  for i in range(len(result)):
    if n2 == result[i][0]:
      cnt_ls.append(i + 1)
      break
for i in range(len(cnt_ls)):
  print(cnt_ls[i])
