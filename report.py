allgroups = []

print("enter details for 5 groups:")

for i in range(1,6):
    print(f"\nEntering details for group {i}: ")
    groupname= input("Enter group name: ")
    groupsize= input("Enter group size: ")
    compdate=input("Enter date of the competetion (DD/MM/YYYY): ")
    venue=input("Enter venue: ")
    medaltype= input("Enter type of medal (gold/silver/bronze): ")
    grouprecord = (groupname, groupsize, compdate, venue, medaltype)
    allgroups.append(grouprecord)

print("------Displaying Competition Records------")

#loop through list to display each record
for record in allgroups:
    name, size, date, venue, medal = record
    print(f"\nGroup Name: {name}")
    print(f"Group Size: {size}")
    print(f"Competition Date: {date}")
    print(f"Venue: {venue}")
    print(f"Medal Won: {medal}")

    

