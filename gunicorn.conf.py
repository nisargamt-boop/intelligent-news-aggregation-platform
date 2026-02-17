import multiprocessing

# Gunicorn configuration for news aggregator

# Binding
bind = '0.0.0.0:8000'  # Change port if needed
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'  # Use 'gevent' for async support
worker_connections = 1000
timeout = 30
keepalive = 2

# Process naming
proc_name = 'news_aggregator'
pythonpath = 'news_aggregator'

# Logging
accesslog = 'logs/gunicorn.access.log'
errorlog = 'logs/gunicorn.error.log'
loglevel = 'info'

# SSL (uncomment and modify if using SSL)
# keyfile = 'path/to/keyfile'
# certfile = 'path/to/certfile'

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190