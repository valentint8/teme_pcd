@echo off
echo Starting UDP Server on port 9001...
start cmd /k python server.py --protocol udp --port 9001 --buffer_size 1024

timeout /t 2 /nobreak
echo Running TCP Client...
python client.py --protocol udp  --port 9001 --buffer_size 1024 --data_size 1000000000

echo UDP Test Completed!
pause



@REM # TCP client: Send 500MB over TCP to server on port 9001
@REM python client.py --protocol tcp --server_ip 127.0.0.1 --port 9001 --buffer_size 1024 --data_size 500000000
@REM
@REM # UDP client: Fire-and-Forget mode, sending 100MB
@REM python client.py --protocol udp --server_ip 127.0.0.1 --port 9001 --buffer_size 1024 --data_size 100000000
@REM
@REM # UDP client: Stop-and-Wait mode, sending 1GB
@REM python client.py --protocol udp --server_ip 127.0.0.1 --port 9001 --buffer_size 1024 --data_size 1000000000 --stop_and_wait
