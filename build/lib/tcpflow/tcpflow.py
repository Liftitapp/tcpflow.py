import subprocess
import re
from queue import Queue, Empty
from threading import Thread
from typing import Iterator, List, Any, Optional


class TcpFlow(Thread):
    cmd = ['tcpflow', '-p', '-c', '-i', 'en1', 'port', '80']

    def __init__(self) -> None:
        super(TcpFlow, self).__init__()
        self.daemon = True
        self.q = Queue()
        self.matches = []  # List[str]
        self.process = subprocess.Popen(
            TcpFlow.cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.gen = self.Generator(self.process)

    def __enter__(self) -> object:
        self.start()
        return self

    def run(self) -> None:
        for _, host in enumerate(self.gen):
            self.q.put(host)

    def contains(self, host: str) -> bool:
        while True:
            try:
                h = self.q.get(timeout=1)
                self.matches.append(h)
            except Empty:
                return host in self.matches

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None:
        self.process.kill()

    class Generator(object):
        def __init__(self, process: subprocess.Popen) -> None:
            self.process = process

        def __iter__(self) -> Iterator[str]:
            while True:
                retcode = self.process.poll()  \
                    # returns None while subprocess is running
                line = self.process.stdout.readline()
                res = self.is_valid(line)
                if res is not None:
                    yield res
                if retcode is not None:
                    break

        @staticmethod
        def is_valid(line: bytes) -> Optional[str]:
            sline = line.decode('utf-8')
            patt = re.search(r'Host: (.*)\r.*', sline)
            if patt is not None:
                host = patt.group(1)
                return host
