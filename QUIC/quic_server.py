import argparse
import asyncio
import sys
import time
from aioquic.asyncio import serve
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived


if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class MyQuicServerProtocol(QuicConnectionProtocol):
    def __init__(self, *args, stop_and_wait=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_bytes_received = 0
        self.total_messages = 0
        self.start_time = None
        self.end_time = None
        self.stop_and_wait = stop_and_wait

    def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            if self.start_time is None:
                self.start_time = time.time()

            data = event.data
            self.total_bytes_received += len(data)
            self.total_messages += 1

            if self.stop_and_wait:
                # Send a simple ACK back (could be more elaborate)
                self._quic.send_stream_data(event.stream_id, b'ACK', end_stream=False)
                self.transmit()

            if event.end_stream:
                self.end_time = time.time()
                self.print_stats()

    def print_stats(self):
        print(f"Protocol: QUIC (Stop-and-Wait: {self.stop_and_wait})")
        print(f"Messages Received: {self.total_messages}")
        print(f"Bytes Received: {self.total_bytes_received}")
        duration = self.end_time - self.start_time if self.end_time and self.start_time else 0
        print(f"Time: {duration:.2f} seconds")


async def run_server(host, port, stop_and_wait):
    configuration = QuicConfiguration(is_client=False)
    await serve(
        host,
        port,
        configuration=configuration,
        create_protocol=lambda *args, **kwargs: MyQuicServerProtocol(
            *args, stop_and_wait=stop_and_wait, **kwargs
        ),
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QUIC Server")
    parser.add_argument('--host', type=str, default='0.0.0.0')
    parser.add_argument('--port', type=int, default=4433)
    parser.add_argument('--stop_and_wait', action='store_true')

    args = parser.parse_args()

    asyncio.run(run_server(args.host, args.port, args.stop_and_wait))
