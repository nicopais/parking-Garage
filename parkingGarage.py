# Start Your Code here
class ParkingGarage():
    def __init__(self, total_tickets, total_parking_spaces, available_tickets, available_parking_spaces):
        self.total_tickets = total_tickets
        self.total_parking_spaces = total_parking_spaces
        self.available_tickets = available_tickets
        self.available_parking_spaces = available_parking_spaces

    def is_Available(self):
        if self.available_tickets > 0 and self.available_parking_spaces > 0:
            return True
        else:
            return False
        
    def issue_tickets(self):
        if self.is_available():
            self.available_tickets -= 1
            self.available_parking_spaces -= 1
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
        self.ticketamount = [i + 1 for i in self.ticketamount]
        print(self.ticketamount)
        self.parkingspace = [j + 1 for j in self.parkingspace]
        print(self.parkingspace)

    

new_ticket = ParkingGarage()
print(new_ticket.isAvaliable())
print(new_ticket.pay_For_Parking())
print(new_ticket.leave_Garage())


