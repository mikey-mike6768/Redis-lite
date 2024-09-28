import socket

# Dictionary to store key-value pairs
data_store = {}

def serialize_response(response):
    if isinstance(response, str):
        return f"+{response}\r\n"
    elif isinstance(response, int):
        return f":{response}\r\n"
    elif response is None:
        return "$-1\r\n"
    else:
        return f"${len(response)}\r\n{response}\r\n"

def handle_command(command):
    parts = command.strip().split()
    if not parts:
        return "Invalid command"

    cmd = parts[0].upper()
    
    if cmd == "PING":
        return "PONG"
    elif cmd == "ECHO":
        return " ".join(parts[1:])
    elif cmd == "SET":
        if len(parts) != 3:
            return "Invalid number of arguments for SET"
        key, value = parts[1], parts[2]
        data_store[key] = value
        return "OK"
    elif cmd == "GET":
        if len(parts) != 2:
            return "Invalid number of arguments for GET"
        key = parts[1]
        return data_store.get(key, None)
    else:
        return "Unknown command"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 6379))
    server_socket.listen(5)
    print("Redis Lite Server started on 127.0.0.1:6379")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        try:
            while True:
                command = client_socket.recv(1024).decode()
                if not command:
                    break
                response = handle_command(command)
                serialized_response = serialize_response(response)
                client_socket.sendall(serialized_response.encode())
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
