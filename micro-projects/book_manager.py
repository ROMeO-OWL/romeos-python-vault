# use py 3.10 or later
def get_typed_input(data_type, prompt='', error_msg="invalid input"):
    for _ in range(3):
        try:
            val = input(prompt)
            if data_type == str:
                if val.strip(): return val
                print("the text cannot be empty") ; continue
            return data_type(val)
        except ValueError: print(error_msg)
    return None

def main():
    books = {} ; opt = 0
    while opt != 6:
        opt = get_typed_input(int, "1) Add a book\n2) Show book titles\n3) Search book by ID\n4) Borrow a book\n5) Check if book is borrowed\n6) Exit\n--> ")
        if opt is None: print("invalid data or no more attempts") ; return
        match opt:
            case 1:
                b_id = get_typed_input(int, "Enter ID:\n--> ")
                if b_id in books: print("book ID already exists") ; continue
                author = get_typed_input(str, "Enter author:\n--> ")
                author = author.title() if author else "unknown"
                title = get_typed_input(str, "Enter title:\n--> ")
                title = title.title() if title else "untitled"
                pages = get_typed_input(int, "Enter pages:\n--> ")
                b_type = get_typed_input(str, "Enter type:\n--> ")
                b_type = b_type.lower() if b_type else "general"
                books[b_id] = [author, title, pages, b_type, False]
            case 2:
                if books:
                    for b_id, b_data in books.items(): print(f"ID: {b_id} | Title: {b_data[1]}")
                else: print("no books registered")
            case 3:
                b_id = get_typed_input(int, "Enter book ID:\n--> ")
                if b_id in books: b = books[b_id] ; print(f"Author: {b[0]}\nTitle: {b[1]}\nPages: {b[2]}\nType: {b[3]}\nBorrowed: {'Yes' if b[4] else 'No'}")
                else: print("book not found")
            case 4:
                b_id = get_typed_input(int, "Enter book ID to borrow:\n--> ")
                if b_id in books:
                    if not books[b_id][4]:
                        books[b_id][4] = True
                        print(f"The book '{books[b_id][1]}' has been borrowed")
                    else: print(f"The book '{books[b_id][1]}' was already borrowed")
                else: print("book not found")
            case 5:
                b_id = get_typed_input(int, "Enter book ID:\n--> ")
                if b_id in books: print(f"The book '{books[b_id][1]}' {'was borrowed' if books[b_id][4] else 'has not been borrowed'}")
                else: print("book not found")
            case 6: print("exiting") ; break
            case _: print("invalid option")

if __name__ == '__main__': main()