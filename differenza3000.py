def splitter(sentence1, sentence2):
    n = 0
    partot = 0
    for word_from_1, word_from_2 in zip(sentence1.split(), sentence2.split()):
        if word_from_1 == word_from_2:
            n += 1
        partot += 1
    return(partot, n)

def diff_checker():
    test_pul = open("test_pul3000.txt", "r")
    correz = open("correzione3000.txt", "r")
    partot = 0
    paruguali = 0
    for linepul, line in zip(test_pul, correz):
        (tot, uguali) = splitter(linepul.lower(), line.lower())
        partot += tot
        paruguali += uguali
    print partot, paruguali
    percgiuste = float(paruguali)/float(partot)
    print("Percentuale parole uguali - Corrette")
    print round(100*percgiuste, 1)
    test_pul.close()
    correz.close()
    test_pul = open("test_pul3000.txt", "r")
    test_spo = open("test_spo3000.txt", "r")
    partotspo = 0
    parugualispo = 0
    for linepul, linespo in zip(test_pul, test_spo):
        (totsp, ugualisp) = splitter(linepul.lower(), linespo.lower())
        partotspo += totsp
        parugualispo += ugualisp
    print partotspo,parugualispo
    percgiustespo = float(parugualispo)/float(partotspo)
    print("Percentuale parole uguali - Sporche")
    print round(100*percgiustespo, 1)
    if(percgiuste >= percgiustespo):
        print("Percentuale miglioramento")
        print round(100*(percgiuste-percgiustespo), 1)
    test_pul.close()
    test_spo.close()

diff_checker()
