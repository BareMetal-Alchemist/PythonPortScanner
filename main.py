import socket

target = "127.0.0.1"


service = ""
for i in range(8079, 8082):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect((target, i))

        try:
            
            service = s.getservbyport(i)
            

        except:
            service = "unknown"
        print(i, ": Port Open Service: ", service)
    except:
        service = "none"
        print(i, ": Port Closed Service: ", service)

    






