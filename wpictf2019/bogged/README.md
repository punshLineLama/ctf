bogged
===============

The Challenge
---------------

This challenge gave 150 points and had 23 solves.

The challenge description said: 

```

Two strange men called me last night. They call themselves the Bogdanoff twins. I don't know much about cryptocurrency- can you help them with their scheme?

nc bogged.wpictf.xyz 31337 (or 31338 or 31339)

made by rm -k

https://soundcloud.com/nanosmusics/one?in=nanosmusics/sets/p-o-r-n-o
```

Additionally a python script was given: `leaked_source.py`

When connection via nc we are given the following prompt:

```

BOGDANOFF:

Bonjour... 
We have access to the Binance backdoor, and got you into a compromised teller station.
We need you to steal tethered cryptocurrency from people's wallets.
We were halted by an unfortunate countermeasure in the teller system, but we have an account ready to recieve the stolen crypto.

Steal the currency from cryptowojak123. Transfer it to not_b0gdan0ff. 

Transfer everything... then we will kill him, and find another.

Do not fail us. 









Welcome to the Binance Teller Terminal!
Please remember to use admin-issued auth tokens with each account transfer!

Either enter a command or one of the following keywords:

accounts: List of accounts currently on the system.
history: A history of prior terminal commands.
help: A reminder on how to use this terminal.
```

The History command gives us:

```

Command:
history

///// TRANSACTION HISTORY //////////////////////////

Command:
withdraw john.doe
Auth token:
b4c967e157fad98060ebbf24135bfdb5a73f14dc
Action successful!

Command:
withdraw john.doe;deposit xXwaltonchaingangXx
Auth token:
455705a6756fb014a4cba2aa0652779008e36878
Action successful!

Command:
withdraw cryptowojak123;deposit xXwaltonchaingangXx
Auth token:
e429ffbfe7cabd62bda3589576d8717aaf3f663f
Action successful!

Command:
withdraw john.doe
Auth token:
b4c967e157fad98060ebbf24135bfdb5a73f14dc
Action successful!

////////////////////////////////////////////////////
```

* Note:
Command can be concatenated in an arbitrary way.

The accounts command gives us:

```
Command:
accounts

cryptowojak123
sminem.1337
xXwaltonchaingangXx
john.doe
not_b0gdan0ff

```

When taking a look at the `leaked_source.py`.
We notice that the sha1 hash algorithm is used and that the secret is concatenated with the command to generate the token:

`hashed = hashlib.sha1(secret+command).hexdigest() `

We found online a tool called `hlextend` which executes a length-extension-attack.
Using this tool, we only needed to "brute-force" the length of the secret to get a valid hash for an extended command.
The extended command will then be something like:
`withdraw cryptowojak123;deposit xXwaltonchaingangXx\x80\x00\x00\x00\x00\x00\x00\x00\x00\xa8;withdraw cryptowojak123;deposit not_b0gdan0ff`

The rest was up to the `exploit.py` script.
After trying several length, the script gave out the flag, which was:
`WPI{duMp_33t_aNd_g@rn33sh_H1$_wAg3$}`

As none of our team members was aware of this kind of attack, we spend a great deal of the time googling the problem.
When we found the right type of attack, the solution was not too hard to implement.

A lot of credit goes to Eric for solving this challenge.

