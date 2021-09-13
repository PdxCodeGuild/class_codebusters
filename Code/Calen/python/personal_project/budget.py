# the purpose here should be writing functions for later use in an attempt to make an online budgeting app

def conversion_validation(data: str, desired_type:type):
    """ (incoming string, desired data type) This function will server as a method of confirming the ability of user input to be converted to a specified datatype"""
    
    if desired_type not in [str, int, float, list]:
        # this will ultimatly return false if the datatype is invalid
        return False
    
    elif desired_type == float:
        try:
            data = float(data)
        except:
            return False
    
    elif desired_type == int:
        try:
            data = int(data)
        except:
            return False
    
    elif desired_type == str:
        try:
            data = str(data)
        except:
            return False
    
    elif desired_type == list:
        try:
            data = list(data)
        except:
            return False
        
    else:
        return False

    return data



def basic_info() -> dict:
    """ This function should return a dict of basic info """
    while True:
        # this will allow us to validate input
        income = input(f'Please provide your estimated income for the month. \nif you need help calculating your monthly income from an hourly rate type "hourly"').lower()

        if income not in ['help', 'hourly']:
            # using this to convert the income to a float if its not in need of hourly conversion
            income = conversion_validation(income,float)

            if not income:
                # using truthy falsy to check if the validation was successful:
                print(f'There was in issue with your input for income, please use only numbers and if needed a single decimal point.')
            else:
                break


        #-----------------------Hourly rate conversion------------------------#

        # this section is designated as a means of calculating monthly income by hourly rate for those unable to estimate.
        if income in ['help', 'hourly']:

            hourly_rate = input(f'Please input your hourly rate in this format: 12.50 / 17.45 ect. | ')
            hourly_rate = conversion_validation(hourly_rate, float)

            if not hourly_rate:
                    # this uses truthy/falsy style of data validation, we know the conversion function returns false on issue during conversion and will result in the below print.
                print(f'Your input of {hourly_rate} is not valid, please stick to numbers and decimals')


        if type(hourly_rate) == float or type(hourly_rate) == int:

                hours_worked = input(f'At your rate of {hourly_rate} roughly how many hours will you work this month? \n    | 40 hours a week is 160 hours a month: ')
                hours_worked = conversion_validation(hours_worked, float)
                
                if not hours_worked:
                    # this uses truthy/falsy style of data validation, we know the conversion function returns false on issue during conversion and will result in the below print.
                    print(f'There was in issue with your input of {hours_worked}, please try again with numbers and a single decimal only.')
                income = hourly_rate*hours_worked
                break
                
    #--------------------------------------------------------------------#
        

    # our current data is hours_worked, hourly rate, and income. 

    #-----------------Expenses---------------------------#

    expenses = {}
    while True:
        # this will allow us to loop through and accept new expenses as needed by user

        if input(f'Would you like to add a new expense to your budget? yes/no').lower() in ['no', 'n', 'no.']:
            # this serves as the break-out of our loop
            print(f'You have {len(expenses)} in your budget.')
            break

        key_data = input(f'What is your first expense? ') # key data
        value_date = input(f'What is the monthly cost of this expense? ') # value data

        if conversion_validation(value_date, float) == False:
            # using truthy to check on the float conversions validation
            print(f'There was an issue with your input for expense cost, please stick to numbers and a single decimal if needed.')
        
        else:
            expenses[len(expenses)] = {'expense': key_data, 'cost': float(value_date)}
        
    
    try: 
        return [income, hours_worked, hourly_rate, expenses]
    except:
        return [income, expenses]
    

basic_info = basic_info()

if len(basic_info) > 2:
    # this will allow us to unpack the basic info based on the amount of data returned by the basic info function. 
    income, hours_worked, hourly_rate, expenses = basic_info
else:
    income, expenses = basic_info



