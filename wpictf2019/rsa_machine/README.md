rsa machine
===============

The Challenge
------------------

This challenge gave 250 points and had 35 solves.

The challenge description said: `nc rsamachine.wpictf.xyz 31337 (or 31338 or 31339)`.
Additionally a python script was given: `rsa_machine_public.py`

Analyzing the script, it became clear that we need to send `getflag` with a valid signature.

I noticed in this line: `(signature,) = privkey.sign(param, None)`, 
that a given string is signed and not the hash of it. 

This is the vulnerability which allows exitential forgery.
When having:
s<sub>1</sub> and s<sub>2</sub> you can calculate s<sub>3</sub> without the knowloedge of the private key `d`.

s<sub>1</sub> = m<sub>1</sub><sup>d</sup> mod n s<sub>2</sub> = m<sub>2</sub><sup>d</sup> mod n
s<sub>1</sub>*s<sub>1</sub> = s<sub>1</sub> = (m<sub>1</sub>*m<sub>1</sub>)<sup>d</sup> mod n

The rest of the work was up to my script `exploit.py` returning the flag:

`WPI{m411e4b1e_cipher5_4re_d4ngerou5}`

Knowing the procedure, this challenge was pretty straight forward.
It was a nice example of a textbook vulnerability.