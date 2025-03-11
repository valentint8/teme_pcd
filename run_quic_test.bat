@echo off
echo Starting QUIC Server on port 4433...
start cmd /k python QUIC/quic_server.py --host 0.0.0.0 --port 4433 --stop_and_wait

timeout /t 2 /nobreak

echo Running QUIC Client...
python QUIC/quic_client.py --host 127.0.0.1 --port 4433 --data_size 500000000 --buffer_size 1024 --stop_and_wait

echo QUIC Test Completed!
pause
