#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 258 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4ad23z/20160314_challenge_258_easy_irc_making_a/
#
# 08 July 2016

import socket


host = 'irc.freenode.net'
port = 6667

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'NICK mooja1\r\n')
    s.sendall(b'USER mooja1 0 * :Maxim A Shkurygin\r\n')
    while True:
        data = s.recv(1024).decode('ascii')
        if data.startswith('PING'):
            from_ = data.strip().split()[1]
            response = 'PONG {}\r\n'.format(from_)
            s.sendall(response.encode('ascii'))
        print(data)
