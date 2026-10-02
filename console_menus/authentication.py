# use py 3.10 or later
import time
def get_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password
def login():
    for i in range(3):
        user, pwd = get_credentials()
        return True if user == "user2026" and pwd == "2026Oxwl" else False
def loading():
    carga = ["loading.", "loading..", "loading..."]
    for j in range(2):
        for i in carga:
            print("\r" + i, end="", flush=True)
            time.sleep(0.5)
        print("\r" + " " * len(carga[-1]), end="")
    print()

def main():
    loading()
    print("Welcome to they system" if login() else "user or password incorrect")
if __name__ == '__main__': main()