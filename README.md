Network Activity Monitor

This script monitors network activity by listening for incoming connections on a specified port. It reports incoming connections and any data sent by the connected clients. The primary goal is to identify and flag potential unusual activity.
Features:

    Host Identification: The script automatically detects the machine's IP address.
    Network Monitoring: Listens for incoming connections on port 5000.
    Activity Logging: Logs the IP address of any client that establishes a connection and any data they send.

Usage:

    Ensure you have the required permissions to listen on the specified port (5000 in this case).
    Run the script. The script will display the machine's IP address and start listening for incoming connections on port 5000.
    Observe the console output for logs about incoming connections and any data received from connected clients.
    To stop the script, use the keyboard interrupt (Ctrl + C).

Code Structure:

    monitor_activity() function: The main function that sets up and starts the network monitoring.
        Initializes and binds a socket to listen for incoming connections on port 5000.
        Continuously checks for and logs incoming connections.
        Reads and logs any data sent by connected clients.

Important Notes:

    The script uses port 5000 to listen for incoming connections. Ensure this port is not being used by another application or service on your machine.
    If you want to listen on a different port, change the 5000 in the s.bind() method to your desired port number.
    The script identifies "unusual activity" as any data sent by connected clients. Depending on your specific use case or requirements, you might want to modify the criteria for what constitutes "unusual activity."
    Running a server that listens for incoming connections can expose your machine to potential threats. Always ensure you have appropriate security measures in place and only run such scripts in trusted environments.
