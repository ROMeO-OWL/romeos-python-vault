# use py 3.10 or later
from datetime import *
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
    id = 1_000 ; patients = {}
    while opt!=5: 
        opt = get_typed_input(int, "Enter option:\n1) Enter date\n2) Patient info by id or SSN\n3) Patients with appointment\n4) List of patients\n5) Exit\n--> ")
        if opt is None or 6>opt>0: print("invalid data or no more attempts") ; return
        match opt:
            case 1:
                ssn = get_typed_input(int, "Enter CI:\n--> ")
                ssn = ssn if 8<=len(str(ssn))>=6 else 0
                name = get_typed_input(str, "Enter patient's name:\n--> ")
                name = name.title() if name else "nothing"
                l_name = get_typed_input(str, "Enter patient's last name:\n--> ")
                l_name = l_name.title() if l_name else "nothing"
                age = get_typed_input(int, "Enter patient's age:\n--> ")
                val_age = age if (age is not None and 0 <= age<= 100) else 0
                address = get_typed_input(str , "Enter address:\n--> ")
                address = address.lower() if address else "nothing"
                phone = get_typed_input(str, "Enter phone:\n--> ")
                phone = phone if 13<=len(phone)>=8 else 0
                patients[id] = [ssn , name ,l_name ,age, address,phone,datetime.now()]
                id +=1
            case 2:
                opt = get_typed_input(int, "Enter CI or user ID\n--> ")
                if opt is None: print("invalid data or no more attempts") ; return
                
            case 3: pass
            case 4: pass
            case 5: print("exiting");break
            case _: print("invalid option")

if __name__ == '__main__':main()