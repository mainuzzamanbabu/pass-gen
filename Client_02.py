import socket

def generate_partial_phrase(x):
    m = 10
    c = .5
    y = m * x + c
    return y

HOST = '127.0.0.1'
PORT = 9090
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

data = int(input("Enter data for seed : "))

client.send("Hello World\n".encode(('utf-8')))

received_message = client.recv(1024).decode('utf-8')
print(received_message)
received_message = client.recv(1024).decode('utf-8')
print(received_message)
list = received_message.split(" ")
print(list)

generated_seed = str(generate_partial_phrase( data ))
print(f"This is the generated seed: {generated_seed}")
client.send(f"{generated_seed}\n".encode(('utf-8')))