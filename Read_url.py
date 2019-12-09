import time
import requests

def download_file(url):
    response = requests.get(url)
    return response.content

def write_file(n, content):
    filename = f'sync_{n}.html'
    with open (filename,'wb') as f:
        f.write(content)

if __name__ =="__main__":
    t=time.perf_counter()

    for n , url in enumerate(open("url.txt").readlines()):
        content = download_file(url)
        write_file(n,content)
        t2=time.perf_counter() -t
        print(f"Time Taken {t2:2.2f} seconds")