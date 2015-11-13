import vigenereCipher
import caesarCipher
import reverseCipher

myMessage = raw_input('Enter Message   : ') 
myKey = raw_input('Enter First Key   :  ')
myKey1 = raw_input('Enter Second Key   :  ')  
myMode = raw_input('E or D  :   ') 

if myMode == 'E':
	for i in range(32):
		translated = vigenereCipher.encryptMessage(myKey, myMessage)
		translated1 = caesarCipher.encryptMessage(len(myKey1), translated)
		myMessage = reverseCipher.reverse(translated1)
	print myMessage

elif myMode == 'D':
	for i in range(32):		
		translated = reverseCipher.reverse(myMessage)
		translated1 = caesarCipher.decryptMessage(len(myKey1), translated)
		myMessage = vigenereCipher.decryptMessage(myKey, translated1)	
	print myMessage

def main(m, k, om. k1):
	myKey = k
	myKey1 = k1
	myMode = om
	myMessage = m


