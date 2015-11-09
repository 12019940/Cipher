import vigenereCipher
import simpleSubCipher
import reverseCipher

myMessage = raw_input('Enter Message   : ') 
myKey = raw_input('Enter Key   :  ') 
myMode = raw_input('Encrypt or Decrypt   :   ') 

if myMode == 'Encrypt':
	for i in range(32):
		translated = vingereCipher.encryptMessage(myKey, myMessage)
		translated1 = simpleSubCipher.main(myKey, myMessage)
		translated2 = reverseCipher.main(len(myKey), myMessage)
	print 'Here it is..encrypted' % translated1

elif myMode == 'Decrypt':
	for i in range(32):
		translated = reverseCipher.main(len(myKey), myMessage)
		translated1 = simpleSubCipher.main(myKey, myMessage)
		translated2 = vingereCipher.encryptMessage(myKey, myMessage)	
	print 'Here it is..decrypted' % translated1

def main(m, k, om):
	myKey = k
	myMode = om
	myMessage = m

