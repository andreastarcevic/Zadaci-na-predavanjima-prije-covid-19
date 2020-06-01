# kamen, papir, škare

igrac1 = input('Unesi k, p ili s: ')
igrac2 = input('Unesi k, p ili s: ')



if igrac1 == 'k' and igrac2 == 'p':
    print('pobijedio je igrac 2')
elif igrac1 == 'k' and igrac2 == 's':
    print('pobijedio je igrac 1')
elif igrac1 == 'k' and igrac2 == 'k':
    print('Izjednačeno je!')
    
if igrac1 == 'p' and igrac2 == 'p':
    print('Izjednačeno je!')
elif igrac1 == 'p' and igrac2 == 's':
    print('pobijedio je igrac 2')
elif igrac1 == 'p' and igrac2 == 'k':
    print('pobijedio je igrac 1')

if igrac1 == 's' and igrac2 == 'p':
    print('pobijedio je igrac 1')
elif igrac1 == 's' and igrac2 == 's':
    print('Izjednačeno je!')
elif igrac1 == 's' and igrac2 == 'k':
    print('pobijedio je igrac 2')