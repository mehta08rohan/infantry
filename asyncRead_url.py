import time
import requests

async def download_file(url):
    response = requests.get(url)
    my_resp = await response.content
    return my_resp

def write_file(n, content):
    filename = f'asyncRead_{n}.html'
    with open (filename,'wb') as f:
        f.write(content)

def main():
    t=time.perf_counter()

    for n , url in enumerate(open("url.txt").readlines()):
        content =  download_file(url)
        # write_file(n,content)
        t2=time.perf_counter() -t
        print(f"Time Taken {t2:2.2f} seconds")

main()