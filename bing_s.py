import socket
from threading import Thread
import os,sys,time
max_conn = 5

class Mythread(Thread):
    def __init__(self,ip,port,conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        print "New thread started for "+ip+":"+str(port)
    def run(self):
        root  = os.getcwd()
        #text1 = "You are in the " +root+ " Directory.Sub-directories and files are :\n"
        root_sub = converter(os.listdir(root))
        self.conn.send("You are in the " +root+ " Directory.Sub-directories and files are :\n")
        time.sleep(5)
        self.conn.send(root_sub)
        #text2 = "Enter the name of the file or folder:"
        self.conn.send("Enter the name of the file or folder:")
        ff=self.conn.recv(4096)
        ff = root + "/" + ff
        print ff
        if(os.path.exists(ff)):
            check(ff)
        else:
            conn.send("Not Found")

def check(ff):
    if not (os.path.exists(ff)):
        conn.send("Not Found")
    if(os.path.isfile(ff)):
        #exists = "File exists"
        #print exists
        conn.send("File exists")
        file(ff)
    elif(os.path.isdir(ff)) and (os.listdir(ff)) :
        conn.send("The Directory mentioned exists.\nBelow are the sub-directories and files:\n")
        folder(ff)
        conn.send("\nEnter the name of the folder or file: ")
        ss = conn.recv(4096)
        ff = ff + "/" + ss
        print "####" + ff + "####"
        check(ff)
    elif not (os.listdir(ff)):
        conn.send("Empty folder")
    #else:
        #self.conn.send("not found")
def folder(ff):
    time.sleep(5)
    sub = content(ff)
    print "folder-f(x)"+str(sub)
    conn.send(sub)
def file(fl):
    print "file to send "+str(f1)
    fb = open(fl,"rb+")
    file_content = fb.read()
    conn.sendall(file_content)
    print('File Sent')
def content(string1):
    list = os.listdir(string1)
    sub = converter(list)
    print "content-f(x) "+str(sub)
    return (sub)
def converter(list):
    instring = '\n'.join(list)
    print "converter-f(x) "+str(instring)
    return instring

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
pirt = int(sys.argv[2])
serv.bind(('',pirt))
print "Socket Binded...[OK]"
threads = []

while True:
    serv.listen(max_conn)
    print "Connected on port {0}...[OK]".format(pirt)
    (conn,(ip,port))=serv.accept()
    print "Connection Request from :{0}:{1}".format(ip,port)
    print "Connection Established...[OK]"
    newthread = Mythread(ip,port,conn)
    newthread.start()
    threads.append(newthread)


for t in threads:
    t.join()

