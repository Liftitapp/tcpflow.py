from http.client import HTTPConnection
from tcpflow import TcpFlow


def test_tcpflow():
    with TcpFlow() as flow:
        conn = HTTPConnection("google.com", 80)
        conn.request('GET', '/', '', {})
        conn.getresponse()
        assert flow.contains('google.com') is True
