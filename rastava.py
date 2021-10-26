import pprint
import re
import os
import shutil

try:
    os.mkdir('AT')
except:
    print('AT vec postoji')

full = ""
ime_zipa = ''

with open('at.txt', 'r') as file:
    ime_zipa = file.readline().rstrip()
    next(file)
    next(file)
    full = file.read()

l = re.compile("T[0-9]+\n").split(full)

i = 1

for t in l:
    oboje = re.compile("R:\n").split(t)
    test = oboje[0]
    rez = oboje[1]
    with open(os.path.join('AT', str(i) + '.txt'), 'w') as file:
        file.write(test)
    with open(os.path.join('AT', str(i) + '_r.txt'), 'w') as file:
        file.write(rez)

    i = i+1

shutil.make_archive(ime_zipa, 'zip', 'AT')

shutil.rmtree('AT')
