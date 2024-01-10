import socket
import threading


class EchoServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                client_socket.sendall(data)
        except Exception as e:
            print(f"Exception: {e}")
        finally:
            client_socket.close()

    def start(self):
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"Accepted connection from {client_address}")

                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()

        except KeyboardInterrupt:
            print("Server shutting down.")
        finally:
            self.server_socket.close()


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345

    echo_server = EchoServer(host, port)
    echo_server.start()
