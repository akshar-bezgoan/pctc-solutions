pi_digits = '31415926535897932384626433832795028841971693993751'
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
output = []
original = input()
original = original.strip(' ')
for i in range(len(original)):
  idx = alpha.index(original[i])
  if i % 2 == 0:
    idx += int(pi_digits[i])
  else:
    idx -= int(pi_digits[i])
  output.append(alpha[idx])
print(output)