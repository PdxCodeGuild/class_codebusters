#----------------------------------------------------#
# *'-.-'*'-.-'(👍≖‿‿≖)👍 👍(≖‿‿≖👍)*'-.-'*'--'*#
# 
#          Project: Python make change bb
#          Version: 1.0
#          Author: Calen Ray
#          Email: Calen.w.ray@gmail.com
#          Date: 04/29/21
#----------------------------------------------------#

# step one, lets get some input up in here
while True:

    while True: # yes yes yes, I could handle errors with exceptions and warnings, or I could use a while loop for these small input errors

        total = input('*'*75 + '\nPlease supply an amount you would like to break into change. I.E. $59.52\n$')
        try:
            total = float(total)
        except:
            pass

        if type(total) == float:
            break
        else:
            print(f'Looks like {total} is not a valid option')


    #-----------------------------------------------------------------#

    # ok now that we have a functioning way of getting our data and confirmed its converted, lets proceed to processing it. 
    print(total)
    quarters = total//0.25
    total = round(total%0.25, 2)
    print(total)
    dime = total//0.10
    total = round(total%0.10, 2)
    print(total)
    nickel = total//0.05
    total = round(total%0.05, 2)
    print(total)
    penny = total//0.01
    total = round(total%0.01, 2)
    
    print(f'''You can have: 
    {quarters} quarters, 
    {dime} dimes, 
    {nickel} nickles
    {penny} one cent coins.''')