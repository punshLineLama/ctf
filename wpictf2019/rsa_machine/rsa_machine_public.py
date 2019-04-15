#!/usr/bin/python3

import sys

from Crypto.PublicKey import RSA

def run(inFile, outFile):
    privkey = RSA.generate(2048)
    pubkey = privkey.publickey().exportKey()

    outFile.write(pubkey + b'\n')

    while not outFile.closed:
        outFile.flush()


        line = inFile.readline()
        if not line: #EOF
            break

        line = line.rstrip(b'\n')
        if not line:
            continue

        try:
            [cmd, param] = line.split(maxsplit=1)
        except ValueError:
            outFile.write(b'Parameter required!\n')
            continue

        if cmd == b'sign':
            if param == b'getflag':
                outFile.write(b'No cheating!\n')
            else:
                (signature,) = privkey.sign(param, None)
                outFile.write(str(signature).encode() + b'\n')

        elif cmd == b'getflag':
            signature = int(param)
            if privkey.verify(b'getflag', (signature,)):
                outFile.write(b'[REDACTED]')
                break
            else:
                outFile.write(b'Bad signature!\n')

        else:
            outFile.write(b'Bad command ' + cmd + b'\n')

if __name__ == '__main__':
    run(sys.stdin.buffer, sys.stdout.buffer)

    #molulus= 0xEADB85D00A741D118E7F520777FBE1B4593E26C0BD2953A0C2DBDE6607BE88E005F72990D3D63E11D996AC45A53FF86CBEF2F4A903754334D166165509FBB5EA7441FBD198065C64F0D35DF6763AADDCBD6530C2CD05E737F79F666C819A9CF28687FB494F2FD7EDBCD43EAB04D6843FAC804BF0DD7B50E262286215F1F6CBCDD13B967AC34EA290DCE79D1DF1DF7EA268BF2FD23739DE8B14538DD77F53986916022DC1F8104A97FBD0F9D09FD4482E752ED5E0637FBA61023347075BAD2F148F077F0558036DECF98F314292A61D6904BD1349FA53DF9656DA137CB2AE9796788481464A2AF895A12B6C6491849CEC8F78BAF01FC50F049F5B5321817D242D
