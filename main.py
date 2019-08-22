from src.person import Person

if __name__ == "__main__":
    input = "5 2 3 4 6"
    # input = "5 1"
    print (input)
    p = Person()
    items = input.split(" ")
    items = filter(None, items)

    for article in items:
        status, history = p.take_action(article)
        if not status:
            history.append('fail')
            break

    items_to_check = ["pants", "shirt", "shoes", "socks"]
    result = (all(i in history for i in items_to_check))
    if result:
        if "leave" not in history:
            history.append("leave")

    print (history)
