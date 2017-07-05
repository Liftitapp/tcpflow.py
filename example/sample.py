from http.client import HTTPConnection
from tcpflow import TcpFlow


if __name__ == '__main__':
    with TcpFlow() as flow:
        conn = HTTPConnection("google.com", 80)
        conn.request('GET', '/', '', {})
        conn.getresponse()
        print(f"exists? {flow.contains('google.com')}")
