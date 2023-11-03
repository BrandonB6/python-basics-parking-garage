class Pg():
    def __init__(self,ticket, parkingSpaces, currentTicket):
        self.ticket = ticket
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
    
    def takeTicket(self):
        print (self.parkingSpaces)
        if self.parkingSpaces == []:
            print("Unfortunately, curently there are no open spaces.")
        response = input("What space would you like? ")
        response2 = response.lower()
        if response2 in self.parkingSpaces:
            self.parkingSpaces.remove(response2)
            self.ticket.append(response2)
            print(f'You selected the space {response2}. Here is your ticket.')
            self.currentTicket[response2]['Paid'] = False
            print(self.parkingSpaces)
            print(self.ticket)
            print(self.currentTicket)
        elif response2 not in self.parkingSpaces: 
            print('Your selection is unavailable. Please select a different space.')


    def payForParking(self):
        price = 10
        response_pay = input("What was your parking space? ")

        while price > 0:
            response_pay1 = int(input('Your payment is $' + str(price) + ' , how much would you like to pay? '))
            if response_pay1 < price:
                print('Your remaining balance is' + str(price-response_pay1 + ' '))
                price -= response_pay1
            elif response_pay1 == price:
                self.currentTicket[response_pay]['Paid'] = True
                self.parkingSpaces.append(response_pay)
                self.ticket.remove(response_pay)
                print(sorted(self.parkingSpaces))
                print(sorted(self.ticket))
                print(self.currentTicket)
                self.leaveGarage()
                break
    def leaveGarage(Self):
        print("Thank You, have a nice day, you have 15 minutes to exit")

garage = Pg([],sorted(['a1', 'b2', 'c3', 'd4', 'e5']),{'a1' : {"Paid" : True},'b2' : {"Paid" : True}, 'c3' : {"Paid" : True}, 'd4' : {"Paid" : True}, 'e5' : {"Paid" : True},})


def Run():
    while True:
        response1 = input('Would you like a ticket or pay for a space, or quit? ')
        if response1.lower() == 'pay for a space':
            garage.payForParking()
        elif response1.lower() == 'ticket':
            garage.takeTicket()
        elif response1.lower() == 'quit':
            break

Run()



    
                

                                
    

            
        


