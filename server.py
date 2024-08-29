import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host= '0.0.0.0'
    port = 9999
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started! Listening on {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")
        
        message = 'Thank you for connecting' + "\r\n"
        client_socket.send(message.encode('ascii'))
        client_socket.close()

if __name__ == "__main__":
    start_server()
