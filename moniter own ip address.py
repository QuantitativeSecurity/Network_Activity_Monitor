import socket

def monitor_activity():
    # Get your own IP address
    host = socket.gethostbyname(socket.gethostname())
    print("Your IP address: ", host)

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to your IP address and a port number
    s.bind((host, 5000))

    # Start listening for incoming connections
    s.listen()
    print("Listening for incoming connections...")

    # Continuously check for incoming connections
    while True:
        conn, addr = s.accept()
        print("Received connection from: ", addr)

        # Check the incoming data to see if it matches your normal activity pattern
        data = conn.recv(1024)
        if data:
            # Do something if there is unusual activity
            print("Unusual activity detected: ", data)

if __name__ == '__main__':
    monitor_activity()
