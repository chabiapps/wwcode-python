""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

#can't subtract string

total_bill = int(input('How much is your total bill?'))
payment = int(input('How much is your payment?'))

change = payment - total_bill

print('Hi! Your change is {}'.format(change)) 
print(f'Hi! Your change is {change}') 