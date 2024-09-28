def serialize(data):
    if isinstance(data, str):
        return f"+{data}\r\n"
    elif isinstance(data, int):
        return f":{data}\r\n"
    elif isinstance(data, list):
        return f"*{len(data)}\r\n" + "".join(serialize(item) for item in data)
    elif data is None:
        return "$-1\r\n"
    else:
        raise ValueError("Unsupported data type")

def deserialize(data):
    if data.startswith("+"):
        return data[1:-2]
    elif data.startswith(":"):
        return int(data[1:-2])
    elif data.startswith("$"):
        length = int(data[1:data.find("\r\n")])
        if length == -1:
            return None
        return data[data.find("\r\n")+2:data.find("\r\n")+2+length]
    elif data.startswith("*"):
        items = int(data[1:data.find("\r\n")])
        result = []
        remaining = data[data.find("\r\n")+2:]
        for _ in range(items):
            result.append(deserialize(remaining))
        return result
    else:
        raise ValueError("Invalid RESP message")