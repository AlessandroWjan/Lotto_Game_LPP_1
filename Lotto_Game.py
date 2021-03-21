import random
from prettytable import PrettyTable


class Bill:
    bill_types = ["AMBATA", "AMBO", "TERNO", "QUATERNA", "CINQUINA"]
    wheels = ["BARI ", "CAGLIARI", "FIRENZE", "GENOVA", "MILANO", "NAPOLI", "PALERMO", "ROMA", "TORINO", "VENEZIA"]
    numbers = list(range(1, 91))

    def __init__(self, bill_type, wheel, n_numbers):
        self.bill_type = bill_type
        self.n_numbers = n_numbers
        self.wheel = wheel

    def num_gen(self):
        num = random.sample(Bill.numbers, self.n_numbers)
        return num

    # Define a play control function <-- START -->
    def playchecked(self):
        if self.bill_type in Bill.bill_types and self.wheel in Bill.wheels and self.n_numbers <= 10:
            return True

        elif self.bill_type in Bill.bill_types and self.wheel not in Bill.wheels and self.n_numbers > 10:
            print(f'Warning: You have entered an invalid name of wheel ({self.wheel}). Try again!')
            print(f'Warning: {self.n_numbers} is an invalid amount of numbers to play (max 10). Try again!')
            return False

        elif self.bill_type in Bill.bill_types and self.wheel in Bill.wheels and self.n_numbers > 10:
            print(f'Warning: {self.n_numbers} is an invalid amount of numbers to play (max 10). Try again!')
            return False

        elif self.bill_type in Bill.bill_types and self.wheel not in Bill.wheels and self.n_numbers <= 10:
            print(f'Warning: You have entered an invalid name of wheel ({self.wheel}). Try again!')
            return False

        elif self.bill_type not in Bill.bill_types and self.wheel in Bill.wheels and self.n_numbers > 10:
            print(f'Warning: You have entered an invalid type of bill ({self.bill_type}). Try again!')
            print(f'Warning: {self.n_numbers} is an invalid amount of numbers to play (max 10). Try again!')
            return False

        elif self.bill_type not in Bill.bill_types and self.wheel not in Bill.wheels and self.n_numbers <= 10:
            print(f'Warning: You have entered an invalid type of bill ({self.bill_type}). Try again!')
            print(f'Warning: You have entered an invalid name of wheel ({self.wheel}). Try again!')
            return False

        elif self.bill_type not in Bill.bill_types and self.wheel in Bill.wheels and self.n_numbers <= 10:
            print(f'Warning: You have entered an invalid type of bill ({self.bill_type}). Try again!')
            return False
    # Define a play control function <-- END -->


# Define the main function of the game <-- START -->
def play_lotto():
    while True:  # Create a loop statement to be able to restart the game without exiting or before this happens

        n_play = int(input('Welcome to "Lotto Game". Enter the number of bills from 1 to 5 (0 [zero] to exit) --> '))

        if n_play == 0:
            print("Thank you to played.")
        elif n_play == 1:
            bill_type_1 = input("Insert the type of bill --> ").upper()
            wheel_1 = input("Insert the wheel to play on --> ").upper()
            n_numbers_1 = int(input("Insert the amount of numbers to play (max 10) --> "))
            play_1 = Bill(bill_type_1, wheel_1, n_numbers_1)
            if play_1.playchecked():
                ticket = PrettyTable()  # Use the PrettyTable module to get a good output
                ticket.field_names = ["N. Play", "Wheel", "Play Type", "Played Numbers"]
                ticket.add_row([1, play_1.wheel, play_1.bill_type, play_1.num_gen()])
                print(ticket)
            else:
                continue
        elif n_play == 2:
            bill_type_1 = input("Insert the first type of bill --> ").upper()
            wheel_1 = input("Insert the first wheel to play on --> ").upper()
            n_numbers_1 = int(input("Insert the first amount of numbers to play (max 10) --> "))
            play_1 = Bill(bill_type_1, wheel_1, n_numbers_1)
            if play_1.playchecked():
                bill_type_2 = input("Insert the second type of bill --> ").upper()
                wheel_2 = input("Insert the second wheel to play on --> ").upper()
                n_numbers_2 = int(input("Insert the second amount of numbers to play (max 10) --> "))
                play_2 = Bill(bill_type_2, wheel_2, n_numbers_2)
                if play_2.playchecked():
                    ticket = PrettyTable()
                    ticket.field_names = ["N. Play", "Wheel", "Play Type", "Played Numbers"]
                    ticket.add_row([1, play_1.wheel, play_1.bill_type, play_1.num_gen()])
                    ticket.add_row([2, play_2.wheel, play_2.bill_type, play_2.num_gen()])
                    print(ticket)
                else:
                    continue
            else:
                continue
        elif n_play == 3:
            bill_type_1 = input("Insert the first type of bill --> ").upper()
            wheel_1 = input("Insert the first wheel to play on --> ").upper()
            n_numbers_1 = int(input("Insert the first amount of numbers to play (max 10) --> "))
            play_1 = Bill(bill_type_1, wheel_1, n_numbers_1)
            if play_1.playchecked():
                bill_type_2 = input("Insert the second type of bill --> ").upper()
                wheel_2 = input("Insert the second wheel to play on --> ").upper()
                n_numbers_2 = int(input("Insert the second amount of numbers to play (max 10) --> "))
                play_2 = Bill(bill_type_2, wheel_2, n_numbers_2)
                if play_2.playchecked():
                    bill_type_3 = input("Insert the third type of bill --> ").upper()
                    wheel_3 = input("Insert the third wheel to play on --> ").upper()
                    n_numbers_3 = int(input("Insert the third amount of numbers to play (max 10) --> "))
                    play_3 = Bill(bill_type_3, wheel_3, n_numbers_3)
                    if play_3.playchecked():
                        ticket = PrettyTable()
                        ticket.field_names = ["N. Play", "Wheel", "Play Type", "Played Numbers"]
                        ticket.add_row([1, play_1.wheel, play_1.bill_type, play_1.num_gen()])
                        ticket.add_row([2, play_2.wheel, play_2.bill_type, play_2.num_gen()])
                        ticket.add_row([3, play_3.wheel, play_3.bill_type, play_3.num_gen()])
                        print(ticket)
                    else:
                        continue
                else:
                    continue
            else:
                continue
        elif n_play == 4:
            bill_type_1 = input("Insert the first type of bill --> ").upper()
            wheel_1 = input("Insert the first wheel to play on --> ").upper()
            n_numbers_1 = int(input("Insert the first amount of numbers to play (max 10) --> "))
            play_1 = Bill(bill_type_1, wheel_1, n_numbers_1)
            if play_1.playchecked():
                bill_type_2 = input("Insert the second type of bill --> ").upper()
                wheel_2 = input("Insert the second wheel to play on --> ").upper()
                n_numbers_2 = int(input("Insert the second amount of numbers to play (max 10) --> "))
                play_2 = Bill(bill_type_2, wheel_2, n_numbers_2)
                if play_2.playchecked():
                    bill_type_3 = input("Insert the third type of bill --> ").upper()
                    wheel_3 = input("Insert the third wheel to play on --> ").upper()
                    n_numbers_3 = int(input("Insert the third amount of numbers to play (max 10) --> "))
                    play_3 = Bill(bill_type_3, wheel_3, n_numbers_3)
                    if play_3.playchecked():
                        bill_type_4 = input("Insert the fourth type of bill --> ").upper()
                        wheel_4 = input("Insert the fourth wheel to play on --> ").upper()
                        n_numbers_4 = int(input("Insert the fourth amount of numbers to play (max 10) --> "))
                        play_4 = Bill(bill_type_4, wheel_4, n_numbers_4)
                        if play_4.playchecked():
                            ticket = PrettyTable()
                            ticket.field_names = ["N. Play", "Wheel", "Play Type", "Played Numbers"]
                            ticket.add_row([1, play_1.wheel, play_1.bill_type, play_1.num_gen()])
                            ticket.add_row([2, play_2.wheel, play_2.bill_type, play_2.num_gen()])
                            ticket.add_row([3, play_3.wheel, play_3.bill_type, play_3.num_gen()])
                            ticket.add_row([4, play_4.wheel, play_4.bill_type, play_4.num_gen()])
                            print(ticket)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        elif n_play == 5:
            bill_type_1 = input("Insert the first type of bill --> ").upper()
            wheel_1 = input("Insert the first wheel to play on --> ").upper()
            n_numbers_1 = int(input("Insert the first amount of numbers to play (max 10) --> "))
            play_1 = Bill(bill_type_1, wheel_1, n_numbers_1)
            if play_1.playchecked():
                bill_type_2 = input("Insert the second type of bill --> ").upper()
                wheel_2 = input("Insert the second wheel to play on --> ").upper()
                n_numbers_2 = int(input("Insert the second amount of numbers to play (max 10) --> "))
                play_2 = Bill(bill_type_2, wheel_2, n_numbers_2)
                if play_2.playchecked():
                    bill_type_3 = input("Insert the third type of bill --> ").upper()
                    wheel_3 = input("Insert the third wheel to play on --> ").upper()
                    n_numbers_3 = int(input("Insert the third amount of numbers to play (max 10) --> "))
                    play_3 = Bill(bill_type_3, wheel_3, n_numbers_3)
                    if play_3.playchecked():
                        bill_type_4 = input("Insert the fourth type of bill --> ").upper()
                        wheel_4 = input("Insert the fourth wheel to play on --> ").upper()
                        n_numbers_4 = int(input("Insert the fourth amount of numbers to play (max 10) --> "))
                        play_4 = Bill(bill_type_4, wheel_4, n_numbers_4)
                        if play_4.playchecked():
                            bill_type_5 = input("Insert the fifth type of bill --> ").upper()
                            wheel_5 = input("Insert the fifth wheel to play on --> ").upper()
                            n_numbers_5 = int(input("Insert the fifth amount of numbers to play (max 10) --> "))
                            play_5 = Bill(bill_type_5, wheel_5, n_numbers_5)
                            if play_5.playchecked():
                                ticket = PrettyTable()
                                ticket.field_names = ["N. Play", "Wheel", "Play Type", "Played Numbers"]
                                ticket.add_row([1, play_1.wheel, play_1.bill_type, play_1.num_gen()])
                                ticket.add_row([2, play_2.wheel, play_2.bill_type, play_2.num_gen()])
                                ticket.add_row([3, play_3.wheel, play_3.bill_type, play_3.num_gen()])
                                ticket.add_row([4, play_4.wheel, play_4.bill_type, play_4.num_gen()])
                                ticket.add_row([5, play_5.wheel, play_5.bill_type, play_5.num_gen()])
                                print(ticket)
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue

        # Create a loop statement choices <-- START -->
        loop = input("Do you want to play again? Y/N --> ")

        if loop == "y" or loop == "Y":
            continue
        elif loop == "n" or loop == "N":
            print("Thank you and goodbye")
            break
        else:
            print("You have entered an invalid option. I exit the program. See you soon!!")
            break
        # Create a loop statement choices <-- END -->

# Define the main function of the game <-- END -->


if __name__ == '__main__':
    play_lotto()
