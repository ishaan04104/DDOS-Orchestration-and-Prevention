import threading
import requests

url = 'http://localhost:3200/'
num_threads = 1000
num_requests_per_thread = 1000
data = {'email': 'test@example.com', 'password': 'password'}

def send_request(thread_id):
    for _ in range(num_requests_per_thread):
        try:
            response = requests.post(url, data=data)
            print(f"Thread {thread_id}: Response - {response.status_code}")
        except Exception as e:
            print(f"Thread {thread_id}: An error occurred - {str(e)}")

threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_request, args=(i+1,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished.")