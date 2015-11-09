import vigenereCipher
import caesarCipher
import reverseCipher

myMessage = raw_input('Enter Message   : ') 
myKey = raw_input('Enter Key   :  ') 
myMode = raw_input('E or D   :   ') 

if myMode == 'E':
	for i in range(64):
		translated = vigenereCipher.encryptMessage(myKey, myMessage)
		translated1 = caesarCipher.encryptMessage(len(myKey), translated)
		myMessage = reverseCipher.reverse(translated1)
	print myMessage

elif myMode == 'D':
	for i in range(64):		
		translated = reverseCipher.reverse(myMessage)
		translated1 = caesarCipher.decryptMessage(len(myKey), translated)
		myMessage = vigenereCipher.decryptMessage(myKey, translated1)	
	print myMessage

def main(m, k, om):
	myKey = k
	myMode = om
	myMessage = m

