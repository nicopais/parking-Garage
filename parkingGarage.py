# Start Your Code here
class ParkingGarage():

    def __init__(self, available_tickets, available_parking_spaces):
        self.available_tickets = available_tickets
        self.available_parking_spaces = available_parking_spaces

    def is_Available(self):
        if self.available_tickets[0] > 0 and self.available_parking_spaces[0] > 0:
            return True
        else:
            return False
        
    def issue_tickets(self):
        if self.is_Available() == True:
            self.available_tickets[0] -= 1
            self.available_parking_spaces[0] -= 1
            print(self.available_tickets)
            print(self.available_parking_spaces)
            print("Ticket issued. Please proceed to park")
        else:
            print("Sorry, the ParkingGarage is currently full, please try again later.")
        
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
        self.available_tickets = [i + 1 for i in self.available_tickets]
        print(self.available_tickets)
        self.available_parking_spaces = [j + 1 for j in self.available_parking_spaces]
        print(self.available_parking_spaces)

    


new_ticket = ParkingGarage([100], [100])
print(new_ticket.is_Available())
print(new_ticket.issue_tickets())
print(new_ticket.pay_For_Parking())
print(new_ticket.leave_Garage())


