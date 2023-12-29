import logging
import os
from os.path import dirname, join

from dotenv import load_dotenv

"""
Settings space to load variables and config the debugging level
"""

envs_path = join(dirname(__file__), ".env")
load_dotenv(envs_path)
logging.basicConfig(level=logging.DEBUG)
KEY = os.environ.get("FACEBOOK_GRAPH_API")
