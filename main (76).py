def xor_cipher(str, key):  
    key= int(input("Введите ключ"))  
    cod_str = ""  
    for letter in str:  
        cod_str += chr(ord(letter) ^ key)  
    return shifr_str  
    print("зашифрованный текст:\n", cod_strg)  
 
def xor_cipher_encrypt(str, key):  
    print("расшифрованный текст:\n", xor_cipher(cod_strg, key))  
strg = input("Введите строку для шифрации")  
key = 8  
print("ваш текст:\n", strg)  
cod_strg = xor_cipher(strg, key)  
xor_cipher_encrypt(strg, key)  
print("зашифрованный текст:\n", cod_strg)