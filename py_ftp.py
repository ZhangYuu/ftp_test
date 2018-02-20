#coding:utf-8

#install
#pip insstall pyftpdlib

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#make a new user group
authorizer = DummyAuthorizer()

#add user_name, pwd, path, privilege
authorizer.add_user("blink", "1234", "/Users/Memo/Desktop/FTP/public", perm="elradfmw")#adfmw

#add anonyomous users
#authorizer.add_anonymous("path")

handler = FTPHandler
handler.authorizer = authorizer

#run ftp server
server = FTPServer(("192.168.1.208", 2121), handler)
server.serve_forever()
