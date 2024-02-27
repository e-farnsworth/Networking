''' 
This is what the client will see when using the program 
This will eventually be converted to use a GUI

Things I want
    Client Autorization (log in and regester)
    send a message (who it is being sent to and what the message is)

Work on
    prepping message for being sent
        [sent_to, message, from]
'''

class ClientView():

    def __init__(self):
        pass

    class Client():
        '''getting client information'''
        def __init__(self):
            # set up user name and password
            self.username = ''
            self.password = ''

        def set_username(self):
            self.username = input("Username: ")

        def set_password(self):
            self.password = input('Password: ')

        def get_username(self):
            return self.username
        
        def get_password(self):
            return self.password
    
    class Message():
        def __init__(self):
            self.send_to = ''
            self.message = ''
            self.sender = ''

        def set_message_packet(self):
            ''' Returns a uniform list [sent_to, message, sender]'''
            return [self.send_to, self.message, self.sender]

    class MessageTo(Message):
        '''creating a message and who it is sent to'''
        def __init__(self, client):
            super().__init__(self)
            self.sender = client.get_username

        def set_send_to(self):
            self.send_to = input('Who would you like to message? ')

        def set_message(self):
            self.message = input(f'Type your message for {self.send_to} below\n')

        def display_message_full(self):
            '''Displays message'''
            print(f'{self.message}')

        def get_send_to(self):
            return self.send_to
        
        def get_message(self):
            return self.message

    class MessageFrom(Message):
        '''
        set and display a message recieved
        
        send_to does not matter in this case since the user is the recipient
        '''
        def __init__(self):
            super().__init__(self)

        def set_sender(self, message_list):
            self.sender = message_list[2]

        def set_message(self, message_list):
            self.message = message_list[1]

        def display_message_full(self):
            '''Displays sender and message'''
            print(f'{self.sender}\n{self.message}')
        
        def get_sender(self):
            return self.sender
        
        def get_message(self):
            return self.message

    def main_menu(self):
        '''
        Initial Menu

        Returns user choice
        '''
        print('If you already have an account, type "Y". If not, type "N".')
        choice = input('Do you have an account? ')
        return choice

    def set_client(self):
        ''' Returns a list [username, password]'''
        self.user = self.Client()
        self.user.set_username
        self.user.set_password
        return [self.user.get_username, self.user.get_password]

    def user_menu(self):
        ''' 
        User Menu
        
        Returns user choice
        '''
        print('What would you like to do?')
        print('1. Send a message')
        print('2. View messages')
        print('3. Logout')
        choice = input('Enter Index: ')
        return choice

    def set_send_message(self):
        message = self.MessageTo(self.user)
        message.set_send_to
        message.set_message
        return message.set_message_packet
    
    def recieve_messages(self, list):
        for item in list: # item is currently the message packet
            message_list = item.split('|')
            message = self.MessageFrom
            message.set_sender(message_list)
            message.set_message(message_list)
            message.display_message_full