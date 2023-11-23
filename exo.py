def count(s):
    dico = dict()
    dico[i] = 0
    for i in s:
        dico[i] += 1
    return dico

print(count("coucou"))