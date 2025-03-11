@echo off
echo Starting UDP Server on port 9001...

:: Start the server in a new command prompt window
start cmd /k python server.py --protocol udp --port 9001 --buffer_size 1024 --stop_and_wait > server_output.txt

:: Give the server time to initialize before starting the client
timeout /t 2 /nobreak

echo Running UDP Client...
python client.py --protocol udp --port 9001 --buffer_size 1024 --data_size 1000000000 --stop_and_wait > client_output.txt

echo UDP Test Completed!

:: Show where the logs are saved
echo Server output saved to server_output.txt
echo Client output saved to client_output.txt

pause