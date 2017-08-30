import socket
import getpass


def listenPort(port):
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    buffer=2048
    host=""
    int(port)
    server_socket.bind((host,port))
    server_socket.listen(10)
    connection_number=1

    print port, "opened and connections listing \n"

    while True:
        print connection_number ," connection is waiting ... \n"
        link=server_socket.accept()
        client_addres=server_socket.accept()

        print connection_number,"\n connection acccept\n"
        print  "\n IP adress is ",client_addres

        while True:
            wanted_packet=link.recv(buffer)
            if not wanted_packet:
                break
            print "\nour message is :" , wanted_packet

        link.close()
        print connection_number ,"connection close"
        connection_number +=1


def listenpacket(host,port):
    str(host)
    int(port)

    username=getpass.getuser()
    hostname=socket.gethostname()
    hostadress=socket.gethostbyname(socket.gethostname())
    buffer=1024

    message_for_server=username,hostname,hostadress
    clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    clientsocket.connect((host, port))
    clientsocket.send(message_for_server)
    print "\nmessage sending..."

    server_packet=clientsocket.recv(buffer)
    print "\nmessage is : \n",server_packet

    clientsocket.close()
    print "connection close..."


listenPort(23456)
listenpacket("127.0.0.1",2345)
