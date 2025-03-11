# HOMEWORK 1  
**Todireanu Valentin, MISS1**

---

## Explanations regarding implementation and tests

---

### ⚙️ TCP

The TCP approach used in the provided code demonstrates a basic TCP server-client communication model in Python using the `socket` library.  
TCP (Transmission Control Protocol) is a connection-oriented protocol, ensuring reliable, ordered delivery of a stream of bytes between applications running on hosts communicating via an IP network.


### ⚙️ UDP

The UDP (User Datagram Protocol) approach in the code illustrates how to set up a basic UDP server-client communication using Python's `socket` library.  
Unlike TCP, UDP is a connectionless protocol.  
This results in a simpler, faster communication process, though it lacks built-in mechanisms for reliability, order, and data integrity.

## ✅ Test Results

---
## 1GB Data transfer:

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

## 5GB Data transfer:

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
- By the test results, the **TCP connection is generally slower and more reliable** compared to the UDP without stop_and_wait, but faster than UDP with stop_and_wait.  
- The tests included sending **1GB** and **5GB** of byte messages from a client to a server.  
- The messages were generally **1MB** in size, ensuring a fair comparison between TCP and UDP.

---

### ✅ Test Environment
- Implemented the tests in **Python**.  
---

Got it! Here's a **simple and clear section** with **no file-saving instructions**, just explaining how to **choose between TCP and UDP**, and how to **optionally use `--stop_and_wait`** for UDP.

---

## ✅ Example Command Script: Run Server and Client (TCP or UDP)

```batch
@echo off

echo Starting Server on port 9001...
start cmd /k python server.py --protocol udp --port 9001 --buffer_size 1024 --stop_and_wait

timeout /t 2

echo Running Client...
python client.py --protocol udp --port 9001 --buffer_size 1024 --data_size 5000000000 --stop_and_wait
```

---

### How It Works
- Replace `udp` with `tcp` to run **TCP tests** instead of **UDP**.
- For **UDP**, you can **add** or **remove** the `--stop_and_wait` option:
  - With `--stop_and_wait`: enables **Stop-and-Wait mode** for reliability.
  - Without it: runs in **Streaming mode** (fire-and-forget, faster but may lose packets).

---

### Examples

#### ✅ TCP Example (No `--stop_and_wait` option)
```batch
start cmd /k python server.py --protocol tcp --port 9001 --buffer_size 1024
timeout /t 2
python client.py --protocol tcp --port 9001 --buffer_size 1024 --data_size 5000000000
```

#### ✅ UDP Example with Stop-and-Wait
```batch
start cmd /k python server.py --protocol udp --port 9001 --buffer_size 1024 --stop_and_wait
timeout /t 2
python client.py --protocol udp --port 9001 --buffer_size 1024 --data_size 5000000000 --stop_and_wait
```

#### ✅ UDP Example without Stop-and-Wait (Streaming)
```batch
start cmd /k python server.py --protocol udp --port 9001 --buffer_size 1024
timeout /t 2
python client.py --protocol udp --port 9001 --buffer_size 1024 --data_size 5000000000
```

---

You can adjust:
- `--port` for different ports.
- `--buffer_size` for different message sizes.
- `--data_size` to test with different amounts of data (1GB = `1000000000` bytes, 5GB = `5000000000` bytes).
