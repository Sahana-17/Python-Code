def remove_duplicates(input_list):  
    
    set1 = set()
    length = len(input_list)

    for i in range(0,length):
        set1.add(input_list[i])

    return set1

def main():

    #input_list1 = [1, 1, 2]
    input_list1 = [0, 10, 1, 5, 8, 2, 2, 3, 1, 8]
    print("Input List : ", input_list1)
    value = remove_duplicates(input_list1)
    print("Output Set : " ,value)

main() 

