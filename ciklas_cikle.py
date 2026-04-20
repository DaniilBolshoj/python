'''
import random

mano_skaicius = 0

boto_skaicius = 0

while mano_skaicius != 1000:
    boto_skaicius = random.randint(1, 100)
    print('Įveskite savo skaičiu (Įvedus 1000, žaidimas bus sustabdytas): ')
    mano_skaicius = int(input())
    if mano_skaicius == 1000:
        print('Žaidimas sustabdytas!')
        
        if mano_skaicius > boto_skaicius:
            print(mano_skaicius, '>', boto_skaicius)
            print('Jūs laimėjote!')
            
        elif mano_skaicius == boto_skaicius:
            print(mano_skaicius, '=', boto_skaicius)
            print('Lygiosios!')
            
        else:
            print(mano_skaicius, '<', boto_skaicius)
            print('Botas laimėjo!')
            
'''

#ciklas cikle kad botas žaistu prieš kita bota, strategiskai galvodamas koki skaiciu pasirinkti kad laimeti. Limitas nuo 0 iki 1000 ir kiekvienas pasirinktas skaicius kitame zaidime istrinamas, kad botas negaletu pasirinkti to paties skaiciaus du kartus. Kiekvienas botas turi savo strategija, kaip pasirinkti skaiciu, atsižvelgiant i praeitu zaidimu rezultatus. Pavyzdziui, jei pirmas botas laimejo paskutini zaidima, jis gali pasirinkti skaiciu, kuris yra didesnis nei antras botas paskutinis pasirinkimas. Jei antras botas laimejo, jis gali pasirinkti skaiciu, kuris yra mazesnis nei pirmas botas paskutinis pasirinkimas. Jei buvo lygiosios, abu botai gali pasirinkti skaiciu, kuris yra viduryje tarp ju paskutiniu pasirinkimu.

import random

skaiciai = list(range(1, 1001))

boto1_skaicius = 0
boto2_skaicius = 0
boto1_paskutinis_skaicius = 0
boto2_paskutinis_skaicius = 0


def choose_number(available, condition):
    candidates = [x for x in available if condition(x)]
    if not candidates:
        candidates = available
    return random.choice(candidates)


while len(skaiciai) > 0:
    if boto1_skaicius > boto2_skaicius:
        boto1_paskutinis_skaicius = choose_number(
            skaiciai,
            lambda x: x > boto2_paskutinis_skaicius,
        )
    elif boto1_skaicius < boto2_skaicius:
        boto1_paskutinis_skaicius = choose_number(
            skaiciai,
            lambda x: x < boto2_paskutinis_skaicius,
        )
    else:
        boto1_paskutinis_skaicius = choose_number(
            skaiciai,
            lambda x: x > boto2_paskutinis_skaicius and x < boto1_paskutinis_skaicius,
        )

    skaiciai.remove(boto1_paskutinis_skaicius)

    if boto2_skaicius > boto1_skaicius:
        boto2_paskutinis_skaicius = choose_number(
            skaiciai,
            lambda x: x > boto1_paskutinis_skaicius,
        )
    elif boto2_skaicius < boto1_skaicius:
        boto2_paskutinis_skaicius = choose_number(
            skaiciai,
            lambda x: x < boto1_paskutinis_skaicius,
        )
    else:
        boto2_paskutinis_skaicius = choose_number(
            skaiciai,
            lambda x: x > boto1_paskutinis_skaicius and x < boto2_paskutinis_skaicius,
        )

    skaiciai.remove(boto2_paskutinis_skaicius)

    print(f'Boto 1 pasirinkimas: {boto1_paskutinis_skaicius}, Boto 2 pasirinkimas: {boto2_paskutinis_skaicius}')

    if boto1_paskutinis_skaicius > boto2_paskutinis_skaicius:
        print('Boto 1 laimėjo!')
        boto1_skaicius += 1
    elif boto1_paskutinis_skaicius < boto2_paskutinis_skaicius:
        print('Boto 2 laimėjo!')
        boto2_skaicius += 1
    else:
        print('Lygiosios!')

galutinis_rezultatas_pirmo = boto1_skaicius
galutinis_rezultatas_antro = boto2_skaicius

print(f'Galutinis rezultatas - Boto 1: {galutinis_rezultatas_pirmo}, Boto 2: {galutinis_rezultatas_antro}')