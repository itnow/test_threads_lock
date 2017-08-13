# to run:
#   gunicorn -c gunicorn.conf.py app:app

bind = '127.0.0.1:5000'
backlog = 512
workers = 1
max_requests = 100000
graceful_timeout = 5
