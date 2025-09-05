'''Problem Statement
You are asked to design a Flight Management System in Python using exception handling.
 
The system should:
- Read flight information from a file called flights.txt.
- Each line has: flight_number available_seats price_per_ticket
  Example: AI101 50 6000
 
Ask the user for:
- Flight number
- Number of tickets to book
 
Implement the following exception rules: (Questions below)
 
(a) Raise FlightNotFoundError (custom) if the entered flight number does not exist.
 
(b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats.
 
(c) Handle ValueError if user enters invalid input (like string instead of integer).
 
(d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket).
 
(e) Always close the file using finally.
 
The program should print:
- Flight details
- Total booking cost
- Discount per ticket (total / tickets)
 
Note**:
Use nested try-except:
 
Inner block for booking operations.
 
Outer block for file handling & re-raised exceptions'''

class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass

def flight_booking_system():
    try:
        with open("/home/nabakumr/Documents/python_training/assignments/day5thSept/flights.txt", "r") as f:
            flights = {}
            for line in f:
                fn, seats, price = line.strip().split()
                flights[fn] = {"seats": int(seats), "price": float(price)}

        try:
            fn = input("Enter Flight Number: ").strip()
            tickets = int(input("Enter number of tickets: "))

            if fn not in flights:
                raise FlightNotFoundError(f"Flight {fn} not found!")

            flight = flights[fn]

            if tickets > flight["seats"]:
                raise SeatsUnavailableError(f"Only {flight['seats']} seats available!")

            total = tickets * flight["price"]
            discount_per_ticket = total / tickets

            flights[fn]["seats"] -= tickets
            print()
            print("Booking Successful!")
            print(f"Flight: {fn}")
            print(f"Tickets Booked: {tickets}")
            print(f"Remaining Seats: {flights[fn]['seats']}")
            print(f"Total Cost: {total}")
            print(f"Discount per Ticket: {discount_per_ticket}")

            with open("/home/nabakumr/Documents/python_training/assignments/day5thSept/flights.txt", "w") as fw:
                for fno, details in flights.items():
                    fw.write(f"{fno} {details['seats']} {details['price']}\n")

        except FlightNotFoundError as e:
            print("error", e)
        except SeatsUnavailableError as e:
            print("error", e)
        except ValueError:
            print("error Please enter a valid number for tickets.")
        except ZeroDivisionError:
            print("error You entered 0 tickets, cannot calculate discount.")
        except Exception as e:
            print("error Unexpected error:", e)

    except FileNotFoundError:
        print("flights.txt not found!")

flight_booking_system()
