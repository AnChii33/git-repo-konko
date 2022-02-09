# MORSE CODE/DECODE using python dictionary

# Dictionary representing the morse code chart
# Source: https://morsecode.world/international/morse2.html

MORSE_DICT={'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-', '&':'.-...', 
            "'":'.----.', '@':'.--.-.', ':':'---...', 
            '=':'-...-', '!':'-.-.--','"':'.-..-.', 
            ' ':'/', '+':'.-.-.'}

print()
print(">>>>> MORSE CODEC <<<<<")
print()

while True:
    print("For ENCODING TEXT to MORSE SCRIPT, type 'E' and press ENTER")
    print("For DECODING MORSE SCRIPT to TEXT, type 'D' and press ENTER")
    print("To EXIT, type 'EXIT' and press ENTER")
    chk=input("Enter your choice: ")
    print()

    if chk=='E':
        txt=input("Enter alphanumeric text: ").upper()
        txt="".join([k for k in txt if k in list(MORSE_DICT.keys())])
        c=""
        for l in txt:
            if l != " ":
                c += MORSE_DICT[l]+" "
            else:
                c += "/ "
        print("MORSE SCRIPT for entered text:",c, end="\n\n")
        print()

    elif chk=='D':
        try:
            mr=input("Enter morse code script: ").strip()
            mr += " "
            dec=""
            ct=""
            for chr in mr:
                if chr!=" ":
                    sp=0
                    ct+=chr
                else:
                    sp+=1
                    if sp==2:
                        dec += ' '
                    else:
                        dec += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(ct)]
                        ct=""
            print("TEXT for entered MORSE SCRIPT:",dec, end="\n\n")
        except Exception:
            print("Invalid Morse Code! Try again..")
        print()
    
    elif chk=="EXIT":
        qc=input("Are you sure you want to exit (y/n): ")
        if qc=="y":
            print("Thank you for using MORSE CODEC.")
            print()
            break
        
    else:
        print("Invalid input! Try again...")
        print()
        continue