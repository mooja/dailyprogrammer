#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 333 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/72ivih/20170926_challenge_333_easy_packet_assembler/
#
# 02 October 2017

import io
import re


test_data = '''
6220    1   10  Because he's the hero Gotham deserves, 
6220    9   10   
5181    5   7   in time, like tears in rain. Time to die.
6220    3   10  So we'll hunt him. 
6220    5   10  Because he's not a hero. 
5181    6   7    
5181    2   7   shoulder of Orion. I watched C-beams 
5181    4   7   Gate. All those moments will be lost 
6220    6   10  He's a silent guardian. 
5181    3   7   glitter in the dark near the Tannhäuser 
6220    7   10  A watchful protector. 
5181    1   7   believe. Attack ships on fire off the 
6220    0   10  We have to chase him. 
5181    0   7   I've seen things you people wouldn't 
6220    4   10  Because he can take it. 
6220    2   10  but not the one it needs right now. 
6220    8   10  A Dark Knight. 
'''
test_data = test_data.strip()


def process_packet(state, msg_id, packet_id, num_packets, text):
    if not msg_id in state:
        state[msg_id] = [None for _ in range(num_packets)]
    state[msg_id][packet_id] = text

    message_complete = all(packet is not None for packet in state[msg_id])
    if not message_complete:
        return

    for packet_id, text in enumerate(state[msg_id]):
        print(msg_id, packet_id, num_packets, text)


if __name__ == '__main__':
    import fileinput
    state = {}
    regexp = re.compile(r'(?P<msg_id>\d+)\s+(?P<packet_id>\d+)\s+(?P<num_packets>\d+)\ +(?P<text>.+)')
    for line in fileinput.input():
        m = regexp.match(line)
        fields = dict(m.groupdict())
        fields['msg_id'] = int(fields['msg_id'])
        fields['packet_id'] = int(fields['packet_id'])
        fields['num_packets'] = int(fields['num_packets'])
        fields['text'] = fields['text']
        process_packet(state, **fields)
