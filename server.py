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
        self.request.sendall("ok\n")
      	self.request.sendall("first line of request --> " + line1 + "\n")
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
      	#user_path = ("https://127.0.0.1:8080/www" + base)
      	user_path = ("127.0.0.1:8080/www" + base)
      	print("user path --> " + user_path)
      	user_path = user_path.strip()
      	print("Stripped user_path --> " + user_path)
      	print(os.path.exists(user_path))
      	
      	#test
      	self.request.sendall("user path --> " + user_path + "\n")
      	response = requests.post(user_path)
      	self.request.sendall(response)
      	
      	#Determines if file is in www
      	#Not Working yet
      	if os.path.isfile(user_path) == True:
      	    print("access GRANTED")
      	    #Handle requests
      	    response = requests.post(user_path)
      	    self.request.sendall("This is response status: " + response.status_code)
      	
      	    
      	    #test
      	    self.request.sendall("access GRANTED\n")
      	elif os.path.isfile(user_path) == False:
      	    print("access DENIED")
      	    
      	    #test
      	    self.request.sendall("access DENIED\n")
      	    #Handle requests
      	    response = requests.post(user_path)
      	    self.requst.sendall("This is response status: " + response.status_code)
      	
      	    

        

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    SocketServer.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)
   #  print ("This is baseurl %s\n" % self.baseurl)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    
  
