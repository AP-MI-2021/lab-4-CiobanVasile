def show_menu():
    print("1.Citire lista ")
    print("2.Afisarea listei cu numerele avand doar partea intreaga ")
    print("3.Afisarea tuturor numerelor care aparțin unui interval deschis citit de la tastatură ")
    print("4.Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare ")
    print("5.Afișarea listei obținute în care numerele sunt înlocuite cu un string format din cuvinte ")
    print("x.Iesire program")

def read_list():
    list = []
    list_str = input('Cititi numerele separate printr-un spatiu: ')
    list_str_split = list_str.split(' ')
    for num_str in list_str_split:
        list.append(float(num_str))
    return list

def get_divisors(list):
    '''
    Aceasta functie returneaza o lista cu toate numerele care au partea intreaga divizor al partii fractionare
    Input:
    -O lista de numere float
    Output:
    -O lista de numere float care au partea intreaga divizor al partii fractionare
    '''
    new_list = []
    for i in list:
        if i != int(i):
            str_i = str(i)
            whole = str_i.split('.')[0]
            decimals = str_i.split('.')[1]
            whole =int(whole)
            decimals =int(decimals)
            if decimals % whole == 0:
                new_list.append(i)

    return new_list

def get_integer_part(list):
    '''
    Aceasta functie returneaza o lista formata doar din numere cu partea intreaga, partea fractionara fiind eliminata
    Input:
    -O lista de numere float
    Output:
    - O lista de numere intregi, partea fractionara fiind eliminata
    '''
    new_list = []
    for i in list:
        new_list.append(int(i))

    return new_list

def get_numbers_interval(list, a, b):
    '''
    Returneaza o lista cu numerele cuprinse intr-un interval deschis, care va fi citit de la tastatura
    Input:
    -O lista de numere float
    -a, capatul din stanga a intervalului deschis
    -b, capatul din dreapta a intervalului deschis
    Output:
    -Lista cu numerele cuprinse in intervalul deschis (a,b)
    '''
    new_list = []
    for i in list:
        if i > a and i < b:
            new_list.append(i)

    return new_list

def change_to_string(number):
    '''
    Aceasta functie este una ajutatoare pentru a schimba numarul intr-un sir de caractere
    Input:
    -Un numar float
    Output:
    -Un sir de caractere
    '''
    lista = ['zero','unu','doi','trei','patru','cinci','sase','sapte','opt','noua','virgula','minus']
    str_number = str(number)
    sir_final = ""
    lungime = len(str_number)
    if number != int(number):
        for i in range(0,lungime):
            if str_number[i] == '.':
                sir_final = sir_final + lista[10]
            elif str_number[i] == '-':
                sir_final = sir_final + lista[11]
            elif str_number[i] == '1':
                sir_final = sir_final + lista[1]
            elif str_number[i]== '2':
                sir_final = sir_final + lista[2]
            elif str_number[i] == '3':
                sir_final = sir_final + lista[3]
            elif str_number[i] == '4':
                sir_final = sir_final + lista[4]
            elif str_number[i] == '5':
                sir_final = sir_final + lista[5]
            elif str_number[i] == '6':
                sir_final = sir_final + lista[6]
            elif str_number[i] == '7':
                sir_final = sir_final + lista[7]
            elif str_number[i] == '8':
                sir_final = sir_final + lista[8]
            elif str_number[i] == '9':
                sir_final = sir_final + lista[9]
    else:
        if str_number[0] == '1':
            sir_final = sir_final + lista[1]
        elif str_number[0] == '2':
            sir_final = sir_final + lista[2]
        elif str_number[0] == '3':
            sir_final = sir_final + lista[3]
        elif str_number[0] == '4':
            sir_final = sir_final + lista[4]
        elif str_number[0] == '5':
            sir_final = sir_final + lista[5]
        elif str_number[0] == '6':
            sir_final = sir_final + lista[6]
        elif str_number[0] == '7':
            sir_final = sir_final + lista[7]
        elif str_number[0] == '8':
            sir_final = sir_final + lista[8]
        elif str_number[0] == '9':
            sir_final = sir_final + lista[9]

    return sir_final

def get_numbers_to_char(list):
    '''
    Aceasta functie returneaza o lista in care toate numerele sunt inlocuite cu un sir de caractere care il descriu
    Input:
    -O lista de numere float
    Output:
    -O lista de siruri de caractere care descriu numerele date initial caracter cu caracter
    '''
    new_list = []
    for i in list:
        new_list.append(change_to_string(i))

    return new_list

def test_get_numbers_to_char():
    assert get_numbers_to_char([1.5])==['unuvirgulacinci']
    assert get_numbers_to_char([1])==['unu']
    assert get_numbers_to_char([-3.3])==['minustreivirgulatrei']

def test_get_divisors():
    assert get_divisors([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]
    assert get_divisors([1.5, 1, 2, 3, 4]) == [1.5]
    assert get_divisors([1.4, 10, 20, 30]) == [1.4]
    assert get_divisors([2.3, 3.4, 4.5]) == []

def test_get_numbers_interval():
    assert get_numbers_interval([1.5, -3.3, 8, 9.8, 3.2], -4, 5) == [1.5, -3.3, 3.2]
    assert get_numbers_interval([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 6) == [4, 5]
    assert get_numbers_interval([],3 , 5) == []
    assert get_numbers_interval([1, 2, 3, 4, 5], 0, 6) == [1,2,3,4,5]

def test_get_integer_part():
    assert get_integer_part([1.3,2,3.5]) == [1,2,3]
    assert get_integer_part([1.3,2.4,3.5,4.6]) == [1,2,3,4]
    assert get_integer_part([]) == []
    assert get_integer_part([1,2,3])==[1,2,3]

def main():
    list =[]
    while True:
        show_menu()
        opt = input("Optiunea aleasa: ")
        if opt == '1':
            list=read_list()
        elif opt == '2':
            print("Afisarea listei cu numerele avand doar partea intreaga: ",get_integer_part(list))
        elif opt == '3':
            a=int(input("Capatul din stanga intervalului: "))
            b=int(input("Capatul din dreapta intervalului: "))
            print("Afisarea listei cu numerele care apartin unui interval :",get_numbers_interval(list,a,b))
        elif opt=='4':
            print("Afisarea listei cu numerele care au partea intreaga divizor al partii fractionare: ",get_divisors(list))
        elif opt=='5':
            print("Lista cu stringuri care descriu numerele caracter cu caracter: ",get_numbers_to_char(list))
        elif opt == 'x':
            break
        else:
            print("Optiune invalida ")

if __name__ == '__main__':
    test_get_numbers_interval()
    test_get_integer_part()
    test_get_divisors()
    test_get_numbers_to_char()
    main()