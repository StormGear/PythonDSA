from typing import List
import datetime


class Solution:
    def __init__(self):
        self.pattern = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

    def encode(self, strs: List[str]) -> str:
        self.pattern.join(strs)

    def decode(self, s: str) -> List[str]:
        s.split(self.pattern)