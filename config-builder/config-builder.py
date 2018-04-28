import socket
from os import getenv
from jinja2 import Template

PROMCONF = '{}/prometheus.yaml'.format(getenv('SNAP_COMMON'))

template = Template("""
global:
  scrape_interval: 120s
  evaluation_interval: 15s
  scrape_timeout: 10s

  external_labels:
    device_id: {{ device_id }}
    snap_version: {{ snap_version }}
    snap_revision: {{ snap_revision }}

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090', 'localhost:9100']
""")

config = template.render(
    device_id=socket.gethostname(),
    snap_version=getenv('SNAP_VERSION'),
    snap_revision=getenv('SNAP_REVISION'),
)

print('Writing config to {}'.PROMCONF)
print(config)

with open(PROMCONF) as f:
    f.write(config)
