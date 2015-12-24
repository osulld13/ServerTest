import sys
import socket
import os


# global threadpool for server
server_thread_pool = threadpool.ThreadPool(40)

port_number = int(sys.argv[1])

def create_server_socket():
    # create socket  and initialise to localhost:8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', port_number)

    print "starting up on %s port %s\n" % server_address

    # bind socket to server address and wait for incoming connections4
    sock.bind(server_address)
    sock.listen(1)

    while True:
        # sock.accept returns a 2 element tuple
        connection, client_address = sock.accept()
        #print "Connection from %s, %s\n" % connection, client_address
        # Hand the client interaction off to a seperate thread
        server_thread_pool.add_task(
            start_client_interaction,
            connection,
            client_address
        )


def start_client_interaction(connection, client_address):
    while True:
        data = connection.recv(1024)
        print "received message: %s" % data



if __name__ == '__main__':
    create_server_socket()
    # wait for threads to complete
    server_thread_pool.wait_completion()

# Plan For Chat Server
#
# Have one socket per client
# Have two threads per client
#   - One listening for messages
#   - One for sending messages
# Have an
