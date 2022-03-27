from suds.client import Client

client = Client('http://localhost:8000/?wsdl', cache=None)

print(client.service.ping(u'goojgcghcjhchgle.com', 2))
print(client.service.ping(u'google.com', 2))
print(client.service.domain_ip(u'google.com'))
print(client.service.name_servers(u'google.com'))
