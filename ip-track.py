from socket import*

def ip_connect(x,y):
    x = gethostbyname(y)
    print("ip website",web,"is :",x)

web = input("Website: ")
ip_connect(web,web)
