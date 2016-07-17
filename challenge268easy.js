#!/usr/bin/env node

// Daily Programmer Challenge 268 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4knivr/20160523_challenge_268_easy_network_and_cards/

// 17 July 2016

const net = require('net');

if (process.argv[2] !== 'server' && process.argv[2] !== 'client') {
  console.log("Useage: cmd <server|client>.");
  process.exit(1);
}

if (process.argv[2] === 'server') {
  let PONG_STATE = false;
  const server = net.createServer((socket) => {
    socket.write('Welcome to server.\r\n');
    setInterval(() => {
      socket.write('PING\r\n');
      setTimeout(() => {
        if (PONG_STATE === false) socket.end('Client didnt respond to ping.');
        else PONG_STATE = false;
      }, 1000);
    }, 5000);
    socket.on('data', data => {
      if(data.toString().trim() === 'PONG')
        PONG_STATE = true;
    });
    socket.on('error', err => {
    });
  });
  console.log('Listenning on port 1337...');
  server.listen(1337, '127.0.0.1');
}

if (process.argv[2] === 'client') {
  const client = new net.Socket();
  client.connect(1337, '127.0.0.1', () => {
    console.log('Connected.');
  });
  client.on('data', data => {
    console.log(data.toString());
    if (data.toString().trim() === 'PING') {
      client.write('PONG');
      console.log('> PONG');
    }
  });
  client.on('close', () => console.log('Connection closed.'));
}
