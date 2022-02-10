import time

try:
    nazov_suboru = input("Zadaj mi nazov suboru (aj s priponou): ")
    with open(nazov_suboru) as subor:
        basnicka = subor.read()
except:
    print("nemam subor :(")
    quit()

try:
    pocet_suborov = int(input("Zadaj pocet suborov: "))
except ValueError:
    print("toto nepojde")
    quit()

slova = []
slova += basnicka.split()
i = int(0)

for slovo in slova:
    #utvor subor  vloz donho slovo
    novy_t = time.time()
    filename = "%s.txt" % novy_t
    otvor_s = open(filename, "w")
    print(slova[i], file=otvor_s)
    otvor_s.close()
    i += 1
    if i >= pocet_suborov:
        print("hotovo")
        quit()