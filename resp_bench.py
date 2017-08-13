import sys
import signal
import requests
from concurrent.futures import ThreadPoolExecutor
from utils import bench


executor = ThreadPoolExecutor(2)


def signal_handler(signal, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


@bench
def make_req(url):
    s = requests.Session()
    s.get(url)


while True:
    make_req('http://127.0.0.1:5000/req')
