#! /usr/bin/env python

import sys
sys.path.append("./gen-py")

from tutorial import MultiplicationService
from tutorial.ttypes import  *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol  = TBinaryProtocol.TBinaryProtocol(transport)

    client = MultiplicationService.Client(protocol)

    transport.open()

    product = client.multiply(4,5)
    print '4*5=%d' % (product)

    transport.close()
    
except Thrift.TException, tx:
    print "%s" % (tx.message)
