from user import User

user_artur = User('Artur')
user_ann = User('Ann')

loging = input('Please enter login: ')
password = input('Please enter password: ')

task = input('Please enter your task: ')
user_artur.create_ticket(task)
ticket_obj = user_artur.get_user_tickets().pop()

user_artur.assign_ticket(ticket_obj, user_ann, 2020, 6, 20)

print(user_ann.get_user_assigned_tickets())


