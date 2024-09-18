#Author Mikael Foxell
#Date 2024-09-18

print(f'Ei23 - genrep praktiskt prov ht24\nAnge 0 för att avsluta')
resistors = list()
resistor = 0
while True:
    res = int(input('\nAnge resistorvärde: '))
    if res == 0:
        resistors.append(res)
        break
    else:
        resistors.append(res)
    print(f'Nuvarande resistorer: {resistors}')
    
if resistors[0] == 0:
    print(f'Serieresistans: 0\nParallellresistans: 0')
else:
    i = 0
    serieresistans = 0
    parallellresistans = 0
    print(f'Resistorvärden: ', end= '')
    for resistor in resistors:
        if resistors[i] != 0:  
            print(f'{resistors[i]}', end=' ')
            serieresistans += resistors[i]
            parallellresistans += 1/resistors[i]
            i+=1
    parallellresistans = 1/parallellresistans
    print(f'\nTotal serieresistans: {serieresistans}')
    print(f'Total parallellresistans: {parallellresistans}')