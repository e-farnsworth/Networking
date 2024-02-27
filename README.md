# Overview

This is a basic client-server chat program. Users are able to connect to a server and send messages to others. Once a user is connected to the server, they are able to log on to the program or create an account. Once logged on, they are prompted about what they want to do. These options are curently limited to sending messages and viewing any messages addressed to them. Each message sent or recieved contains who the message is being sent to, the message itself, and the sender.

This is a client to server program. The ServerMain.py file needs to be run first. After the set up reads out, then ClientMain.py files can be run. Additional files that need to be created are two text files for storing the users and the pending messages. In this program, the files are default as Users.txt and PendingMessages.txt.

The purpose of writting this software is to get an introduction into the world of network programming. This program has not only taught me much about both client to server programing, but it has also led me to learn about peer to peer programing as I need to distinguish between the two. This program is still a work in progress and I still have a lot to learn.

Program is still a work and progress and thus no demo video is available yet

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

This is a client/server type program. The files for each are seperated into the two labeled folders for clarity. This is an attempted TCP program.

The majority of information sent between the two are single bursts of information. This inclues the client's username and password. There are also several instances of verification durring the log on process to ensure that there are no duplicates for the usernames when generateing a new user or that the username is correct. 

Message packets are strings that contain three peices of information divided by a single vertical bar. The packets take the general form of "SEND TO|MESSAGE|SENDER".

# Development Environment

* Python 3.10
* Python library socket
* Visual Studio Code
* Git and GitHub


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [What's the Difference Between TCP and UDP?](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [Socket Programming in Python](https://www.geeksforgeeks.org/socket-programming-python/)
* [Implimentation of a simple client-server program | github](https://github.com/kanika2296/client-sever-password-based-authentication-in-python/tree/master)
* [Reading and Writing to text files in Python - GeeksforGeeks](https://www.geeksforgeeks.org/reading-writing-text-files-python/)

# Future Work

* Ensuring everything works properly
* Verification for sending to a user in the system
* Old messages will be stored in the cloud once read
* The use of a GUI