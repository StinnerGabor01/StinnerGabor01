telb= 2.7
telk= 7.9
autóp= 29.7

telbsz=50
telksz=90
autópsz=130

ő_idő_ó= telb/telbsz+telk/telksz+autóp/autópsz

print("a, feladat:")
print(10*"-")
print("A szükséges idő az egyetemig:", round(ő_idő_ó,2))

print("b, feladat:")
print(10*"-")
print("A szükséges idő az egyetemig:", round(ő_idő_ó*60))

print("c, feladat:")
print(10*"-")
print("A szükséges idő az egyetemig: 7:",60-round(ő_idő_ó*60))