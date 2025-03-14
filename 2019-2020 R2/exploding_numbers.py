D = {'6': '350', '7': '50', '8': '3505', '9': '35052', '0':'0'}
num = input()
ans = []
for i in range(len(num)):
      ans.append(D.get(num[i], num[i]))

print(''.join(ans))

