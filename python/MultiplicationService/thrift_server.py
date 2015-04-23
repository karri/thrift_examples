#! /usr/bin/env python

import sys
sys.path.append("./gen-py")

from tutorial import MultiplicationService

from thrift import Thrift
from thrift.server import TServer
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol  import TBinaryProtocol

class MultiplicationServiceHandler:
    def __init__(self):
        self.log = {}

    def multiply(self,n1,n2):
        return n1*n2

handler = MultiplicationServiceHandler()
processor = MultiplicationService.Processor(handler)

transport = TSocket.TServerSocket('localhost','9090')
tfactory  = TTransport.TBufferedTransportFactory()
pfactory  = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor,transport,tfactory,pfactory)

print "Starting Python Server"

server.serve()




