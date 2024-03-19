# Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, 
# issue description, and status (open/closed).
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Implement functions to:
# Open a new service ticket.

def open_ticket(service_tickets, ID, name, issue, status):
    service_tickets[ID] = {"Customer": name, "Issue": issue, "Status": status}

    
open_ticket(service_tickets, "ticket003", "kris", "bugs", "open")
print(service_tickets)
    
# Update the status of an existing ticket.
def change_status(service_tickets, ID, status):
    service_tickets[ID]["Status"] = status
    
change_status(service_tickets, "ticket003", "closed")
print(service_tickets)

# Display all tickets or filter by status.
def display_all(service_tickets):
    for ID in service_tickets:
        print(service_tickets[ID])
        
def display_filter(service_tickets, status):
    for ID in service_tickets:
        if service_tickets[ID]["Status"] == status:
            print(service_tickets[ID])
            
# display_all(service_tickets)
display_filter(service_tickets, "closed")
# Initialize with some sample tickets and include functionality for additional ticket entry.

