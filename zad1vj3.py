# vjerojatnost kise

kisa = input('unesi broj za vjerojatnost kiše: ')
kisa = float(kisa)

if kisa >= 0.5 and kisa <= 1:
    print('Treba ponijeti kišobran')
elif kisa >= 0.0 and kisa <= 0.5:
    print('Ne treba ponijeti kišobran')
else:
    print('Neispravna vrijednost')