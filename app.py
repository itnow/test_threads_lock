import time
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from utils import fib_r
from utils import bench


executor = ThreadPoolExecutor(2)
app = Flask(__name__)


@app.route('/slow_req/')
@app.route('/slow_req/<int:n>')
@bench
def slow_req(n=37):
    executor.submit(fib_r, n)
    executor.submit(fib_r, n)
    return 'Heavy CPU calc started in background threads.'


@app.route('/req')
def req():
    time.sleep(1)  # DB delay emulation
    return 'Request done.'
