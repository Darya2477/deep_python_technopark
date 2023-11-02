import threading
import requests
import sys


class Client:
    def send_request(self, url):
        try:
            response = requests.get(url)
            response_data = response.text.encode()
        except requests.exceptions.JSONDecodeError:
            print(f"{url}: Invalid response")

    def run_client(self, url_file, num_threads):
        with open(url_file, "r") as file:
            urls = file.readlines() 

        threads = []
        for url in urls:
            url = url.strip()  
            thread = threading.Thread(target=self.send_request, args=(url,))
            threads.append(thread)
            
        num_threads = min(num_threads, len(threads))
        for thread in threads[:num_threads]:
            thread.start()

        for thread in threads[:num_threads]:
            thread.join()
if __name__ == '__main__':
    console_args = sys.argv[1:]

    if len(console_args) >= 2:
        num_threads = int(console_args[0])
        url_file = console_args[1]

        client = Client()
        client.run_client(url_file, num_threads)
    else:
        print("Usage: python client.py num_threads url_file")
