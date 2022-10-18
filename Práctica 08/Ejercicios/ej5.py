filename = 'Ejercicios.py'

with open(filename) as file1:
    lines = file1.readlines()

for line in lines:
    print(line.rstrip())

print(len(lines))

print('Clientito\n' in lines)
print(lines.count('Clientito\n'))


