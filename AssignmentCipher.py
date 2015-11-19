

import vigenereCipher
import caesarCipher
import reverseCipher


def encrypt(myKey, myMessage):
	translated = vigenereCipher.encryptMessage(myKey, myMessage)
	translated1 = caesarCipher.encryptMessage(len(myKey), translated)
	myMessage = reverseCipher.reverse(translated1)
	return myMessage

def decrypt(myKey, myMessage):
	translated = reverseCipher.reverse(myMessage)
	translated1 = caesarCipher.decryptMessage(len(myKey), translated)
	myMessage = vigenereCipher.decryptMessage(myKey, translated1)	
	return myMessage

def main():
	myMessage = raw_input('Enter Message   : ') 
	myKey = raw_input('Enter First Key   :  ')
	myMode = raw_input('e or d  :   ') 

	if myMode == 'e':
		for i in range(32):
			myMessage = encrypt(myKey, myMessage)
	elif myMode == 'd':
		for i in range(32):
	 		myMessage = decrypt(myKey, myMessage)
	print myMessage


if __name__ == '__main__':
	main()
