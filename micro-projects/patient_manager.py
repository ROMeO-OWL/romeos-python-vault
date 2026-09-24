def get_typed_input(data_type, prompt='',error_msg="invalid input"):
    for _ in range(3):
        try:
            val = input(prompt)
            if data_type == str:
                if val.strip():return val
                print("the text cannot be empty") ; continue
            return data_type(val)
        except ValueError: print(error_msg)
    return None

def main():
    while opc!=5: 
        opc = get_typed_input(int, "Enter opcion:\n1) Enter date\n2) Info del pacientes\n3) pacientes con consulta\n4) listado de pacientes\n5) Exit\n--> ")
        if opc is None: print("invalid data or no more attempts") ; return

if __name__ == '__main__':main()
