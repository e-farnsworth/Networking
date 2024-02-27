''' 
Biggest Problem so far
the classes I have are not being implimented properly

'''

import socket

from ServerSave import ServerSave

server_s = socket.socket()
print ("Socket successfully created")
 
# reserve a port on the computer 
port_listen = 51362

# Binding the socket to the port, 
# the empty string in the ip feild makes the server listen to requests comming from other computers on the network
server_s.bind(('', port_listen))
print ("socket binded to %s" %(port_listen)) # Dubugging statment
 
# Put the socket into listening mode, 5 is how many conections the server can handle.
server_s.listen(5) # 5 is how many connections are kept waiting if the server is busy
print ("socket is listening") # Dubugging statment

# a forever loop until we interrupt it or 
# an error occurs 

# Might want some of this in the connection loop so it gets updated when someone connects
# server_view = ServerSave()

while True: 

# Establish connection with client. 
  client_connect, addr = server_s.accept()     
  print ('Got connection from', addr )

  # updateing the user dictionary and the pending messages
  # server_view.set_user_dict
  user_dict = {}
  file = open(r'ServerFiles/Users.txt')
  for line in file:
    user = line.split('|')
    user_dict[user[0]] = user[1]
  file.close
  
  # send a thank you message to the client. encoding to send byte type. 
  client_connect.send('Thank you for connecting to the ChattApp'.encode()) 
 
  ''' When the client first connects to log into the program '''
  user = False # the user is not yet verified
  while user == False:
    new_user = client_connect.recv(1024)
    new_user = new_user.decode()
    if new_user == 'False': # if the client already has an account
      # first verify the username
      varification = False
      while varification == False:
        username = client_connect.recv(1024)
        username = username.decode()
        # varification = server_view.find_user(username)
        if username in user_dict:
          varification = 'True'
        else:
          varification = 'False'
        server_s.send(str.encode(varification))
      # then verify the password
      varification = 'False'
      while varification == 'False':
        password = client_connect.recv(1024)
        password = password.decode()
        # varification = server_view.verify_password([username, password])
        
        act_password = dict[username] #actual password
        if act_password == password: # if the password is correct
          varification = 'True'
        else:
          varification = 'False'
        server_s.send(str.encode(varification))
      # everything has been verified
      user = True

    elif new_user == 'True': # new_user == 'True': The client does not have an account
      # first verify the username is not a duplicate
      varification = 'True'
      while varification == 'True':
        username = client_connect.recv(1024) # gets the username
        username = username.decode() # decodes the username
        # varification = server_view.find_user(username) # returns str T if username is in use
        if username in user_dict:
          varification = 'True'
        else:
          varification = 'False'
        server_s.send(str.encode(varification))
      # then set the password
      
      password = client_connect.recv(1024)
      password = password.decode()
      user_dict[username] = password
      user_file_info = f'{username}|{password}' # this is how information is stored
      # server_view.append_user_file(user_file_info)
      file = open(r'ServerFiles/Users.txt', 'a') # the 'a' is for append mode
      file.write(user_file_info)
      file.close
      # everything has been verified
      user = True

    else: # new_user will be 'exit' for the client exiting the log on process
      client_connect.close() # end the connection with client and ends the loop
      break
      
  ''' While loop for when a person is using the program'''
  choice = 0
  while choice != '3': # choice = '3' exits the program
    chocie = client_connect.recv(1024)
    if choice == '1': # recieving and storing messages
      message_packet = client_connect.recv(1024)
      # server_view.add_new_message(message)
      message = message_packet.split('|') # list will be [send_to, message, sender]
      if message[0] in pending_messages_dict:
        message_list = pending_messages_dict[message[0]]
        message_list.append(message)
        pending_messages_dict[message[0]] = message_list
      else: 
        pending_messages_dict[message[0]] = [message] # create a list of lists for the reciever
        client_connect.send(str.encode('Message Sent'))
        '''Updates the Pending message file'''
        file = open(r'ServerFiles/PendingMessages.txt', 'w')
        for user in pending_messages_dict:
          message_list = pending_messages_dict[user]
          for message in message_list:
            file.write(f'{message[0]}|{message[1]}|{message[2]}\n')
      
    elif choice == '2': # loading and viewing pending messages
      # server_view.set_pending_messages_dict
      pending_messages_dict = {}
      file = open(r'ServerFiles/PendingMessages.txt', 'r')
      for line in file:
        message = line.split('|') # message should be in the order of [send_to, message, sender]
        if message[0] in pending_messages_dict: # if there is already an instance of messages to this user
          message_list = pending_messages_dict[message[0]] # extract the messages list
          message_list.append(message) # add the new message to the lsit
          pending_messages_dict[message[0]] = message_list # reset the value to the new list
        else: 
          pending_messages_dict[message[0]] = [message] # create a list of lists for the reciever

      if username in pending_messages_dict:
        messages = pending_messages_dict[username]
        length = len(messages)
        client_connect.send(str.encode(str(length))) # send the length of the list
        send_list = []
        for message in messages: # [send_to, message, sender]
            entry = f'{message[0]}|{message[1]}|{message[2]}'
            send_list.append(entry)
        # After getting the information, delete the pending entries for that person
        
        client_connect.send(str.encode('All Messages Sent'))
        del pending_messages_dict[username] # delete the messages from pending after sending all messages
      else:
        client_connect.send(str.encode('0'))# if the user is not in the pending messages dict, no messages to send

    else: 
      # if the choice is out of range do nothing
      # if choice is 3, will break the loop
      pass

  # only want to break connection when client quits app
  # Close the connection with the client 
  client_connect.close()
   
  # Breaking once connection closed
  break



'''
Will need 2 txt files
  dictionary of users and passwords
  pending messages

Used
  when someone logs on or regesters, verifies that there isn't duplication with Usernames
  when someone send a message that the person uses the program
  
  when someone logs on, looks for any pending messages and 
'''