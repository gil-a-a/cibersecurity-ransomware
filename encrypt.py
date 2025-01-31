import os
import pyaes

#Abre o arquivo descriptografado
fileName = "file.txt"
file = open(fileName, "rb")
fileData = file.read()
file.close()

os.remove(fileName)

#Cria a chave
key = b"chaveTeste"
aes = pyaes.AESModeOfOperationCTR(key)

#Criptografa o arquivo
cryptoData = aes.encrypt(fileData)

#Salva o arquivo criptografado
newFile = fileName + ".encrypted"
newFile = open(f'{newFile}','wb')
newFile.write(cryptoData)
newFile.close()
