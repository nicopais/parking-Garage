# Start Your Code here
class ParkingGarage():
    def __init__(self, tickets, spaces):
        self.ticketamount = tickets
        self.parkingspace = spaces
        self.currentTicket = {}

    def isAvaliable(self):
        for i in range(len(self.ticketamount)):
            self.ticketamount[i] = self.ticketamount[i] - 1
            print(self.ticketamount)
        for j in range(len(self.parkingspace)):
            self.parkingspace[j] = self.parkingspace[j] - 1
            print(self.parkingspace)
        
    def pay_For_Parking(self):
        self.currentTicket = {
            'Paid': 'False'
        }
        paid = input('Please enter your payment')
        if paid != '':
            self.currentTicket['Paid'] = 'True'
            print('Your ticket has been paid, you now have 15 minutes to leave.')

    def leave_Garage(self):
        for value in self.currentTicket.values():
            if value == 'True':
                print('Thank you, have a nice day')
            elif value == 'False':
                paid1 = input('Please enter your payment here!')
                if paid1 != '':
                    print("Thank you, have a nice day!")
        self.ticketamount = [i + 1 for i in self.ticketamount]
        print(self.ticketamount)
        self.parkingspace = [j + 1 for j in self.parkingspace]
        print(self.parkingspace)

    

new_ticket = ParkingGarage([100], [100])
print(new_ticket.isAvaliable())
print(new_ticket.pay_For_Parking())
print(new_ticket.leave_Garage())


