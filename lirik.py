import sys
import time


def putar_lirik():
    lirik = [
        ("Sorrowful reunion", 0.1), 
        ("Was inevitable", 0.2),
        ("Living an illusion", 0.1), 
        ("oh but we're so compatible", 0.1),
        ("And I miss all the X and Os", 0.1),
        ("Do you regret the path you chose", 0.1),
        ("With me?", 0.1),
    ]

    delay = [2, 2.5, 0.6, 2.3, 2, 3, 1.2]
    print("\nA Sorrowful Reunion - Reality Club")
    time.sleep(7)
    for i, (baris_musik, delay_kata) in enumerate(lirik):
        for kata in baris_musik:
            print(kata, end='') 
            sys.stdout.flush()
            time.sleep(delay_kata)
        time.sleep(delay[i])
        print('')
    print("     ~~~Code by Dafun~~~     ")


putar_lirik()    