<h2>Cictrohash</h2>

<p><h5> The Task </h5> This challenge was about implementing a hash function and finding a collision. <br>
In the CictroHash.pdf you can see how the hashfunction was supposed to be implemented.
The input is of arbitrary length and the digest is 4 bytes long. 
Thus there are 2^32 possible hashvalues. Thanks to the birthday paradox (https://en.wikipedia.org/wiki/Birthday_problem), finding a collision should not be too hard. <br>
<h5> The implementation </h5>
The hash.py file calculates the Cictro hashalue of a given input.
The findCollision.py script then creates a wordlist and tries to find collisions within that wordist.
If a collision is found, both preimages are printed. <br>

<h5>Find the collision</h5>
After running the script, I found a collision caused by the preimages "AP" and "PA" (without the quotes).
<h5>Getting the flag</h5>
Then I submitted them to the gameserver as described in the challenge description: <br>
curl -X POST http://fun.ritsec.club:8003/checkCollision --header "Content-Type: application/json" --data '{"str1": "AP", "str2": "PA"}'
 <br>
And the flag comes back: RITSEC{I_am_th3_gr3@t3st_h@XOR_3v@}

<h5>Final Thought</h5>
This was a really fun challenge. As I am pretty new to CTFs I have not seen a similar challenge before. 
Thanks to the Author of the challenge and the CTF organizers.
