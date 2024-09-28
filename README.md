# Redis Lite

Redis Lite is a lightweight, in-memory key-value store that mimics Redis functionality. Built in Python, it supports basic commands like `SET` and `GET` using the RESP protocol for client-server communication. Ideal for learning and small projects, Redis Lite is easy to set up and use, demonstrating key-value data storage concepts.

## Features

- **In-Memory Storage:** Fast access to data with in-memory storage.
- **RESP Protocol:** Implements the Redis Serialization Protocol for communication.
- **Basic Commands:** Supports essential Redis commands such as `SET` and `GET`.
- **Lightweight:** Minimalistic design for easy deployment and learning.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mikey-mike6768/redis-lite.git
   cd redis-lite/src
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

To start the Redis Lite server, run:
```bash
python redis_server.py
```

### Using the Client

To interact with the server, run the client:
```bash
python redis_client.py
```

You can then issue commands like:
```
SET key1 "value1"
GET key1
```

### Example

1. Start the server:
   ```bash
   python redis_server.py
   ```

2. In a new terminal, run the client:
   ```bash
   python redis_client.py
   ```

3. Issue commands:
   ```
   SET key1 "value1"
   GET key1
   ```

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features!

## Acknowledgments

- Inspired by Redis, a powerful in-memory data structure store.
