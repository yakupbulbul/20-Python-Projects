# collect the necessary inputs: principal, apr, years
# calculate the montly payment
# show the user 

def main(): 
    print(" This is a montly payment loan calculator ")
    print("")

    principal = float( input("Input the loan amount: "))
    apr = float( input("Input the anual interest rate: "))
    years = int( input("Input the amount of years: "))


    montly_interst_rate = apr / 1200
    amount_of_months = years * 12
    montly_payment = principal * montly_interst_rate / (1 - (1 + montly_interst_rate) ** (- amount_of_months))

    print( "The montly payment for this loan is : %.2f " % montly_payment)
   
main()