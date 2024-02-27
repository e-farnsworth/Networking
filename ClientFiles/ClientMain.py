import socket

from ClientView import ClientView

# Create a socket object 
client_s = socket.socket()
 
# Define the port on which you want to connect 
port = 51362
 
# connect to the server on local computer 
client_s.connect(('127.0.0.1', port))


response = client_s.recv(1024)



client_view = ClientView
class ClientMain():
    def logging_on():
        logged_on = False
        while logged_on == False:
            print('If you already have an account, type "Y". If not, type "N".')
            choice = input('Do you have an account? ')
            if choice == 'Y': # If the user has an account
                client_s.send(str.encode('False'))
                username = input('Username: ')
                password = input('Password: ')
                client_s.send(str.encode(username))
                verification = client_s.recv(1024)
                # resopnse = str boolean
                if verification == 'False':
                    print('Username not valid')
                else:
                    client_s.send(str.encode(password))
                    verification = client_s.recv(1024)

                    if verification == 'False':
                        print('Password not valid')
                    else: 
                        print(f'Welcome {username}')
                        logged_on = True
                        return

            elif choice == 'N': # if the user does not have an account
                client_s.send(str.encode('True'))
                username = input('Username: ')
                password = input('Password: ')
                client_s.send(str.encode(username))
                verification = client_s.recv(1024)
                verification = verification.decode()
                # verification will be a str bool
                if verification == 'False': # if false on server end, save username and password
                    # send client [1]
                    client_s.send(str.encode(password))
                    logged_on = True
                    return
                else:
                    print('That username is already being used')
            elif choice == 'exit':
                client_s.send(str.encode(choice))
                return 'exit'
            else:
                print('\nIf you would like to exit, type "exit".\n')

    def program_user():
        while choice != '3': # attempt, might need to add an elif choice == '3'
            print('What would you like to do?')
            print('1. Send a message')
            print('2. View messages')
            print('3. Logout')
            choice = input('Enter Index: ')
            client_s.send(str.encode(choice))
            if choice == '1': # send a message
                message = client_view.set_send_message
                client_s.send(str.encode(message))
                verification = client_s.recv(1024)
                verification = verification.decode
                print(verification)
            elif choice == '2': # view messages
                length = client_s.recv(1024)
                length = length.decode
                if length == '0':
                    print('No New Messages')
                else:
                    for i in range(int(length)):
                        messages_list = []
                        message = client_s.recv(1024)
                        messages_list.append(message)
                    # client_view.recieve_messages(messages_list)
                    for item in messages_list: # item is currently the message packet
                        message_list = item.split('|') # list is [sent_to, message, sender]
                        print(f'{message_list[2]}\n{message_list[1]}')
                        # Having problems with getting the other class to fully cooperate
                        # message.set_sender(message_list)
                        # message.set_message(message_list)
                        # message.display_message_full
            elif choice == '3': # don't raise an "error" message
                pass
            else:
                print('Choice is not in range')

def main():
    client = ClientMain
    while True:
        continue_ = client.logging_on()
        if continue_ != 'exit': # if it isn't anything
            client.program_user()
            break

main()

# close the connection 
client_s.close() 