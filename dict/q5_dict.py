
def fill_dict():
    name_age = {}

    name_age = {'Sahana' : 18, 'Achu' : 9, 'Menaka' : 40, 'Murali' : 50, 'Sneha' : 19}


    return name_age

def highest_age(name_age): 

    key = []
    value = []
    fields = name_age.items()
    for i in fields:
        key.append(i[0]), value.append(i[1])
  
    print ("keys : ", str(key))
    print ("values : ", str(value))

    highest = 0
    for j in range(0,5):
        if value[j] > highest:
            highest = value[j]
            name = key[j]

    return highest, name
    
        


def main():

    dict = fill_dict()
    print(dict)

    highest, name = highest_age(dict)

    print("The oldest person is :", name)
    print("Their age is : ", highest)

main()