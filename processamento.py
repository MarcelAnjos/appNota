def calc_media(notas=[]):
    media= sum(notas) / len(notas)
    notas = notas.append(media)
    if media <=0:
        return print("ERRO: Valores incorretos!")
    if media >10:
        media = 10
    return media

def status(n):
    if n >= 7:
        n="APROVADO"
        return n
    else:
        n="RECUPERACAO"
        return n