import socket
import threading

HEADER = 64 #bytes accepted
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr): #handles individual connection between specific client and server; this runs for EACH client
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected: #wait to receive information from client
        msg = conn.recv()

def start(): #handles new connections and distributes them where to go
    server.listen() #listening to new connections
    while True: #continue to listen until we don't want to listen anymore
        conn, addr = server.accept() # this will wait for a new connection to the server; when there is a connection, we'll store an address and object to send info back
        thread = threading.Thread(target=handle_client, args = (conn, addr)) #when a new connection occurs, we'll pass the connection to handle_client
        thread.start() #starts the thread
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting ...")
start()