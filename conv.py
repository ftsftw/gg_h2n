tfile = input('Enter file: ')

# try:
#     tfile = open(nfile)
# except:
#     print("Can't find file", nfile)
#     quit()

import fileinput

with fileinput.FileInput(tfile, inplace=True, backup='.bak') as file:

    for line in file:
        if 'Dealt' not in line:
            print(line.replace('Poker Hand #RC', 'PokerStars Hand #20'), end='')
        else:
            if '[' in line:
                print(line.replace('Poker Hand #RC', 'PokerStars Hand #20'), end='')
