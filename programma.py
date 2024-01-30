def ierakstit(teksts, faila_nosaukums):
    fails=open(faila_nosaukums, "w", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def pierakstit(teksts, faila_nosaukums):
    fails=open(faila_nosaukums, "a", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding="utf-8") as fails:
     rindas=fails.readlines()
    return rindas

#print(nolasit("faili/teksts.txt"))

vardi=["Anna", "Maija", "Jānis", "Kaspars"]
uzvardi=["Bērziņa", "Paija", "Ozols", "Kasprets"]
vecums=[23,150,89,11]

ierakstit("","faili/cilveki.txt")



#pierakstit("Sveiki, sienāži, šodien ir darbadiena!\n\"\n", "faili/teksts.txt")