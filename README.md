# HOMEWORK 1  
**Todireanu Valentin, MISS1**

---

## Explanations regarding implementation and tests

---

### ⚙️ TCP

The TCP approach used in the provided code demonstrates a basic TCP server-client communication model in Python using the `socket` library.  
TCP (Transmission Control Protocol) is a connection-oriented protocol, ensuring reliable, ordered delivery of a stream of bytes between applications running on hosts communicating via an IP network.

#### ✅ TCP Server
- **Socket Creation**:  
  The server starts by creating a TCP socket with:
  ```python
  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ```  
  `AF_INET` specifies the IPv4 address family, and `SOCK_STREAM` indicates that this is a TCP socket.

- **Binding and Listening**:  
  The server socket binds to an empty string for the host (`''`), meaning it accepts connections on all available IPv4 interfaces, and to a specified port (`port`).  
  After binding, it listens for incoming connections with `s.listen()`.  
  This prepares the server to accept connections.

- **Accepting Connections**:  
  With `conn, addr = s.accept()`, the server accepts an incoming connection.  
  The `accept` method blocks and waits for an incoming connection.  
  When a client connects, it returns a new socket object representing the connection (`conn`) and a tuple holding the address of the client (`addr`).

- **Receiving Data**:  
  Once a connection is established, the server enters a loop where it receives data from the client using `conn.recv(buffer_size)`.  
  The `buffer_size` parameter determines the maximum amount of data to be received at once.  
  The server accumulates the total data received in `total_data_received`.

- **Session End and Reporting**:  
  When the client closes the connection, `recv` returns an empty bytes object (`b''`), signaling the end of data transmission.  
  The server then calculates the session duration and prints:
  - The protocol used (TCP)
  - The estimated number of messages read (assuming each "message" is of size `buffer_size`)
  - The total bytes received

#### ✅ TCP Client
- **Socket Creation**:  
  Similar to the server, the client creates a TCP socket.

- **Connecting to the Server**:  
  The client uses `s.connect((server_ip, port))` to initiate a connection to the server.

- **Sending Data**:  
  The client breaks down the data into chunks of `buffer_size` and sends each chunk in a loop using `s.send()`.  
  The total bytes sent are tracked.

- **Transmission Time and Reporting**:  
  The client measures the time it takes to send all the chunks and, after the transmission is complete, prints:
  - The total transmission time
  - The number of messages sent (chunks)
  - The total bytes sent

---

### ⚙️ UDP

The UDP (User Datagram Protocol) approach in the code illustrates how to set up a basic UDP server-client communication using Python's `socket` library.  
Unlike TCP, UDP is a connectionless protocol.  
This results in a simpler, faster communication process, though it lacks built-in mechanisms for reliability, order, and data integrity.

#### ✅ UDP Server
- **Socket Creation**:  
  The server initiates a UDP socket with:
  ```python
  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  ```  
  `AF_INET` specifies the IPv4 address family, and `SOCK_DGRAM` indicates a UDP socket.

- **Binding**:  
  The server binds to an empty string for the host (`''`) and a specified port (`port`).

- **Receiving Data**:  
  The server enters a loop, continuously calling `s.recvfrom(buffer_size)`, which waits for data from clients.  
  `recvfrom` returns the received data and the address of the sender.  
  The server processes each received datagram independently.

- **Acknowledgment (ACK)** (Stop-and-Wait):  
  In the stop-and-wait implementation, for each packet received, the server sends back an `"ACK"` message to the sender's address.  
  This requires the client to wait for this acknowledgment before sending the next piece of data, introducing **reliability** into the otherwise **unreliable UDP communication**.

- **Handling Session End**:  
  Since UDP lacks connection termination signals, the server relies on a mechanism such as:
  - Checking for a specific `"END"` message
  - Setting a timeout

#### ✅ UDP Client
- **Socket Creation**:  
  Similar to the server, the client creates a UDP socket.

- **Sending Data with Stop-and-Wait**:  
  The client breaks the data into chunks and sends each chunk using `s.sendto()`, specifying the server's address.  
  After sending each chunk, it waits for an acknowledgment from the server before proceeding.  
  This loop resends the current chunk if no acknowledgment is received within a specified timeout.

- **Timeouts**:  
  The client uses `s.settimeout()` to specify how long it should wait for an acknowledgment before resending.  
  This is crucial for handling packet loss or network delays.

- **Transmission Report**:  
  The client measures and reports:
  - The transmission time
  - The number of chunks (messages) sent
  - The total bytes sent

---

## ✅ Test Results

---
1GB Data transfer:

### UDP With stop_and_wait
- **Client**:  
  <img width="587" alt="image" src="https://github.com/user-attachments/assets/6147e6a1-2e75-4804-9fd5-0f833cdd545d" />


- **Server**:  
  <img width="538" alt="image" src="https://github.com/user-attachments/assets/a513a6d5-b27e-419c-82ab-aacce0c3deca" />


---

### UDP Without stop_and_wait
- **Client**:  
  <img width="592" alt="image" src="https://github.com/user-attachments/assets/af17ee74-6454-451f-9967-7941597a8617" />


- **Server**:  
  <img width="542" alt="image" src="https://github.com/user-attachments/assets/9a94e815-a02d-41bc-afea-af6b076f0762" />


---

### TCP
- **Client**:  
  <img width="562" alt="image" src="https://github.com/user-attachments/assets/089f3f9c-b5de-4500-a442-4a5a607063f4" />


- **Server**:  
  <img width="623" alt="image" src="https://github.com/user-attachments/assets/87b54972-e6c3-44d6-8ba8-257958629a8e" />


---

5GB Data transfer:

### UDP With stop_and_wait
- **Client**:  
<img width="598" alt="image" src="https://github.com/user-attachments/assets/97772c4a-90c1-438e-b510-42be7e7224ff" />


- **Server**:  
<img width="553" alt="image" src="https://github.com/user-attachments/assets/1f242f0a-6d07-46a8-9a00-00a84a540544" />


---

### UDP Without stop_and_wait
- **Client**:  
<img width="604" alt="image" src="https://github.com/user-attachments/assets/57bde47e-947a-4630-9224-a05cadcb574d" />


- **Server**:  
<img width="584" alt="image" src="https://github.com/user-attachments/assets/d08ec54c-3a78-4b36-8e0c-0107f2da9fec" />


---

### TCP
- **Client**:  
<img width="567" alt="image" src="https://github.com/user-attachments/assets/e31bb01b-5bb1-49de-b7ca-2f18eea1789f" />


- **Server**:  
<img width="633" alt="image" src="https://github.com/user-attachments/assets/f1aa33f8-a4ff-4791-ad58-f9fe19ebf192" />


---

### Summary of Results:
- By the test results, the **TCP connection is generally slower** (based on my tests).  
- The tests included sending **1GB** and **5GB** of byte messages from a client to a server.  
- The messages were generally **1MB** in size, ensuring a fair comparison between TCP and UDP.

---

### ✅ Test Environment
- Implemented the tests in **Python**.  
---
