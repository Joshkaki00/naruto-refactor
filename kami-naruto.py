# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

def send_alert():
    print("alert!")

def check_security(people):
    found = False
    for p in people:
        if not found:
            if p == "Naruto":
                send_alert()
                found = True

            if p == "Goku":
                send_alert()
                found = True


check_security(["Kami", "Naruto"])
