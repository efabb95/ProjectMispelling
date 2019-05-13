from pomegranate import *
import warnings
import numpy as np
import matplotlib
import networkx as nx
import csv
import ast
from Tkinter import *
master = Tk()

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

def modelImport():
    numerazione = np.zeros(26)
    with open('numerazione3000.csv') as myFile:
        reader = csv.reader(myFile)
        i = 0
        for row in reader:
            numerazione[i] = row[0]
            i += 1

    matrT = np.zeros((27,27))
    with open('matrtrans3000.csv') as myFileT:
        readerT = csv.reader(myFileT)
        i = 0
        j = 0
        for row in readerT:
            for i in range(0,27):
                matrT[j][i] = row[i]
            j += 1

    matrO = np.zeros((27,27))
    with open('matross3000.csv') as myFileO:
        readerO = csv.reader(myFileO)
        i = 0
        j = 0
        for row in readerO:
            for i in range(0,27):
                matrO[j][i] = row[i]
            j += 1

    model = HiddenMarkovModel('Mispelling')
    oss_a = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0,
        "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, " ":0}
    s = list()
    k=0
    i = 0
    for j in range(0, 27):
        for c in oss_a:
            oss_a[c] = matrO[j][i]
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
            model.add_transition(s[i], s[j], matrT[i, j])

    model.bake()
    return model


# Create this method before you create the entry
def calcoloViterbi():
    unlist=['\x82', '\xac','\x87', '\xbd', '\xbe', '\xb6', '\xa4',
            '\xc5', '\x9f', '\xc4', '\xb1', '\xc3', '\xbc', '\xa3',
            '$', '\x98', '%', '\xa6', '\x9c', '\x9d', '|', ']',
            '[', '_', '\xc2', '\xa0', '\x99', ';', '+', '=', '*',
            '\xe2', '\x80', '\x94','?', '\n', ':', '/', '!', '\'',
            ',', '.', '-', '"', '(', ')', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', '@', '&', '\xef', '#']
    modello = modelImport()
    contento = entry.get().lower()
    contentoS = [x for x in contento if x not in unlist] #pulisco dai caratteri di cui non esiste lo stato
    logp, path = modello.viterbi(contentoS[0:len(contentoS)])
    x = ""
    for i in range(1, len(path)):
        if (json.loads(ast.literal_eval(json.dumps(str(path[i][1]), sort_keys= False))).get('name') == 'Space'):
            x = x+ " "
        else:
            x = x+""+json.loads(ast.literal_eval(json.dumps(str(path[i][1]), sort_keys= False))).get('name')
    entry1.delete(0, END)
    entry1.insert(0, x)

master.title("Calcolo Viterbi - 3000")
master.geometry("300x200")
Label(master, text="Insert tweet: ").grid(row=0, sticky=W, padx=10, pady=10)
Label(master, text="Result: ").grid(row=1, sticky=W, padx=10)

entry = Entry(master, justify="center")
entry.grid(row=0, column=1, ipadx=20, padx=10)
entry1 = Entry(master, justify="center")
entry1.grid(row=1, column=1, ipadx=20)

but = Button(master, text="Viterbi", command=calcoloViterbi, justify="center")
but.grid(row=2, column=1, pady=10)
but1 = Button(master, text="Quit", command=quit, justify="center")
but1.grid(row=2, column=0)


mainloop()
