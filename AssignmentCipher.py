import vigenereCipher
import caesarCipher
import reverseCipher

myMessage = raw_input('Enter Message   : ') 
myKey = raw_input('Enter Key   :  ') 
myMode = raw_input('e or d   :   ') 

if myMode == 'e':
	for i in range(32):
		translated = vigenereCipher.encryptMessage(myKey, myMessage)
		translated1 = caesarCipher.encryptMessage(len(myKey), translated)
		myMessage = reverseCipher.reverse(translated1)
	print myMessage

elif myMode == 'd':
	for i in range(32):		
		translated = reverseCipher.reverse(myMessage)
		translated1 = caesarCipher.decryptMessage(len(myKey), translated)
		myMessage = vigenereCipher.decryptMessage(myKey, translated1)	
	print myMessage

def main(m, k, om):
	myKey = k
	myMode = om
	myMessage = m

