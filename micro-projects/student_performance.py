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
    students = {}
    n_studen = get_typed_input(int, "Enter the number of students:\n--> ")
    if n_studen is None or not (0 < n_studen <= 50): print("invalid data or no more attempts") ; return
    for i in range(1, n_studen + 1):
        print(f"student id: {i}")
        name = get_typed_input(str, "Enter student's name:\n--> ")
        name = name.title() if name else None
        l_name = get_typed_input(str, "Enter student's last name:\n--> ")
        l_name = l_name.title() if l_name else None
        age = get_typed_input(int, "Enter student's age:\n--> ")
        val_age = age if (age is not None and 5 <= age<= 25) else None
        note = get_typed_input(float, "Enter student's note:\n--> ")
        val_note = note if (note is not None and 0<= note <=100) else None
        students[i] = [name, l_name, val_age,val_note]

    print("\nNumber of passing students: ",sum(1 for x in students.values() if x[3]>=50.6))
    print("Number of failing students: ",sum(1 for x in students.values() if x[3]<=50.5))
    keymax , maxlist= max(students.items(), key=lambda item:item[1][3])
    keymin , minlis = min(students.items(), key=lambda item: item[1][3])
    print(f"Max note {maxlist[3]} id: {keymax}\nMin note {minlis[3]} id: {keymin}")
    for id, data in students.items(): print(f"\nid {id}: full name: {data[0]} {data[1]}, note: {data[3]}")
 
if __name__ == '__main__':main()