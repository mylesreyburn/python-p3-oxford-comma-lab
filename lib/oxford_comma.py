def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:  
        items[-1] = f"and {items[-1]}"

        joined_items = ", ".join(items)
        return joined_items

print("one element: " + oxford_comma(["Malians"]))

print("four elements: " + oxford_comma(["Teutons", "Aztecs", "Hindustani", "Spanish"]))
