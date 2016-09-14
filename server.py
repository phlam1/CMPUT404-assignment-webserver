#  coding: utf-8 
import SocketServer
import os
import os.path
import StringIO
import requests

#From stackoverflow citied
from os.path import exists

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print ("Got a request of: %s\n" % self.data)
        
        #Takes first line of data
        inputdata = StringIO.StringIO(self.data)
        line1 = inputdata.readline()
        
        #Print test
        print("line1 --> " + line1)
        #self.request.sendall("ok\n")
      	#self.request.sendall("first line of request --> " + line1 + "\n")
      	split_line = line1.split()
      	
      	#Http command
      	command = split_line[0]
      	#Print test
      	print("command --> " + command)
      	
      	#Http URI
      	base = split_line[1]
      	#Print test
      	print("base --> " + base)
      	
      	#self.request.sendall(line2[0])
      	
      	#Format user path
      	user_path = ("www" + base)
      	print("user path --> " + user_path)
      	user_path = user_path.strip()
      	print("Stripped user_path --> " + user_path)
      	print(os.path.exists(user_path))
      	
      	#test
      	#self.request.sendall("user path --> " + user_path + "\n")
      	
      	#Determines if file is in www
      	#Not Working yet
      	
      	
      	
      	if os.path.exists(user_path) == True:
      	    #test
      	    #self.request.sendall("access GRANTED\n")
      	    print("access GRANTED")
      	    #Handle requests
      	    
      	    if (base == "/"):
      	    	openfile = open("www/index.html", "r")
      	    	file_information = openfile.read()
      	    	self.request.send('HTTP/1.1 200 OK\r\n')
      	    	self.request.send('Content-Type: text/html\r\n\r\n')
      	    	self.request.send(file_information)
      	    
      	    if (".html" in user_path):
      	    	openfile = open(user_path, "r")
      	    	file_information = openfile.read()
      	    	#Code from citied stackoverflow url
      	    	# Establish connection with client.    
      	    	self.request.send('HTTP/1.1 200 OK\r\n')
      	    	self.request.send('Content-Type: text/html\r\n\r\n')
      	    	self.request.send(file_information)
      	    
      	    if (".css" in user_path):
      	    	openfile = open(user_path, "r")
      	    	file_information = openfile.read()
      	    	self.request.send('HTTP/1.1 200 OK\r\n')
      	    	self.request.send('Content-Type: text/css\r\n\r\n')
      	    	self.request.send(file_information)
      	    	
      	    if (base == "/deep/"):
      	    	user_path = user_path + "index.html"
      	    	openfile = open(user_path, "r")
      	    	file_information = openfile.read()
      	    	self.request.send('HTTP/1.1 200 OK\r\n')
      	    	self.request.send('Content-Type: text/html\r\n\r\n')
      	    	self.request.send(file_information)
      	    
      	    if (base == "/deep"):
      	    	self.request.send('HTTP/1.1 301 Redirect')
      	    	self.request.send(
      	    
      	elif os.path.exists(user_path) == False:
      	    print("access DENIED")
      	    self.request.send('HTTP/1.1 404 Not found\r\n')
      	    
      	    #test
      	    #self.request.sendall("access DENIED\n")

      	    

        

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    SocketServer.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)
   #  print ("This is baseurl %s\n" % self.baseurl)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    
  
