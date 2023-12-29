"""
This script is for get all links of  one list of links
"""

import validators


class FilesWithFormat:
    def __init__(self, path: str):
        self.path = path

    def get_files(self):
        pass

    def validate_urls(self):
        return validators.url(self.path)
