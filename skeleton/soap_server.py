from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import os
import platform
import subprocess
import netifaces as ni
import shutil
import socket
import dns
import dns.resolver

class HelloWorldService(ServiceBase):

    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def ping(ctx, domain_name, times):
        """Docstrings for service methods appear as documentation in the wsdl.
        @param domain_name the domain to ping
        @param times the number of times to execute ping
        @return the completed array
        """
        result = []

        hostname = domain_name
        response = os.system(f"ping -c {times} " + hostname)

        if response == 0:
            result.append(f"{hostname} reachable: {True}")
        else:
            result.append(f"{hostname} reachable: {False}")
        return result


    @rpc(Unicode, _returns=Iterable(Unicode))
    def domain_ip(ctx, domain_name):
        """Docstrings for service methods appear as documentation in the wsdl.
        @param domain_name the domain to get ip address
        @return the completed array
        """
        result = []
        result.append(socket.gethostbyname(domain_name))
        return result


    @rpc(Unicode, _returns=Iterable(Unicode))
    def name_servers(ctx, domain_name):
        """Docstrings for service methods appear as documentation in the wsdl.
        @param domain_name the domain to get nameservers: NS, SOA, MX
        @return the completed array
        """
        result = []
        nameservers = dns.resolver.query(domain_name, 'NS')
        for data in nameservers.rrset:
            result.append("NS: "+data.to_text())

        soa = dns.resolver.query(domain_name, 'SOA')
        result.append("SOA: "+soa.rrset[0].mname.to_text())

        mails = dns.resolver.query(domain_name, 'MX')
        for i in range(len(mails.rrset)):
            result.append("MX: "+mails.rrset[i].exchange.to_text())

        return result


application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8090")
    logging.info("wsdl is at: http://localhost:8090/?wsdl")

    server = make_server('127.0.0.1', 8090, wsgi_application)
    server.serve_forever()
