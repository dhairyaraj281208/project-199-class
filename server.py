import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 1355

questions = ["1. Who is the Father of our Nation? \n a.Charlie Chapline \n b. Rahul gandhi \n c. Dhairya raj maloo \n d. Mahatma gandhi",
            "2. Who was the first President of India?\n a. Donald Trump \n b. Mukesh Ambani \n c. Patrakar Popatlal d. Dr. Rajendra Prasad",
            "3. Which is the most sensitive organ in our body?\n a. Skin \n b. Brain \n c. Heart \n d. Legs",
            "4. Giddha is the folk dance of?\n a. Lahore \n b. Spain \n c. Punjab \n d. Portugal"]

answers = ['d', 'd', 'a', 'c']

server.bind((ip_address, port))
server.listen()

list_of_clients = []

print("Server Is Running!")
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + "Connected")

    new_thread = Thread(target=clientthread, args=(conn, addr))
    new_thread.start()

def clientthread(conn, addr):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will recieve a question. The answer to that question should bo one of a, b, c, d\n".encode('utf-8'))
    conn.send("Good Luck! \n\n". encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2049).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1
                    conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect answer! Better luck next time!\n\n".encode('utf-8'))
            else:
                remove(conn)
        except:
            continue
                    
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!= connection:
            try:
                clients.send(message.encode('utf-8'))
            except:
                remove(clients)

def get_random_questton_answer(conn) :
    random_index = random.randint(0,len(questions) - l)
    random_question = questions [random_index]
    random_answer = answers[random_index]
    conn.send(random_question,encode( 'utf-8' ) )
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)