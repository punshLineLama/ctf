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
When having $s_1$ and $s_2$ you can calculate $s_3$ without the knowloedge of the private key d.
$s_1 = m_1^d mod n$ $s_2 = m_2^d mod n$ $s_1*s_2 = s_3 = (m_1*m_2)^d mod n$

The rest of the work was up to my script `exploit.py` returning the flag:

`WPI{m411e4b1e_cipher5_4re_d4ngerou5}`

Knowing the procedure, this challenge was pretty straight forward.
It was a nice example of a textbook vulnerability.