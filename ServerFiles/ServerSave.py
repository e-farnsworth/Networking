class ServerSave():
  def __init__(self):
    self.user_dict = {}
    self.pending_messages_dict = {}

  def set_user_dict(self):
    ''' When the server is put up, pulls the past info for easy access'''
    try:
      file = open(r'ServerFiles/Users.txt')
      for line in file:
        user = line.split('|')
        self.user_dict[user[0]] = user[1]
      file.close
    except IOError:
      print('file can\'t be opened')
    except:
      print('something else went wrong')
  
  def append_user_file(self,user_info):
    try:
      file = open(r'ServerFiles/Users.txt', 'a') # the 'a' is for append mode
      file.write(user_info)
      file.close
    except IOError:
      print('file can\'t be opened')
    except:
       print('something else went wrong')

  def find_user(self, username):
      '''
  Used to see if a user is in already in the user dictionary/files
  
  Returns bool
  '''
      if username in self.user_dict:
          return 'True'
      else:
          return 'False'

  def verify_password(self, client):
      '''
      used to verify the password of a particular client
      
      Input client is a list [username, password] gotten from the client

      Returns bool
      '''
      password = dict[client[0]]
      if client[1] == password: # if the password is correct
          return 'True'
      else:
          return 'False'

  def set_pending_messages_dict(self):
    ''' When the server is put up, pulls the past info for easy access'''
    file = open(r'ServerFiles/PendingMessages.txt', 'r')
    for line in file:
      message = line.split('|') # message should be in the order of [send_to, message, sender]
      if message[0] in self.pending_messages_dict: # if there is already an instance of messages to this user
        message_list = self.pending_messages_dict[message[0]]
        message_list.append(message)
        self.pending_messages_dict[message[0]] = message_list
      else: 
        self.pending_messages_dict[message[0]] = [message] # create a list of lists for the reciever

      file.close

  def get_pending_messages(self, username):
    if username in self.pending_messages_dict:
      messages = self.pending_messages_dict[username]
      send_list = []
      for message in messages: # [send_to, message, sender]
          entry = f'{message[0]}|{message[1]}|{message[2]}'
          send_list.append(entry)
      # After getting the information, delete the pending entries for that person
      del self.pending_messages_dict[username]
      return send_list
    else:
       return 'No new messages'
    
  def add_new_message(self, message_packet):
    message = message_packet.split('|') # list will be [send_to, message, sender]
    if message[0] in self.pending_messages_dict:
      message_list = self.pending_messages_dict[message[0]]
      message_list.append(message)
      self.pending_messages_dict[message[0]] = message_list
    else: 
      self.pending_messages_dict[message[0]] = [message] # create a list of lists for the reciever

    # When a new message is added, it updates the file for everone
    self.set_pending_messages

  def set_pending_messages(self):
    ''' Updates the Pending Messages.txt file '''
    file = open(r'ServerFiles/PendingMessages.txt', 'w')
    for user in self.pending_messages_dict:
      message_list = self.pending_messages_dict[user]
      for message in message_list:
        file.write(f'{message[0]}|{message[1]}|{message[2]}\n')

'''
'''
       
