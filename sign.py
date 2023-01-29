from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point, sign
from hashlib import sha256

import random

def sign(m):
	#generate public key
	#Your code here
	n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
	#d = random.randrange(1,n)
	key = gen_keypair(secp256k1)
	public_key = key[1]
	sig = sign(M, d, secp256k1, hashfunc=SHA256)

	#generate signature
	#Your code here
	r = sig[0]
	s = sig[1]

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )


