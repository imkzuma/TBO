import os

def Prefix(state , string):
    errState = 'q4'
    finishState = 'q3'

    if len(string) >= 3:
        if state == 'q0':
            if string[0] == '1':
                return Prefix('q1' , string[0:])
            else:
                return Prefix(errState , string[0:])
        
        elif state == 'q1':
            if string[1] == '0':
                return Prefix('q2' , string[0:])
            else:
                return Prefix(errState , string[0:])
        
        elif state == 'q2':
            if string[2] == '1':
                return Prefix(finishState , string[0:])
            else:
                return Prefix(errState , string[0:])
        
        elif state == finishState : return state
        elif state == errState : return state

        else : return state
    
    else: return errState

def Suffix(state , string):
    finishState= 'q3'

    if len(string) >= 1:
        suffixString = string[-3:]
        if state == "q0":
            if suffixString[0] == "1":
                return Suffix("q1", suffixString[1:])
            else:
                return Suffix("q0", suffixString[1:])

        elif state == "q1":
            if suffixString[0] == "0":
                return Suffix("q2", suffixString[1:])
            else:
                return Suffix("q1", suffixString[1:])

        elif state == "q2":
            if suffixString[0] == "1":
                return Suffix("q3", suffixString[1:])
            else:
                return Suffix("q0", suffixString[1:])

        elif state == finishState : return finishState
    
    return state


def SubString(state , string):
    finishState = 'q3'
    
    if len(string) >= 1:
        if state == "q0":
            if string[0] == "1":
                return SubString("q1", string[1:])
            else:
                return SubString("q0", string[1:])

        elif state == "q1":
            if string[0] == "0":
                return SubString("q2", string[1:])
            else:
                return SubString("q1", string[1:])
                
        elif state == "q2":
            if string[0] == "1":
                return SubString("q3", string[1:])
            else:
                return SubString("q0", string[1:])

        elif state == finishState : return finishState
    
    return state

def MainMenu():
    print("Tugas Programming DFA")
    print("================================")
    print("Menu: ")
    print("1. Prefix \t\t 2. Suffix \n3. Substring 101 \t 4. Exit")
    print("Masukkan Pilihan: " , end='')
    choice = int(input())

    if choice == 1:
        print("\nMasukkan String: " , end='')
        string = str(input())
        print("Hasil: " , Prefix('q0' , string))

    elif choice == 2:
        print("\nMasukkan String: " , end='')
        string = str(input())

        if len(string) >= 3: 
            print("Hasil: " , Suffix('q0' , string))

        else : print('q0')

    elif choice == 3:
        print("\nMasukkan String: " , end='')
        string = str(input())

        if len(string) >= 3:
            print("Hasil: " , SubString("q0", string))

        else : print("q0")

    os._exit(0)

MainMenu()