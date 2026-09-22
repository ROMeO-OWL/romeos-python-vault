def filter_even_num(matrix): # function filter even numbers
    f = 0 ; c = 0 
    for i in matrix:
        for j in i:
            if j%2==0: print(f"This number {j} is even\nIt's in the position: {f} , {c}:") 
            c +=1
        c = 0 ; f +=1
# example of use:
# filter_even_num([[1 , 2 , 3], [4, 5 , 6], [5 , 4 , 6] ,[4 , 6 , 4]])

def word_finder(matrix , fw:str): # function is char in string?
    f = 0 ; c = 0
    for i in matrix:
        for j in i:
            if fw in j: print(f"This word {j}, contains the letter: {fw}\nIt's in the position: {f} , {c}:")
            c +=1
        c = 0 ; f +=1
# example of use
# ltt = input("Enter a letter:\n--> ")
# word_finder([["romeo" , "chavez" ], ["dante"  , "chavez" ], ["cuellar" , "valdez" , "Choque"]] , ltt)

def wrd_and_num(matrix): # function display alphanum
    f = 0 ; c = 0
    for i in matrix:
        for j in i:
            if j.isalnum() and not j.isalpha() and not j.isdigit():print(f" {j}, is alphanumeric\nIt's in the position: {f} , {c}")
            c +=1
        c =0 ; f +=1
# example of use
# wrd_and_num([["romeo45" , "dante" , "shirley"] 
#     , ["juan" , "pedro05" , "Teodoro5" ] 
#     , ["zorro54" , "mama03" , "jose"]
# ])     

def filter_numbers_f_alnum(matrix): # function filter numbers of alphanum
    f = 0 ; c = 0
    for i in matrix:
        for j in i:
            print(f"{''.join(x for x in j if x.isdigit())} numbers\nIt's in the position: {f} , {c}") ; c +=1
        c = 0 ; f +=1
# example of use
# filter_numbers_f_alnum([["romeo45654654" , "juan45" , "45"],
#          ["pedro45" , "ozil45646" ,"fer4564ff"],
#          ["bryan45" , "zoto4"],
#          ["amador45" , "pedro4564654"]
#        ])

def filter_letters_f_alnum(matrix): # function filter letters of alphanum
    f = 0 ; c = 0
    for i in matrix:
        for j in i:
            print(f"{''.join(x for x in j if x.isalpha())} letters\nIt's in the position: {f} , {c}") ; c +=1
        c = 0 ; f +=1
# example of use
# filter_letters_f_alnum([["romeo45654654" , "juan45" , "45"],
#          ["pedro45" , "ozil45646" ,"fer4564ff"],
#          ["bryan45" , "zoto4"],
#          ["amador45" , "pedro4564654"]
#        ])

def get_domin_char_type(matrix): # function get dominant char type
    f = 0 ; c = 0
    for i in matrix:
       for j in i:
           cnum = sum(1 for x in j if x.isdigit())   
           clett = sum(1 for x in j if x.isalpha())
           if cnum>clett:print(f"There are more numbers {cnum} than letters {clett} in this str {j}\nIt's in the position: {f} , {c}")
           elif cnum<clett:print(f"There are more letters {clett} than numbers {cnum} in this str {j}\nIt's in the position: {f} , {c}")
           else:print(f"Equal numbers {cnum} and letters {clett} in this str {j}\nIt's in the position: {f} , {c}")
           c +=1
    c = 0 ; f +=1 
# example of use
# get_domin_char_type([["romeo45654654" , "juan45" , "45"],
#          ["pedro45" , "ozil45646" ,"fer4564ff"],
#          ["bryan45" , "zoto4"],
#          ["amador45" , "pedro4564654"]
#        ])

def is_str_num_multiple(matrix , n:int): # function is extracted num multiple
    f = 0 ; c = 0 ; aux =""
    for i in matrix:
        for j in i:
            aux += "".join(x for x in j if x.isdigit())
            if aux!="":
                print(f'''The formed number {aux} is a multiple of {n}\nIt's in the position: {f} , {c}\n'''
                  if int(aux)%n==0 else
                  f'''The formed number {aux} is not a multiple of {n}\nIt's in the position: {f} , {c}\n'''
                )
            else:print(f"Zero digits in {j}\nIt's in the position: {f} , {c}\n")
            c +=1 ; aux = ""
        c = 0 ; f +=1 
# example of use
# n = int(input())
# is_str_num_multiple([["romeo45654654" , "juan45" , "45"],
#        ["pedro45" , "ozil45646" ,"fer4564ff"],
#        ["bryan45" , "zoto"],
#        ["amador45" , "pedro4564654"]], n)

def split_lett_and_num(matrix): # function split lett and num
    pal= [] ; num = []
    auxnum = "" ; auxpal = ""
    for i in matrix:
        for j in i:
            auxpal += "".join(x for x in j if x.isalpha())
            auxnum += "".join(x for x in j if x.isdigit())
            pal.append(auxpal); num.append(auxnum)
            auxpal = "" ; auxnum = ""
    print(*pal , "\n" , *num)  
# # example of use
# split_lett_and_num([["Romeo45" , "Pedro22" , "Shirley18"],
#            ["Juan17" , "Edgar" , "San20"],
#           ["Jose7" , "Maria" , "Juanito8"],
#            ["Solomeo22" , "Dante" , "Ferandno9"]])            