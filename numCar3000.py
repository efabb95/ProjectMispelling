import numpy as np
import json
import ast
from scipy.stats import norm
from pomegranate import *

def numerazione():
    numcaratteri = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0,
                    "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
    training_puliti = open("training_pul3000.txt", "r")

    caratteritot = 0
    for line in training_puliti:
        pos = 0
        while(pos<len(line)):
            if(line[pos].isalpha() == False ):
                caratteritot += 1
            else:
                numcaratteri[line[pos].lower()] += 1
                caratteritot += 1
            pos += 1
    for c in numcaratteri:
        numcaratteri[c] = float(numcaratteri[c])/float(caratteritot)

    myorder=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    modific = [ numcaratteri[c] for c in myorder] #riordino alfabeticamente la lista dei valori
    #print modific

    np.savetxt("numerazione3000.csv", modific ,delimiter=",")
    training_puliti.close()
    return (modific)

def matrice_transizioni():
        training_puliti = open("training_pul3000.txt", "r")

        number = 0
        matrice_transizioni = np.zeros((27, 27))

        for line in training_puliti.readlines():
            for i in range(1, len(line)):
                car_prec = line[i - 1].lower()
                carattere = line[i].lower()
                if ((carattere.isalpha() == True) and (car_prec.isalpha() == True)):
                    matrice_transizioni[(ord(car_prec) - ord('a'), ord(carattere) - ord('a'))] += 1.0
                elif (carattere.isspace() == True) or (car_prec.isspace() == True):
                        if ((car_prec.isalpha() == True) and (carattere.isspace() == True)):
                            matrice_transizioni[(ord(car_prec) - ord('a'), 26)] +=  1.0
                        elif ((car_prec.isspace() == True) and (carattere.isalpha() == True)):
                            matrice_transizioni[(26, ord(carattere) - ord('a'))] += 1.0
                        elif ((car_prec.isspace() == True) and (carattere.isspace() == True)):
                            matrice_transizioni[26, 26] += 1.0

        for i in range(0, matrice_transizioni.shape[0]):
            matrice_transizioni[i, 0:matrice_transizioni.shape[1]] = matrice_transizioni[i, 0:matrice_transizioni.shape[1]] / matrice_transizioni[i, 0:matrice_transizioni.shape[1]].sum()
        #print matrice_transizioni
        training_puliti.close()
        np.savetxt("matrtrans3000.csv", matrice_transizioni ,delimiter=",")
        return (matrice_transizioni)

def matrice_osservazioni():
    training_sporchi = open("training_spo3000.txt", "r")
    training_puliti = open("training_pul3000.txt", "r")
    matrice_osservazioni = np.zeros((27, 27))
    line_pul=training_puliti.readlines()
    numLine=0

    for line in training_sporchi.readlines() :
        for i in range(0, len(line)):
            car_spo = line[i].lower()
            car_pul = line_pul[numLine][i].lower()
            if (car_spo.isalpha() == True):
                matrice_osservazioni[(ord(car_pul) - ord('a'), ord(car_spo) - ord('a'))] += 1
            else:
                matrice_osservazioni[26, 26] +=  1
        numLine += 1

    for i in range(0, matrice_osservazioni.shape[0]):
        matrice_osservazioni[i, 0:matrice_osservazioni.shape[1]] = matrice_osservazioni[i, 0:matrice_osservazioni.shape[1]] / matrice_osservazioni[i, 0:matrice_osservazioni.shape[1]].sum()
    array = np.zeros(27)
    for i in range(0, matrice_osservazioni.shape[0]):
        array[i] = matrice_osservazioni[i, 0:matrice_osservazioni.shape[1]].max()

    for i in range(0, matrice_osservazioni.shape[0]):
        count=0
        for j in range(0, matrice_osservazioni.shape[1]):
            if(matrice_osservazioni[i, j] == 0):
                matrice_osservazioni[i, j] = 0.000001 #epsilon 10^-6
                count += 1
            elif(matrice_osservazioni[i,j] == array[i]):
                max = j
        matrice_osservazioni[i, max] = matrice_osservazioni[i,max] - (count * 0.000001)
    training_sporchi.close()
    training_puliti.close()
    np.savetxt("matross3000.csv", matrice_osservazioni ,delimiter=",")
    return (matrice_osservazioni)
#    for i in range(0, matrice_osservazioni.shape[0]):
#        print round(matrice_osservazioni[i, 0:matrice_osservazioni.shape[1]].sum())

def json_matrice(matrice):
    lista = list()
    for i in range(97, 124):
        for j in range(97, 124):
            if(j == 97):
                data=[{}]
            if (j < 123):
                data[0][chr(j)] = matrice[i-97, j-97]
            else:
                if(j == 123):
                    data[0][chr(32)] = matrice[i-97, j-97]

        lista.append(json.dumps(data, sort_keys = False))
    print lista
    return (lista)

def convert_sample(a):
    array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z", " "]
    i = 0
    while (i < len(a)):
        c = a[i]
        print array[int(c)]
        i += 1

def ordina_dict(dict):
    #ordine = [" ", "a", "c", "b", "e", "d", "g", "f", "i", "h", "k", "j", "m", "l", "o", "n", "q", "p", "s",
    #        "r", "u", "t", "w", "v", "y", "x", "z"]
    #riordino il dizionario in modo tale ho la corrispondenza esatta tra chiave e valore
    #lo faccio per ogni stato
    numer=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z", " "]
    res = {}
    ord = dict.values()
    i = 0
    while i<len(numer):
        dict2 = {numer[i] : ord[i]}
        res.update(dict2)
        i += 1
    return res

def creazione_modello(matrice_transizioni, matrice_osservazioni, numerazione):
    #T = matrix_to_json(matrice_T)
    numer=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z", " "]
    seq = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z", " ")
    oss_a = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0,
            "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, " ":0}
    ordinao = {}
    ordina = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0,
            "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, " ":0}

    print ordinao
    model = HiddenMarkovModel('Mispelling3000')
    s = list()
    k=0
    i = 0
    for j in range(0, 27):
        for c in oss_a:
            oss_a[c] = matrice_osservazioni[j][i]
            i += 1
            if(i>26):
                oss = ordina_dict(oss_a)
                if(j>=26):
                    s.append(State(DiscreteDistribution(oss), name= "Space"))
                else:
                    s.append(State(DiscreteDistribution(oss), name= ""+chr(97+j)))
                i = 0
    i = 0
    for i in range(0, 26):
        model.add_states(s[i])
    for i in range(0, 26):
        model.add_transition(model.start, s[i], numerazione[i])

    for i in range(0, 27):
        for j in range(0, 27):
            model.add_transition(s[i], s[j], matrice_transizioni[i, j])

    model.bake()
    print model
    unlist=['\x82', '\xac','\x87', '\xbd', '\xbe', '\xb6', '\xa4',
            '\xc5', '\x9f', '\xc4', '\xb1', '\xc3', '\xbc', '\xa3',
            '$', '\x98', '%', '\xa6', '\x9c', '\x9d', '|', ']',
            '[', '_', '\xc2', '\xa0', '\x99', ';', '+', '=', '*',
            '\xe2', '\x80', '\x94','?', '\n', ':', '/', '!', '\'',
            ',', '.', '-', '"', '(', ')', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', '@', '&', '\xef', '#']
    testProv = open("test_spo3000.txt", "r")
    testPul = open("test_pul3000.txt", "r")
    correzioneTemp = open("correzioneTemp3000.txt", "w")
    correzione = open("correzione3000.txt", "w")
    lines_pulite = testPul.readlines()
    numLine = 0
    i=0
    for line in testProv:
          shortseq = [x for x in line.lower() if x not in unlist] #pulisco dai caratteri di cui non esiste lo stato
          logp, path = model.viterbi(shortseq[0:len(shortseq)])
          [state.name for i, state in path]
          for i in range(1, len(path)):
              if (json.loads(ast.literal_eval(json.dumps(str(path[i][1]), sort_keys= False))).get('name') == 'Space'):
                  x = x+ " "
              else:
                  x = x+""+json.loads(ast.literal_eval(json.dumps(str(path[i][1]), sort_keys= False))).get('name')
          correzioneTemp.write(x)
    correzioneTemp.close()
    correzioneTemp = open("correzioneTemp3000.txt", "r")
    i = 0
    for line in correzioneTemp:
        if i != 0:
	        correzione.write(line)
        i = i + 1
    testProv.close()
    testPul.close()
    correzioneTemp.close()
    correzione.close()
    #plt.plot()
    #model.draw()
    return model
    #myorder=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    #        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    #oss_a = [ oss_a[c] for c in myorder] #riordino alfabeticamente la lista dei valori
    #print modific

    #lista_distrib = list()
    #for i in range(0, 27):
    #    lista_distrib.append((matrice_osservazioni[i][1:len(matrice_osservazioni[i])-1]))
    #print lista_distrib[1]

    #states = list()
    #for j in range(0, 27):
    #    if(j < 26):
    #        states.append(State(lista_distrib[j], name = ""+chr(j+97) ))
    #    else:
    #        if(j == 26):
    #            states.append(State(lista_distrib[j], name = "Space" ))

    #model.add_states(states)

    #pi = json.loads(pi.to_json())
    #pi = pi['parameters']
    #print pi[0]['z']






retoss = matrice_osservazioni()
rettran = matrice_transizioni()
retnum = numerazione()
#json_matrice(retoss)
creazione_modello(rettran, retoss, retnum)
