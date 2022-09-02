import PySimpleGUI as sg

import random

vittorie = 0

sconfitte = 0

iterations = 50000

for games in range(0, iterations):

    print(f'\n---inizio gioco---\n')

    num_casu = random.sample(range(100), 100)

    box_slip_arr = []                   # empty array. will be filled with the 100 random numbers to give them an index.


    for pos in range(0, 100):                   # for loop that arranges random numbers in the array (100 elements, from 0-99)
        # print(f'{[pos]} : {num_casu[pos]}')         # pos = ordinal number; num_casu[pos] is the slip associated to ordinal number, meaning the random number at position "pos" in the array; num_casu is a random number from 0-99 (100 elements)
        box_slip_arr.append(num_casu[pos])

    # print(f'box_slip_array:{box_slip_arr}')

        scatole_numerate = [pos]

        fogli_casuali = num_casu[pos]

    loop_length = []                                      # empty array. Every time a game loop closes, the loop's length gets appended to this array.

    for i in range(0, 100):                         # outer for loop. it goes through every number from 0 to 99 to start following the slips

        # print(box_slip_arr)

        start = i

        pos = start                                 # ordinal number to start the operation at. By default is set to 0 and goes up by 1 for each loop to 99

        count = 0                                   # length of the game loop. Goes up by one everytime the nested loop repeats. It prints its value (length of the game loop) as soon as the nested loop halts

        # loop = [pos]                              # array. it only contains the starting box (ordinal number). Every new box of the loop gets appended here. It prints its value when the outer for loop breaks. At the end, it contains every box of ONE game loop

        if box_slip_arr[pos] != -1:

            for j in range(0, 100):      # for loop that reads, closes and prints game loops
                # print(num_casu[pos])
                pos = num_casu[pos]                     # checks the random number (num_casu) at position [pos] in the array and jumps to the ordinal number of the same value
                # loop.append(pos)                      # adds the newest box of the list to the array "loop"
                box_slip_arr[pos] = -1
                count = count + 1                       # counts the elements of loop. for each loop it goes up by one; when the loop finishes it prints its value.
                if pos == start:                        # checks if the next box (ordinal number) is the same as the one we started with. If it is, it breaks the loop.
                    break
        else:
            continue

        # print(loop)
        print(f'Lunghezza loop: {count}')
        loop_length.append(count)

    print(f'Loop trovati: {len(loop_length)}')

    def win_lose():

        largest = loop_length[0]

        for k in range(1, len(loop_length)):
            if loop_length[k] > largest:
                largest = loop_length[k]
        print(f'Il più grande loop è lungo {largest}')
        return largest

    maxx = win_lose()

    if maxx <= 50:
        print('Vittoria!')
        vittorie = vittorie + 1
    else:
        print('Sconfitta')
        sconfitte = sconfitte + 1



    print(f'\n---fine gioco---\n')

print('\n\n-----------------------------------------------')
print(f'\nSono state calcolate {iterations} iterazioni')
print('Le percentuali sono:')
print(f'Vittoria:{(vittorie/iterations)*100}%')
print(f'Sconfitta:{(sconfitte/iterations)*100}%')


input('\n\nPremi qualunque tasto per uscire...')
