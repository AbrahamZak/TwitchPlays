import socket
import os
import KeyProcessor

if __name__ == '__main__':
    server = 'irc.chat.twitch.tv'
    port = 6667
    nickname = 'MrAmericano97'
    token = os.environ.get('token')
    channel = '#kingofsins98'

    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    while True:
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))

        elif len(resp) > 0:
            message_data = resp.split(':')[1:]
            if len(message_data) > 1:
                message = message_data[1].rstrip().lower()
                print(message)
                if KeyProcessor.process_key(message) != "invalid":
                    KeyProcessor.press_key(message)

