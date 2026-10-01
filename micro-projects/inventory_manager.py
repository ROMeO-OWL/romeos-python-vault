# use py 3.10 or later
from datetime import *

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
    items = {} ; opt = 0
    while opt != 8:
        opt = get_typed_input(int, "Inventory\n1)add articles\n2)check low stock articles\n3)count sales\n4)show deposited quantities\n5)show cash payments\n6)group articles by month\n7)show all articles\n8)exit\n--> ")
        if opt is None: print("invalid data or no more attempts") ; return
        match opt:
            case 1:
                qty = get_typed_input(int, "how many articles to enter?:\n--> ")
                if not qty or qty <= 0: continue
                for i in range(qty):
                    print(f"Id article: {i + 1}")
                    item_num = get_typed_input(int, "Enter article number or Id:\n--> ")
                    if item_num in items: print("article Id already exists") ; continue
                    name = get_typed_input(str, "Enter article name:\n--> ")
                    name = name.title() if name else "unnamed"
                    price = get_typed_input(float, "Enter price:\n--> ")
                    val_price = price if (price and price > 0) else 0.0
                    min_qty = get_typed_input(int, "Enter minimum stock:\n--> ")
                    val_min = min_qty if min_qty is not None and min_qty >= 0 else 0
                    curr_qty = get_typed_input(int, "Enter current stock:\n--> ")
                    val_curr = curr_qty if curr_qty is not None and curr_qty >= 0 else 0
                    date_str = get_typed_input(str, "Enter sale date yyyy-mm-dd or mm:\n--> ")
                    date_val = date_str if date_str else "01"
                    dep_qty = get_typed_input(int, "Enter deposited quantity:\n--> ")
                    val_dep = dep_qty if dep_qty is not None and dep_qty >= 0 else 0
                    cash_pay = get_typed_input(float, "Enter cash payment:\n--> ")
                    val_cash = cash_pay if (cash_pay and cash_pay >= 0) else 0.0
                    items[item_num] = [name, val_price, val_min, val_curr, date_val, val_dep, val_cash]
            case 2:
                low_stock = [f"Id: {item_id} name: {data[0]} current: {data[3]} min: {data[2]}" for item_id, data in items.items() if data[3] < data[2]]
                if low_stock:
                    for item in low_stock: print(item)
                else: print("all articles have sufficient stock")
            case 3:
                nov_count = sum(1 for data in items.values() if (data[4].split('-')[1] if '-' in data[4] else data[4]) == '11')
                print(f"Articles sold in november: {nov_count}")
            case 4:
                if items:
                    for item_id, data in items.items(): print(f"Id: {item_id} name: {data[0]} deposited Qty: {data[5]}")
                else: print("no articles registered")
            case 5:
                if items:
                    for item_id, data in items.items(): print(f"Id: {item_id} name: {data[0]} cash payment: ${data[6]:.2f}")
                else: print("no articles registered")
            case 6:
                if not items: print("no articles registered") ; continue
                by_month = {}
                for item_id, data in items.items():
                    m = data[4].split('-')[1] if '-' in data[4] else data[4]
                    by_month.setdefault(m, []).append((item_id, data[0], data[4]))
                for m, art_list in by_month.items():
                    print(f"month: {m}")
                    for art in art_list: print(f"Id: {art[0]} name: {art[1]} sale date: {art[2]}")
            case 7:
                if items:
                    for item_id, data in items.items(): print(f"Id: {item_id} name: {data[0]} price: ${data[1]:.2f} stock: {data[3]}")
                else: print("no articles registered")
            case 8: print("exiting") ; break
            case _: print("invalid option")

if __name__ == '__main__': main()