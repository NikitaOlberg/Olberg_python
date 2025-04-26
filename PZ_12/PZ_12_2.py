# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.

def upstr(string):
    yield from[i.upper() for i in string]

words = "привет пока"
new_str = upstr(words)
print(''.join(new_str))

