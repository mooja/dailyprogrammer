#!/usr/bin/env python
# encoding: utf-8

from binascii import unhexlify
from Crypto.Cipher import AES
from struct import unpack


class BlockCipher(object):
    """
    Block Cipher Class which implements the secure PRP primitive
    using the AES algorithm.

    Subclass this class to implement specific Block Cipher Modes of Operation
    """

    def __init__(self, key):
        self.key = key
        self.AES = AES.new(self.key)

    @staticmethod
    def _xor_blocks(block_a, block_b):
        block_a = bytearray(block_a)
        block_b = bytearray(block_b)
        xored_block = bytearray()
        for a, b in zip(block_a, block_b):
            xored_block.append(a ^ b)
        return str(xored_block)

    @staticmethod
    def _block_to_num(block):
        bytes = unpack('16B', block)
        num = 0
        for byte in bytes:
            num = num << 8
            num += byte
        return num

    @staticmethod
    def _num_to_block(num):
        block = bytearray()
        for _ in range(16):
            postfix = num % 256
            block.insert(0, postfix)
            num = num >> 8
        return str(block)


class CbcCipher(BlockCipher):
    """
    Cipher Block-Chain mode of operation.
    Decryption XORs the result of D(k, c_i) with c_(i-1)
    First block is XORed with the IV
    """
    def decrypt(self, ctext):
        iv = ctext[:16]
        ctext = ctext[16:]
        ptext = bytearray()

        prev_cblock = iv
        for i in range(0, len(ctext), 16):
            cblock = ctext[i:i+16]
            tblock = self.AES.decrypt(cblock)
            tblock = self._xor_blocks(tblock, prev_cblock)
            ptext.extend(bytearray(tblock))
            prev_cblock = cblock

        return str(ptext)


class CrtCipher(BlockCipher):
    """
    CRT (Counter) mode of operation.
    Decryption XORs each C_i with E(k, nonce_i)  where nonce
    is usually the IV + counter.

    Semantically this is simliar to a stream cipher whose PRG's domain is
    128 bits
    """

    def decrypt(self, ctext):
        iv = ctext[:16]
        iv_num = self._block_to_num(iv)
        ctext = ctext[16:]
        ptext = bytearray()

        counter = 0
        for i in range(0, len(ctext), 16):
            # generate and encrypt the unique nonce
            nonce = iv_num + counter
            nonce_block = self._num_to_block(nonce)
            nonce_encrypted = self.AES.encrypt(nonce_block)

            # xor encrypted with the cipher block to get plain text
            cblock = ctext[i:i+16]
            tblock = self._xor_blocks(cblock, nonce_encrypted)

            ptext.extend(bytearray(tblock))
            counter += 1

        return str(ptext)


if __name__ == '__main__':
    # CBC keys and cipher texts
    cbc_key = unhexlify("140b41b22a29beb4061bda66b6747e14")
    cbc_ctext1 = unhexlify(
        '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee'
        '2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
    cbc_ctext2 = unhexlify(
        '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48'
        'e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253')

    # CRT keys and cipher texts
    crt_key = unhexlify("36f18357be4dbd77f050515c73fcf9f2")
    crt_ctext1 = unhexlify(
        '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc38'
        '8d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f'
        '51eeca32eabedd9afa9329'
    )
    crt_ctext2 = unhexlify(
        '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0'
        'e311bde9d4e01726d3184c34451'
    )

    cbc = CbcCipher(cbc_key)
    msg1 = cbc.decrypt(cbc_ctext1)
    msg2 = cbc.decrypt(cbc_ctext2)
    print('cbc message 1: {}'.format(str(msg1)))
    print('cbc message 2: {}'.format(str(msg2)))

    crt = CrtCipher(crt_key)
    msg1 = crt.decrypt(crt_ctext1)
    msg2 = crt.decrypt(crt_ctext2)
    print('crt message 1: {}'.format(str(msg1)))
    print('crt message 2: {}'.format(str(msg2)))
