import socket
def start_client():
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     host= '10.70.24.65' 
     port = 9999
     client_socket.connect((host, port))
     message = client_socket.recv(1024)
     print(message.decode('ascii'))
     client_socket.close()			

if __name__ == "__main__":
    start_client()
