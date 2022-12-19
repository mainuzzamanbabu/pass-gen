import socket
import random
import requests


def api_seed_generate():
    API_URL = "https://api-inference.huggingface.co/models/xlm-roberta-base"
    headers = {"Authorization": f"Bearer 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"}

    def user_phase_input():
        input_phrase = input("Give me a random string of words: Put <mask> in the 3rd last word!")
        return input_phrase

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": "The answer to the universe is <mask> and nothing .",
    })

    print(output)
    passwords_keys = []

    for i in output:
        # print(i)
        for j in i:
            if (j == 'sequence'):
                print(i[j])
                x = i[j]
                x = x.split(" ")
                passwords_keys.append(x[-3])
    print(passwords_keys)

    dictionary = "abcdefghijklmnopqrstuvwxyz"

    def key_generator(x):
        list = x
        key = random.choice(list)
        return key

    generated_key = key_generator(passwords_keys)
    global key_number
    key_number = 0
    for i in generated_key:
        location_of_string = dictionary.find(i)
        key_number = location_of_string + key_number


f = open('vault.txt', 'a')
api_seed_generate()
a = float((key_number % random.random()))
message = float(a) * (10**8)
message2 = str(message)
message2 = str(message2[0:8])
message = f.write(f"{message2}\n")
f.close()


def generate_partial_phrase(x):
    random.seed(x)
    x = random.random()
    return x

#this is the data structure where the received values are stored from the client
received_phrases = []
print("Server is listening..........")

#always specify the private ip address
HOST = '127.0.0.1'
PORT = 9090


# defining the server and the type of socket, sock_stream means that it is a tcp socket,
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#now we need to bind the server to a host and the port
server.bind((HOST,PORT))

#keep listening, at max 5 connections,
#if more than 5 conections are waiting then we reject
server.listen(5)

while True:
    # we communicate using the communication socket
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    #specifying the number of bytes to receive
    #you need to be able to decode the messages in order to read the messages
    # has the ability to send 1024 bytes
    message = communication_socket.recv(1024).decode('utf-8')

    print(f"Message from the client is {message}")

    communication_socket.send(f"Got your message, Thank You!".encode('utf-8'))
    communication_socket.send(f"Your random seed is {str(generate_partial_phrase(random.randint(0,1000)))}".encode('utf-8'))
    # We do not need the ticket id here for this case
    #ticket_id = ticket_id + 1 # important to increment the number after sent to the client

    # We need to store the message2 as the instance of the password received due to the random seed sent from the server
    message2 = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from the client is {message2}")
    message2 = float(message2) * (10**8)


    # Count is used here to ensure that the message2 is only append into the received_phrases only once and not repeatedly
    count = 0
    if(count < 1):
        received_phrases.append(message2)
        print("These are the received phrases from the assisting clients/peers so far: ")
        print(received_phrases)
        f = open('vault.txt', 'a')
        message2 = str(message2)
        message2 = str(message2[0:8])
        message = f.write(f"{message2}\n")
        f.close()

        # closing the connection with the server and client
        communication_socket.close()
        print(f"Connection with {address} ended")
        count = count + 1