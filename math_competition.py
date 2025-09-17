import time
import matematica

list1 = matematica.which_level()

def one_min_competition(calc):
    start_time = time.time()
    current = 0
    count_true = 0
    count_false = 0
    while time.time() - start_time < 60 :
        print(f"Solve: {calc[current][0]} : ")
        answer = int(input())
        if answer == calc[current][1] :
            count_true += 1
            print("CORRECT!")
        else :
            count_false += 1
        current += 1


    print(f"In one minute you solved : {count_false+count_true} \n You solved {count_true} correctly.")

one_min_competition(list1)