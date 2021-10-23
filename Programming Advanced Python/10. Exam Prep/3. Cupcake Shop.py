def stock_availability(inventory_list: list, delivery_or_sell: str, *args):
    if delivery_or_sell == "delivery":
        for item in args:
            inventory_list.append(item)
    elif delivery_or_sell == "sell":
        if len(args) == 0:
            del inventory_list[0]
        elif isinstance(args[0], int):
            n_of_items_to_remove = int(args[0])
            for _ in range(n_of_items_to_remove):
                del inventory_list[0]
        else:
            for item in args:
                while item in inventory_list:
                    inventory_list.remove(item)
    return inventory_list

