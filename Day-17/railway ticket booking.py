while True:
                    
          ticket=10000
          gender=input(''' 1.male(m)
                             
                           2.female(f)
                           3.exit(e)''')
          age=int(input('age:'))
          if gender=='m':
                    if age>60:
                              print('price: ',ticket-ticket*0.3)
                    else:
                              print('price: ',ticket)
          if gender=='f':
                    if age>60:
                              print('price: ',ticket-ticket*0.5)
                    else:
                              print('price: ',ticket-ticket*0.3)
          if gender=='e':
                    break
                    
          
