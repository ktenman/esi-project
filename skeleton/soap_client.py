from suds.client import Client

client = Client('http://localhost:8090/?wsdl', cache=None)

print("Running Service 1 ...")
print(client.service.ping('google.com', 2))
print("Running Service 2 ...")
print(client.service.domain_ip('google.com'))
print("Running Service 3 ...")
print(client.service.name_servers('google.com'))
