lista = ['j', 'c', 'z', 'k']
tajny_przekaz = []


def secret_message(lista, secret):
    while lista:
        lista.reverse()
        hint = lista.pop()
        print(hint)
        tajny_przekaz.append(hint)

print(lista)
print(tajny_przekaz)
