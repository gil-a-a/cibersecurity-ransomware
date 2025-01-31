import os
import pyaes

#Abre o arquivo criptografado
fileName = "file.txt.encrypted"
file = open(fileName, "rb")
fileData = file.read()
file.close()

#Descriptografa
key = b"chaveTeste"
aes = pyaes.AESModeOfOperationCTR(key)
decryptData = aes.decrypt(fileData)

#Remove o arquivo criptografado
os.remove(fileName)

#Cria o descriptografado
newFile = "file.txt"
newFile = open(f'{newFile}', "wb")
newFile.write(decryptData)
newFile.close()
