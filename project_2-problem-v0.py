MIN_READING = 0
MAX_READING = 999999999

RESIDENTIAL_BASIC = 5.00
RESIDENTIAL_PER_GALLON = 0.0005


COMMERCIAL_BASIC =1000.00 
COMMERCIAL_CUTOFF = 4000000
COMMERCIAL_PER_GALLON = 0.00025


INDUSTRIAL_BASIC_1 = 1000.00 
INDUSTRIAL_CUTOFF_1 = 4000000
INDUSTRIAL_BASIC_2 = 2000.00 
INDUSTRIAL_CUTOFF_2 = 10000000
INDUSTRIAL_PER_GALLON = 0.00025 

customer_code = str(input('Enter customer code (R, C, or I):'))
used_gallons = 0 
to_bill = 0

#CUSTOMER CODE R
if customer_code == 'R':
    start_reading = int(input('Enter beginning reading (between 0 and 999999999):'))
    end_reading = int(input('Enter ending reading (between 0 and 999999999):'))

    #turning into gallons
    start_reading_gallons = start_reading/10
    end_reading_gallons = end_reading/10
    
    if (0<= start_reading <= 999999999) and ((0<= end_reading <= 999999999)):
        
        used_gallons =(end_reading_gallons) - (start_reading_gallons)

        to_bill =  RESIDENTIAL_BASIC + (RESIDENTIAL_PER_GALLON * used_gallons)
        
    else:
         print(' Invalid input (beginning or ending reading value is out of the range)' )


#CUSTOMER CODE C
elif customer_code == 'C':
    start_reading = int(input('Enter beginning reading (between 0 and 999999999):'))
    end_reading = int(input('Enter ending reading (between 0 and 999999999):'))

    #turning into gallons
    start_reading_gallons = start_reading/10
    end_reading_gallons = end_reading/10
    
    if (0<= start_reading <= 999999999) and ((0<= end_reading <= 999999999)):

        used_gallons =(end_reading_gallons) - (start_reading_gallons)


        if used_gallons > COMMERCIAL_CUTOFF:

            to_bill = 1000 + (used_gallons-COMMERCIAL_CUTOFF)*COMMERCIAL_PER_GALLON

        elif used_gallons <= COMMERCIAL_CUTOFF:

            to_bill = 1000

    else:
         print(' Invalid input (beginning or ending reading value is out of the range)' )


#CUSTOMER CODE I
elif customer_code == 'I':
    start_reading = int(input('Enter beginning reading (between 0 and 999999999):'))
    end_reading = int(input('Enter ending reading (between 0 and 999999999):'))

    #turning into gallons
    start_reading_gallons = start_reading/10
    end_reading_gallons = end_reading/10
    
    if (0<= start_reading <= 999999999) and ((0<= end_reading <= 999999999)):

        used_gallons =(end_reading_gallons) - (start_reading_gallons)


        if used_gallons < 4000000:

            to_bill = INDUSTRIAL_BASIC_1 #1000

        elif  INDUSTRIAL_CUTOFF_1 < used_gallons < INDUSTRIAL_CUTOFF_2: #4mil < user_gallons < 10mil

            to_bill = INDUSTRIAL_BASIC_2 #2000

        else:
            to_bill = INDUSTRIAL_BASIC_2 + (used_gallons - INDUSTRIAL_CUTOFF_2) * INDUSTRIAL_PER_GALLON
    
    else:
        print(' Invalid input (beginning or ending reading value is out of the range)' )

else:
    print('Invalid input (customer code)')

print(f'Customer code: {customer_code}')
print('Beginning reading value in gallons and tenths of gallon', start_reading_gallons)
print('Ending reading value in gallons and tenths of gallon', end_reading_gallons)
print(f'Gallons of water used: {used_gallons:0.1f}')
print(f'Amount billed ${to_bill:0.2f}')


