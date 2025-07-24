import socket # For connecting to the ip
import threading # To enable Multithreading for faster output

def scan_port(ip, port):
    s = socket.socket()
    s.settimeout(0.3) # To avoid continous scans
    try:
        s.connect((ip, port))
        print(f"[+] Port {port} is open")
    except:
        pass
    finally:
        s.close()

target = input("Target IP: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(target, port))
    t.start()
