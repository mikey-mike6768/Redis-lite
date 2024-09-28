data_store = {}

def execute_command(command):
    cmd = command[0].lower()

    if cmd == "ping":
        return "PONG"
    elif cmd == "echo":
        return command[1]
    elif cmd == "set":
        key, value = command[1], command[2]
        data_store[key] = value
        return "OK"
    elif cmd == "get":
        key = command[1]
        return data_store.get(key, None)
    else:
        return f"Error: Command {cmd} not recognized" 