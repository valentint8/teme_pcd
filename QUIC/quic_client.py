import argparse
import asyncio
import sys
import time
from aioquic.asyncio import connect
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class MyQuicClient:
    def __init__(self, host, port, data_size, buffer_size, stop_and_wait):
        self.host = host
        self.port = port
        self.data_size = data_size
        self.buffer_size = buffer_size
        self.stop_and_wait = stop_and_wait
        self.total_bytes_sent = 0
        self.total_messages = 0

    async def run(self):
        configuration = QuicConfiguration(is_client=True)
        async with connect(self.host, self.port, configuration=configuration) as client:
            stream_id = client._quic.get_next_available_stream_id()
            self.start_time = time.time()

            for i in range(0, self.data_size, self.buffer_size):
                message = b'x' * min(self.buffer_size, self.data_size - i)

                if self.stop_and_wait:
                    # Send the message and wait for ACK
                    client._quic.send_stream_data(stream_id, message, end_stream=False)
                    await client.wait_connected()
                    await client._network.wait_idle()
                    event = await client._network.next_event()

                    if isinstance(event, StreamDataReceived):
                        if event.data != b'ACK':
                            print("Did not receive ACK!")
                            continue
                else:
                    # Streaming mode
                    client._quic.send_stream_data(stream_id, message, end_stream=False)

                self.total_bytes_sent += len(message)
                self.total_messages += 1

            # Close the stream
            client._quic.send_stream_data(stream_id, b'', end_stream=True)
            await client.wait_closed()

            self.end_time = time.time()
            self.print_stats()

    def print_stats(self):
        print(f"QUIC {'Stop-and-Wait' if self.stop_and_wait else 'Streaming'} Transmission Complete")
        print(f"Total Messages Sent: {self.total_messages}")
        print(f"Total Bytes Sent: {self.total_bytes_sent}")
        duration = self.end_time - self.start_time if self.end_time and self.start_time else 0
        print(f"Transmission Time: {duration:.2f} seconds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QUIC Client")
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=4433)
    parser.add_argument('--data_size', type=int, default=500000000)
    parser.add_argument('--buffer_size', type=int, default=1024)
    parser.add_argument('--stop_and_wait', action='store_true')

    args = parser.parse_args()

    client = MyQuicClient(
        args.host,
        args.port,
        args.data_size,
        args.buffer_size,
        args.stop_and_wait
    )
    asyncio.run(client.run())
