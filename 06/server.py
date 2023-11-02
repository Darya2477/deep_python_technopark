import socket, threading, json, requests
from collections import Counter
from queue import Queue

class Worker(threading.Thread):
    def __init__(self,  worker_id, url_queue):
        super().__init__()
        self.worker_id = worker_id
        self.url_queue = url_queue
        self.word_count = {}

    def run(self):
        while True:
            url, client_socket = self.url_queue.get()
            self.process_url(url, client_socket)
            self.url_queue.task_done()

    def process_url(self, url, client_socket):
        response = requests.get(url)
        text = response.text
        words = text.split()
        self.count_words(words)

        json_result = json.dumps(self.word_count)
        client_socket.send(json_result.encode())

    def count_words(self, words):
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1


class Master:
    def __init__(self, worker_count):
        self.worker_count = worker_count
        self.workers = []
        self.url_queue = Queue()

    def start(self):
        for i in range(self.worker_count):
            worker = Worker(i, self.url_queue)
            self.workers.append(worker)
            worker.start()

    def get_worker(self):
        return self.workers[self.url_queue.qsize() % self.worker_count]


class Server:
    def __init__(self, host, port, worker_count):
        self.host = host
        self.port = port
        self.worker_count = worker_count
        self.master = None
        self.url_count = 0

    def start(self):
        self.master = Master(self.worker_count)
        self.master.start()

        self.bind_socket()
        self.accept_clients()

    def bind_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()

    def accept_clients(self):
        while True:
            client_socket, _ = self.socket.accept()
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        self.url_count += 1
        worker = self.master.get_worker()
        worker.url_queue.put((client_socket.recv(1024).decode().strip(), client_socket))

    def print_statistics(self):
        print(f"Total URLs processed: {self.url_count}")

if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    worker_count = 5  # количество рабочих потоков
    server = Server(host, port, worker_count)
    server.start()