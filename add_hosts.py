input_file = 'input.txt'
output_file = 'output.txt'
group_name = "Add_group_name_here"  
ticket_ref = "Add_ticket_ref_here"

# Read the IP addresses from the input file
with open(input_file, 'r') as file:
    ip_addresses = [line.strip() for line in file if line.strip()]

# Open the file to write the formatted lines
with open(output_file, 'w') as file:
    for i, ip in enumerate(ip_addresses):
        line = f'add host name "host_{ip}" ip-address "{ip}" comments "Ticket:{ticket_ref}" groups.1 "{group_name}"'
        file.write(line + '\n')

print("Output written to output.txt")
