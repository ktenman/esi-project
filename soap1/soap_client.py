from suds.client import Client

client = Client('http://localhost:8000/?wsdl', cache=None)

print(client.service.say_hello(u'Maarika', 5))
print(client.service.ping(u'google.com', 2))


# wsdl = Client('http://www.learnwebservices.com/services/hello?wsdl', cache=None)
# request = {'Name': 'Maarika'}
# print(wsdl.service.SayHello(request))



