
# Ini merupakan fungsi dari L1 untuk mencari
# string yang diawali dan diakhiri dengan simbol yang sama
def SameString(state , string): 
    #state adalah state awal, string adalah string yang akan diuji

    firstFinishState = 'q1' #FINISH STATE AWAL YAITU q1
    secondFinishState = 'q3' #FINISH STATE KEDUA YAITU q3

    if(string != ""): #Jika string tidak kosong
        print(f'δ({ state } , { string[0] }) = ', end = '') 
        #Menampilkan delta-topi state dan string yang akan diuji

        if(state=="q0"): #Jika state awal adalah q0
            if(string[0]=="0"): #Jika string yang akan diuji adalah 0
                print(secondFinishState) #Maka akan menampilkan finish state kedua yaitu q3
                return [SameString(secondFinishState, string[1:])] 
                #Mengembalikan fungsi dengan state awal finish state kedua 
                # dan string yang akan diuji adalah string yang akan diuji tanpa karakter pertama

            else: #Jika string yang akan diuji bukan 0
                print(firstFinishState) #Maka akan menampilkan finish state awal yaitu q1
                return [SameString(firstFinishState, string[1:])]
                #Mengembalikan fungsi dengan state awal finish state awal

        elif(state == firstFinishState): #Jika state awal adalah finish state awal
            if(string[0]=="0"): #Jika string yang akan diuji adalah 0
                print("q2") #Maka akan menampilkan state q2
                return [SameString("q2", string[1:])] 
                # Mengembalikan fungsi dengan state awal q2

            else: #Jika string yang akan diuji bukan 0
                print(firstFinishState) #Maka akan menampilkan finish state awal yaitu q1
                return [SameString(state, string[1:])] 
                # Mengembalikan fungsi dengan state awal finish state awal

        elif(state=="q2"):  #Jika state awal adalah q2
            if(string[0]=="0"): #Jika string yang akan diuji adalah 0
                print(state) #Maka akan menampilkan state q2
                return [SameString(state, string[1:])]
                # Mengembalikan fungsi dengan state awal q2

            else: #Jika string yang akan diuji bukan 0
                print(firstFinishState) #Maka akan menampilkan finish state awal yaitu q1
                return [SameString("q1", string[1:])] 
                # Mengembalikan fungsi dengan state awal finish state awal

        elif(state == secondFinishState): #Jika state awal adalah finish state kedua
            if(string[0]=="0"): #Jika string yang akan diuji adalah 0
                print(secondFinishState) #Maka akan menampilkan finish state kedua yaitu q3

                return [SameString(state, string[1:])]
                # Mengembalikan fungsi dengan state awal finish state kedua

            else: #Jika string yang akan diuji bukan 0
                print("q4") #Maka akan menampilkan state q4

                return [SameString("q4", string[1:])]
                # Mengembalikan fungsi dengan state awal q4

        elif(state=="q4"): #Jika state awal adalah q4
            if(string[0]=="0"): #Jika string yang akan diuji adalah 0
                print(secondFinishState) #Maka akan menampilkan finish state kedua yaitu q3

                return [SameString(secondFinishState, string[1:])]
                # Mengembalikan fungsi dengan state awal finish state kedua

            else: #Jika string yang akan diuji bukan 0
                print(state) #Maka akan menampilkan state q4

                return [SameString(state, string[1:])]
                # Mengembalikan fungsi dengan state awal q4

    else: #Jika string kosong
        if state == firstFinishState or state == secondFinishState:
        # Jika state awal adalah finish state awal atau finish state kedua
            print('Finish State = ', state) # Maka akan menampilkan finish state

        else: # Jika state awal bukan finish state
            print('Dead State = ', state) #Maka akan menampilkan dead state