import socket

target = "10.10.11.64"


service = ""
for i in range(0, 100):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, i))
    #service = socket.getservbyport(i)
    if result == 0:
        try:
            
            service = socket.getservbyport(i)
            

        except:
            service = "unknown"
        print(i, ": Port Open Service: ", service)

    else:
        service = "none"
        #print(i, ": Port Closed Service: ", service)
   

    






