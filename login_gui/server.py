import socket
import threading


users = {
    "alice": "alice_password",
    "bob": "bob_password",
    "john": "john_password",
    
}



def server():
    def logins():
        print('Server Start At Port 4444 [LOGIN]')
        i = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        i.bind(('localhost',4444))
        i.listen(100)
        print('Listen on port 4444 [LOGIN]')
        while True:
            conn , addr = i.accept()
            threading.Thread(target=login_page,args=(conn ,addr)).start()

    def chats():
        print('Server Start At port 8081 [CHAT]')
        i = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        i.bind(('localhost',8081))
        i.listen(100)
        print('Listen on port 8081 [CHAT]')
        while True:
            conn , addr = i.accept()
            threading.Thread(target=chat , args=(conn ,addr)).start()

    th1 = threading.Thread(target=logins).start()
    th2 = threading.Thread(target=chats).start()


def login_page(conn , addr):
    def login():
            global username 
            try :
                username = conn.recv(1024).decode('utf-8')
                password = conn.recv(1024).decode('utf-8')
                if username in users and users[username] == password:
                    conn.sendall('accept'.encode('utf-8'))
                else :
                    conn.sendall('refuse'.encode('utf-8'))
            except:
                print('Error ?! (Maybe Client Lose Connection) [LOGIN]')
                
    def sign_in():
            try :
                username = conn.recv(1024).decode('utf-8')
                print(username)
                password = conn.recv(1024).decode('utf-8')
                print(password)
                if username in users:
                    conn.sendall('refuse'.encode('utf-8'))
                    login_page(conn , addr)
                else :
                    conn.sendall('accept'.encode('utf-8'))
                    users[username] = password
                    login_page(conn , addr)
            except:
                print('Error ?! (Maybe Client Lose Connection) [LOGIN]')
                
    while True:
        
        ############################################
        #                                          #
        #                MY CODE                   #
        #                                          #
        #############################################
        try :
            print(f'Got New Connection : {addr} [LOGIN]')
            reponse = conn.recv(1024).decode('utf-8')
            print(reponse)
            if  reponse == 'login':
                login()
            else :
                sign_in()
        except:
            print('Error ?! (Maybe Client Lose Connection) [LOGIN]')
            break

def chat(conn ,addr):
    print(f'Got New Connection : {addr} [CHAT]')
    def receive():
        global message 
        try :
            while True:
                username = conn.recv(1024).decode('utf-8')
                message = conn.recv(1024).decode('utf-8')
                if not username or not message:
                    break
                print(f'{username}: {message}')
        except:
            print('Error ?! (Maybe Client Lose Connection) [CHAT]')
    def send():
        try:
        
            conn.sendall(username.encode('utf-8'))
            conn.sendall(message.encode('utf-8'))
                
        except:
            print('Error ?! (Maybe Client Lose Connection) [CHAT]')
    threading.Thread(target=receive).start()
    threading.Thread(target=send).start()
server()
    

