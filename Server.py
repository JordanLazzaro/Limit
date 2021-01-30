import socket
import sys

#TODO: move print statements to output standard error
class LimitServer:
    def __init__(self, ip, port):
        self.client_conn, self.client_address = self.start_server(ip, port)
    
        try:
            print('connection from', self.client_address, file=sys.stderr)

            # Receive the data in small chunks and retransmit it
            while True:
                data = self.client_conn.recv(16)
                print('received "%s"' % data)
                if data:
                    print('sending data back to the client')
                    self.client_conn.sendall(data)
                else:
                    print('no more data from', client_address)
                    break
                
        finally:
            # Clean up the connection
            self.client_conn.close()

    def start_server(self,ip, port):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = (ip, port)
        print('starting up on %s port %s' % server_address, file=sys.stderr)
        sock.bind(server_address)
        # Listen for incoming connections
        sock.listen(1)

        while True:
            # Wait for a connection
            print('waiting for a connection', file=sys.stderr)
            return sock.accept()
            

    
