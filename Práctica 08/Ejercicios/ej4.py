import re

phrase = 'La vida está llena de matices, detalles y elementos que muchas veces nos hacen parar y dudar.'

print(re.findall('elementos',phrase,flags = re.IGNORECASE))
print(re.sub('elementos','circunstancias',phrase,flags = re.IGNORECASE))
