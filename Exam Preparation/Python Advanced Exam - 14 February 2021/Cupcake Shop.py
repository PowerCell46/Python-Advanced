def stock_availability(inventory_list, delivery_sell, *args):
    if delivery_sell == "delivery":
        for item in args:
            inventory_list.append(item)
        return inventory_list

    elif delivery_sell == "sell":
        if len(args) == 0:
            inventory_list.pop(0)
            return inventory_list

        else:
            args = list(str(args))
            args.pop()
            args.pop()
            args.pop(0)
            while "'" in args:
                search_index = args.index("'")
                args.pop(search_index)
            args = "".join(args)
            try:
                remove_count = int(args)
                while remove_count > 0:
                    inventory_list.pop(0)
                    remove_count -= 1
            except:
                remove_elements = args.split(", ")
                for remove_element in remove_elements:
                    while remove_element in inventory_list:
                        search_index = inventory_list.index(remove_element)
                        inventory_list.pop(search_index)
            finally:
                return inventory_list
