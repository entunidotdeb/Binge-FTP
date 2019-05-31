import socket
import sys,os,re



serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '193.138.218.164'
port = int(sys.argv[2])
serv.connect((host,port))
print ("Connection Established...[OK]")

#text1 = You are in the root directory.
text1 = serv.recv(4096)
print text1
#root_content after 5 sec
root_content = serv.recv(4096)
print root_content

#text2 = Enter the name of the file or folder:
ff = raw_input(serv.recv(4096))
serv.send(ff)

def check():
    #existence
    exists = serv.recv(1024)
    print (exists +"\n")
    if("Empty folder" in exists):
        print ("Connection Closed Sucessfully.....[OK]")
    elif("Directory mentioned" in exists):
        sub = serv.recv(4096)
        print sub
        global ff
        sd = serv.recv(4096)
        ff = raw_input(sd)
        serv.send(ff)
        check()
    elif("File exists" in exists):
        fb = open(ff,"w+")
        file = serv.recv(8192)
        fb.write(file)
        print("file received\n Connection Closed Sucessfully...[OK]")
    else:
         print "Bye"

check()
