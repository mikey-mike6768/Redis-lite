import socket

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 6379))
        client_socket.sendall(command.encode())
        response = client_socket.recv(4096).decode()
        return response

if __name__ == "__main__":
    # Step 1: Set a key-value pair
    set_command = "SET key1 value1\r\n"
    response = send_command(set_command)
    print("Response:", response)

    # Step 2: Get the value of the key
    get_command = "GET key1\r\n"
    response = send_command(get_command)
    print("Response:", response)
