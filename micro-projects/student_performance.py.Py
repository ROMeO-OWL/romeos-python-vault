def get_integer(prompt=''):
    for _ in range(3):
        try: return int(input(prompt))
        except ValueError: print("debes ingresar un number integer!!")
    return None

def main():
    students = {}
    n_studen = get_integer("Enter the number of students:\n--> ")
    if n_studen is None or not (0<n_studen<=50): print("Date no validos or intenos agotados") ; return
    for i in range(1,n_studen+1):
        print(f"Student Id {i}\n")
        student = []
        student.append(age) if (age := get_integer("Enter your age:\n--> ")) is not None else print("Dato no valido")

if __name__ == '__main__':main()
