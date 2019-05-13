import random
import re

def clean_tweet():
    tweet = open("down3000.txt", "r+")
    pul = open("puliti3000.txt", "w+")
    for line in tweet:
        newline = re.sub('https:?[A-Za-z0-9/\.]+',"",line)
        pulline1 = re.sub("[^a-zA-Z0-9 ]+","", newline)
        pulline = ''.join([i for i in pulline1 if not i.isdigit()])
        pul.write(pulline+"\n")
		

def modifica_tweet():
    tweet_puliti = open("puliti3000.txt", "r")
    tweet_sporchi = open("sporchi3000.txt", "w")
    char_vicini = {"q": "wsa", "w": "qasde", "e": "wsdfr", "r": "edfgt", "t": "rfghy", "y": "tghju", "u": "yhjki", "i": "ujklo", "o": "iklp",
                      "p": "ol", "a": "qwsz", "s": "azxdew", "d": "sxcfre", "f": "dcvgtr", "g": "fvbhyt", "h": "gbnjuy", "j": "hnmkiu",
                      "k": "jmloi", "l": "pok", "z": "asx", "x": "zsdc", "c": "xdfv", "v": "cfgb", "b": "vghn", "n": "bhjm", "m": "njk"}
	
    for line in tweet_puliti:
        pos = 0
        while(pos < len(line)):
            if(line[pos].isalpha() == True):
                char_select = line[pos]
                c = random.random()
                if(c<=0.1):
                    cran = random.choice(char_vicini[char_select.lower()])  #dato il char selezionato in minuscolo, cerco i suoi vicini e scelgo random
                    parteInizio = line[0:pos]
                    parteFine = line[pos+1:]
                    line = parteInizio+cran+parteFine
                pos += 1
            else:
                pos += 1
            if pos == len(line):
                tweet_sporchi.write(line)

    tweet_puliti.close()
    tweet_sporchi.close()

def divisione_tweet():
    tweet_puliti = open("puliti3000.txt", "r")
    tweet_sporchi = open("sporchi3000.txt", "r")
    tweet_training_pul = open("training_pul3000.txt", "w")
    tweet_test_pul = open("test_pul3000.txt", "w")
    tweet_training_spo = open("training_spo3000.txt", "w")
    tweet_test_spo = open("test_spo3000.txt", "w")

    puliti = open("puliti3000.txt")
    lines_number = sum(1 for line in puliti)
    puliti.close()

    training = int(0.8*lines_number)
    i = 1
    for line in tweet_puliti:
        if (i <= training):
            tweet_training_pul.write(line)
        else:
            tweet_test_pul.write(line)
        i += 1

    sporchi = open("sporchi3000.txt")
    lines_number = sum(1 for line in sporchi)
    sporchi.close()

    training = int(0.8*lines_number)
    i = 1
    for line in tweet_sporchi:
        if (i <= training):
            tweet_training_spo.write(line)
        else:
            tweet_test_spo.write(line)
        i += 1
    tweet_puliti.close()
    tweet_sporchi.close()
    tweet_training_pul.close()
    tweet_test_pul.close()
    tweet_training_spo.close()
    tweet_test_spo.close()

clean_tweet()
modifica_tweet()
divisione_tweet()
