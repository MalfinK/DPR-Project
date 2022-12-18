import re

# kalimat negatif
kata_kunci_negatif = ['ga_seru', 'ga_lucu', 'ga_peduli']
pencarianBarisNegatif = [[] for x in range(len(kata_kunci_negatif))]
pencarianKalimatNegatif = [[] for x in range(len(kata_kunci_negatif))]

get_data = open(r'hasil_crawler.txt', 'r', encoding='utf-8')

barisPerSatuKalimat = list(get_data.read().split('\n\n'))

for indexNo, baris in enumerate(barisPerSatuKalimat):
    hanyaKata = re.sub(
        pattern = r"[^\w\s]",
        repl = "",
        string = baris.lower())
    for indexKata, kataNegatif in enumerate(kata_kunci_negatif):
        kataDalamKalimat = hanyaKata.split()
        for kata in kataDalamKalimat:
            if kata.lower() == kataNegatif and indexNo not in pencarianBarisNegatif[indexKata]:
                pencarianBarisNegatif[indexKata].append(indexNo)
                pencarianKalimatNegatif[indexKata].append(baris)

# kalimat positif
kata_kunci_positif = ['bagus', 'ngakak', 'ketawa', 'lucu']
pencarianBarisPositif = [[] for x in range(len(kata_kunci_positif))]
pencarianKalimatPositif = [[] for x in range(len(kata_kunci_positif))]

for indexNo, baris in enumerate(barisPerSatuKalimat):
    hanyaKata = re.sub(
        pattern = r"[^\w\s]",
        repl = "",
        string = baris.lower())
    # print(kata_kunci_positif)
    for indexKata, kataPositif in enumerate(kata_kunci_positif):
        kataDalamKalimat = hanyaKata.split()
        for kata in kataDalamKalimat:
            if kata.lower() == kataPositif and indexNo not in pencarianBarisPositif[indexKata]:
                pencarianBarisPositif[indexKata].append(indexNo)
                pencarianKalimatPositif[indexKata].append(baris)


with open("hasil_crawler2.txt", "w", encoding="utf8") as hasilKeseluruhan:
    
#     print(f'''
# Kelompok \t: 5
# Prodi \t\t: Ilmu komputer
#     ''', file=hasilKeseluruhan)

    print("Kalimat-Kalimat Negatif", file=hasilKeseluruhan)
    total = 0   
    for indexNo, kataNegatif in enumerate(kata_kunci_negatif):
        total += len(pencarianBarisNegatif[indexNo])
        print(f'\n\n- Kalimat dengan kata "{kataNegatif}" ==> {len(pencarianBarisNegatif[indexNo])}\n', file=hasilKeseluruhan)
        for indexKalimat, kalimat in enumerate(pencarianKalimatNegatif[indexNo]):
            print(f'{indexKalimat + 1}. {kalimat}', file=hasilKeseluruhan)

    print("Kalimat-Kalimat Positif", file=hasilKeseluruhan)
    for indexNo, kataPositif in enumerate(kata_kunci_positif):
        total += len(pencarianBarisPositif[indexNo])
        print(f'\n\n- Kalimat dengan kata "{kataPositif}" ==> {len(pencarianBarisPositif[indexNo])}\n', file=hasilKeseluruhan)
        for indexKalimat, kalimat in enumerate(pencarianKalimatPositif[indexNo]):
            print(f'{indexKalimat + 1}. {kalimat}', file=hasilKeseluruhan)