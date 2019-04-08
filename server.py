import socket
import argparse
import threading

def submit(conn) :
        receive = conn.recv(1024)
        receive= receive.decode()
        receive = receive[::-1]
        conn.sendall(receive.encode())

def run_server(port=4000):
        host = ""

        with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen(1)
            
            while True :
                conn, addr = s.accept()
                send = threading.Thread(target = submit, args=(conn,))

                send.start()
                send.join()

            conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument("-p", help="port_number", required=True)

    args = parser.parse_args()
    run_server(port=int(args.p))