import logging
import os

logging.basicConfig(level=logging.INFO)

os.environ["API_ID"] = "12345"
os.environ["API_HASH"] = "abcd12345"

os.environ[
    "TELETGCF_CONFIG"
] = """
forwards:
- dest:
  - -1001656
  offset: '316'
  source: -100148156
plugins: {}
show_forwarded_from: false

"""


from teletgcf.config import CONFIG

print(CONFIG)
