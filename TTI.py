tm= float(input("Kérem adja meg a magasságát méterben: "))
tt= int(input("Kérem adja meg a testtömegét kg-ban: "))
tti= tt/tm**2
ntt_a= tm**2*20
ntt_m= tm**2*25

print(20*"*"+5*"-"+20*"*")
print("Az ön testtömegindexe:", round(tti,2),"%")
print("Az ön magasságához az ideális testtömeg:", round(ntt_a,2),"kg és", round(ntt_m,2), "kg között van")