"""
aplikacija: Napad Orkova v0.0.1
autor: Andrea Starcevic

"""

import random # generiranje slucajnog broja
# kontrole
igraj = 'd'
okupanti = ['neprijatelj', 'prijatelj', 'slobodno']

# zaglavlje i izbornik

sirina = 72
ukras = '-' * sirina
poruka = """
    Hrabri vitez Talion vraća se iz boja iz želi odmoriti.
    U seocu se nalazi 5 kućica i želi ući u jednu od njih.
    Hrabri vitez ne zna da u ovom području ima neprijatelja.
    Odluči se za jedna vrata...

"""
print(ukras)
print("\033[1m" + "Napad Orkova v0.0.1:" + "\033[0m")
print(poruka)
print("\033[1m" + "Misija:" + "\033[0m")
print("\tOdaberi gdje se Talion može odmoriti...")
print("\033[1m" + "SAVJET:" + "\033[0m")
print("\tPAZI kako biraš jer je neprijatelj u blizini!")
print(ukras)

# glavna petlja 
while igraj == 'd':
    kucice = []
    while  len(kucice) < 5:
        # odaberi nasumicno stanje
        komp_odabir = random.choice(okupanti)
        # dodaj u kucicu 
        kucice += [komp_odabir]

    # pitaj korisnika da odabere kućicu
    poruka = "\n\033[1m" + "Odaberi kućicu za ulaz (1-5): " + "\033[0m"
    odabir = input(poruka)
    idx = int(odabir)

    print('otkrivamo tko je u kućici: ')
    for i in range(len(kucice)):
        okupant_info = "{}:{}".format(i+1,kucice[i])
        if i+1 == idx:
            okupant_info = "\033[1m" + okupant_info + "\033[0m"
        poruka += okupant_info + " "
    print ("\t" + poruka)
    print(ukras)
    print("\033[1m" + "Ulazim u kućicu {}".format(idx) + "\033[0m")



    # proglasi pobjednika
    if kucice[idx-1] == 'neprijatelj': 
        print("\033[1m" + "IZGUBIO SI :( više sreće drugi puta!" + "\033[0m")
    else:
         print("\033[1m" + "Čestitamo! POBIJEDILI STE !!!" + "\033[0m")

    
    


    igraj = input("Igrati ponovno ? DA (d)/NE (n) ")