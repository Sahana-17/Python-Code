def fill_set(set1):
    try:

        while True:
            value = int(input("Enter an interger that is not -1 : "))
            if value == -1:
                break
            else:
                
                set1.add(value)
                
    except ValueError:
        print("Non-integer value!")

    return set1

def main():

    set1 = set()
    set_value = fill_set(set1)
    print(set_value)

main()
