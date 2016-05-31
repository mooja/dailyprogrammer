#!/usr/bin/env node

// Daily Programmer Challenge 222 Intermediate
//
// https://www.reddit.com/r/dailyprogrammer/comments/3chvxy/20150708_challenge_222_intermediate_simple_stream/
//
// 30 May 2016

// linear congruential generator (weak crypto)
function* lgc(seed, n, modulus=256, a=123, c=210) {
    let state = seed;
    for(let i = 0; i < n; i++) {
        state = (a*state + c) % modulus;
        yield state;
    }
}

function encrypt(key, msg) {
    let chars = msg.split('');
    let prandoms = [];
    for(let num of lgc(key, chars.length))
        prandoms.push(num);

    let ciphertext = chars.map((ch, i) =>  {
        let xored_num = ch.charCodeAt(0) ^ prandoms[i];
        return String.fromCharCode(xored_num);
    })
    .join('');
    return ciphertext;
}

function decrypt(key, ciphertext) {
    let cipher_chars = ciphertext.split('');
    let prandoms = [];
    for(let num of lgc(key, cipher_chars.length))
        prandoms.push(num);

    let plaintext = cipher_chars.map((ch, i) =>  {
        let xored_num = ch.charCodeAt(0) ^ prandoms[i];
        return String.fromCharCode(xored_num);
    })
    .join('');
    return plaintext;
}

console.log(encrypt(12345, 'hello world!'));
console.log(decrypt(12345, encrypt(12345, 'hello world!')));
