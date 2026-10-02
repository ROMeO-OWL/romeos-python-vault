# use py 3.10 or late
class ReservationNode:
    def __init__(self, client_name,table, time,guests):
        self.client_name =client_name
        self.table =table
        self.time= time
        self.guests= guests
        self.next= None

class ReservationList:
    def __init__(self):self.head =None
    def add_reservation(self, client_name, table,time, guests):
        new_node = ReservationNode(client_name, table, time, guests)
        if self.head is None: self.head = new_node
        else:
            current = self.head
            while current.next is not None: current = current.next
            current.next = new_node
        print(f"reservation for {client_name} added.")

    def delete_reservation(self,client_name):
        if self.head is None: 
            print("no reservations to delete.")
            return

        if self.head.client_name == client_name:
            self.head = self.head.next
            print(f"reservation for {client_name} deleted.")
            return

        current= self.head
        while current.next is not None and current.next.client_name != client_name: current = current.next

        if current.next is not None:
            current.next =current.next.next
            print(f"reservation for {client_name} deleted.")
        else: print(f"no reservation found for {client_name}.")

    def update_reservation(self, client_name,new_table,new_time, new_guests):
        node = self.search_reservation(client_name)
        if node:
            node.table =new_table
            node.time= new_time
            node.guests =new_guests
            print(f"reservation for {client_name} updated.")
        else: print(f"no reservation found for {client_name}.")

    def search_reservation(self, client_name):
        current = self.head
        while current is not None:
            if current.client_name == client_name: return current
            current = current.next
        return None

    def show_reservations(self):
        current = self.head
        if current is None:
            print("no reservations.")
            return

        while current is not None:
            print(
                f"client: {current.client_name}, table: {current.table}, "
                f"time: {current.time}, guests: {current.guests}"
            )
            current =current.next

def main():
    reservations = ReservationList()
    while True:
        print("\n1)add reservation")
        print("2)delete reservation")
        print("3)update reservation")
        print("4)search reservation")
        print("5)show all reservations")
        print("6)exit")
        option = input("Select an option:\n--> ")
        match option:
            case "1":
                name = input("Client name: ")
                table = int(input("Table number: "))
                time = input("Time (HH:MM): ")
                guests = int(input("Number of guests: "))
                reservations.add_reservation(name, table, time, guests)
            case "2":
                name = input("Client name to delete: ")
                reservations.delete_reservation(name)
            case "3":
                name = input("Client name to update: ")
                table = int(input("New table number: "))
                time = input("New time: ")
                guests = int(input("New number of guests: "))
                reservations.update_reservation(name, table, time, guests)

            case "4":
                name = input("Client name: ")
                result = reservations.search_reservation(name)
                if result:
                    print(
                        f"reservation found: client: {result.client_name}, "
                        f"table: {result.table}, time: {result.time}, guests {result.guests}"
                    )
                else:print(f"no reservation found for {name}.")
            case "5":reservations.show_reservations()
            case "6": print("exiting..") ; break
            case _:print("invalid option.")

if __name__ == "__main__": main()