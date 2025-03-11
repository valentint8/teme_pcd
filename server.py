import socket
import argparse
import time

def tcp_server(port, buffer_size):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        print(f"TCP Server listening on port {port}")
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            total_data_received = 0
            start_time = time.time()
            while True:
                data = conn.recv(buffer_size)
                if not data:
                    break
                total_data_received += len(data)
            end_time = time.time()
            print(
                f'Protocol: TCP, Messages Read: {total_data_received / buffer_size}, Bytes Read: {total_data_received}, Time: {end_time - start_time}')


def udp_server(port, buffer_size, stop_and_wait=False):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('', port))
        print(f"Server listening on port {port}")

        total_data_received = 0
        start_time = time.time()

        try:
            while True:
                data, addr = s.recvfrom(buffer_size)
                if not data:
                    continue  # Ignore empty messages

                if data == b"END":
                    print(f"Received termination message from {addr}. Closing server.")
                    break

                total_data_received += len(data)
                #print(f"Received {len(data)} bytes from {addr}")
                if stop_and_wait:
                    s.sendto(b"ACK", addr)

        except KeyboardInterrupt:
            print("Server interrupted manually.")

        end_time = time.time()
        print(f'Protocol: UDP, Messages Read: {total_data_received / buffer_size}, '
              f'Bytes Read: {total_data_received}, Time: {end_time - start_time:.2f}s')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Server for TCP or UDP protocol.')

    parser.add_argument('--protocol', choices=['tcp', 'udp'], required=True, help='Protocol to use (tcp or udp)')

    parser.add_argument('--stop_and_wait', action='store_true',
                        help='Enable Stop-and-Wait mode (UDP only). Default is Fire-and-Forget')

    parser.add_argument('--port', type=int, default=12345, help='Port number')

    parser.add_argument('--buffer_size', type=int, default=1024, help='Buffer size in bytes')
    args = parser.parse_args()

    print(args.stop_and_wait)

    if args.protocol == 'tcp':
        tcp_server(args.port, args.buffer_size)
    elif args.protocol == 'udp':
        udp_server(args.port, args.buffer_size, stop_and_wait=args.stop_and_wait)
