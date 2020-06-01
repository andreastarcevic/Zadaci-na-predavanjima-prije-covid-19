# naredbe selekcije

ime = input('Ime: ')

if len(ime) > 5:
    print('ime {} je dugacko'.format(ime))
elif len(ime) > 2:
    print('ime {} je srednje'.format(ime))
else :
    print('ime {} je kratko'.format(ime))