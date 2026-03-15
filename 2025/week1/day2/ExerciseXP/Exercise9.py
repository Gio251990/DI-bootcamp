ticket_price_children = 0
ticket_price_young = 10
ticket_price_senior = 15

senior = []
young = []
children = []

client_age = int(input("How old are you? Write -1 when you are done "))

while client_age != -1:

    if client_age <3:
        children.append(client_age)
        print(f"Cinema's tickets are free for children aged {client_age} years old")

    elif client_age >=3 and client_age <12:
        young.append(client_age)
        print(f"Children aged between 3 and 12 pay ${ticket_price_young}")

    else:
        print(f"Clients over the age of 12 pay ${ticket_price_senior}")
        senior.append(client_age)

    client_age = int(input("How old are you? Write -1 when you are done "))

total_price = (len(senior)*ticket_price_senior) + (len(young)*ticket_price_young)
print(f"Total cost: ${total_price}")

 




