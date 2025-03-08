stairs = int(input())
print('___')
for i in range(1, stairs):
    print('#'*(2*i + 1) + ']' + '_')
print('#'*(2*stairs + 1) + ']' + '___')