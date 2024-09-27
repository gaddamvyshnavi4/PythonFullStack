
while True:
          marks=int(input())
          
          if marks in range(90,101):
                    print('grade A')

          elif marks in range(81,91):
                    print('grade B')
          elif marks in range(71,81):
                    print('grade C')
          elif marks in range(50,71):
                    print('D')
          elif marks in range(0,51):
                    print('fail! study well')
          
          
                    

break  continue pass
a=9
while a>2:
          a-=1
          if a==3:
               break
          
          if a==6:
                    continue
          
          print(a)


for i in 'va':
          if i=='a':
                    pass
          print('ok')

for i in 'va':
          if i=='a':
                    pass
          else:
                    print('ok')





'''ATM application building'''
card_name=input('Insert the card \t')
balance=10000
pwd=1234
if card_name=='c':
          print('welcome Vyshnavi')
if int(input('Enter the password'))==1234:
          while True:
                    number=int(input('''choose the option:
                                        1.Balance Enquiry
                                        2.Withdraw
                                        3.exit
                                        '''))
                    if number==1:
                              print('The current account balance is ',balance)
                    elif number==2:
                              withdraw=int(input('Enter the amount'))
                              if withdraw<balance:
                                        balance-=withdraw
                                        print('Your remaining account balance is',balance)
                              else:
                                        print('Balance is not sufficient')
                    elif number==3:
                              print('Thank you for visiting')
                              break
                    else:
                              print('Choose the correct query')
                              



a=10
while a>1:
          print(a)
          a=a-1
##          if a==5:
##                    break
else:
          print('while else loop')
