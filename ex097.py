# Um print especial
def escreva(txt):
    c = len(txt) + 4
    print('~'*c)
    print(f'  {txt}')
    print('~' * c)


msg = str(input('Digite alguma coisa:')).strip()
escreva(msg)