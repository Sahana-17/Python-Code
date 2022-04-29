# BRANCH SALES
# Created by : Sahana Muralikrishnan

sales_dict = dict()
cost_dict = dict()

def read_branch(branch_id):
    """reads the contents of branch file"""

    try:
        file_name = "sales_{}.csv".format(branch_id)
        with open(file_name) as f:
            file_branch = f.readline() #to remove title line
            while True:

                file_branch = f.readline()

                if not file_branch:
                    break
                fields = file_branch.strip().split(',')

                key = int(fields[0])
                sales_dict[key] = float(fields[1])
                cost_dict[key] = float(fields[2])

        f.close()
    except FileNotFoundError:
        print("Sorry, this file does not exist!")   
    
    except:
        print("Unknown error while opening file!")

    return sales_dict, cost_dict
        
def calculate_profit(sales_dict, cost_dict, start_date, end_date): 
    """calculates profit of branch over a range"""
    
    try:

        profit = 0
        for day in range(start_date, end_date+1):
            profit = profit+(sales_dict[day] - cost_dict[day])

        if profit < 0:
            raise ValueError
    except ValueError:
        print("Profit is Negative!!!")

    return profit

def minimum_sales(day_number): 
    """calculates which branch has minimum sales"""  
    
    min_sales_branch = 0
    value = [dict()] * 3
    min_sales = 99999999
    tmp = dict() #to store the cost values
    for i in range(1,4):
        value[i-1],tmp = read_branch(i)
            
        if min_sales > value[i-1][day_number]:
            min_sales = value[i-1][day_number]
            min_sales_branch = i

    print("Branch with minimum sales : ", min_sales_branch)
    print("Min sales : ", min_sales)    
        
    return min_sales

def main():

    branch_num = int(input("Enter the branch number : "))
    sales_dict, cost_dict = read_branch(branch_num)

    
    start_date = int(input("Enter start date : "))
    end_date = int(input("Enter end date : "))
    profit = calculate_profit(sales_dict, cost_dict, start_date, end_date)
    print("Profit is : ", profit)

    day_num = int(input("Enter the day number : "))
    min_sales = minimum_sales(day_num)
main()
