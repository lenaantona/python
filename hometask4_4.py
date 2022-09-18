# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево 
# или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" -
# сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
# которая спрашивает ключ, считывает текст и дешифровывает его.
text = input('Введите текст для шифрования: ')
new_kod = int(input('Введите код шифрования: '))

def encryption_text(input_text, kod1):
   '''
   функция шифрования
   '''
   new_text = ''
   for i in input_text:
      s = ord(i)
      s = s + kod1
      new_text += chr(s)
   print('Шифрование текста выполнено')

   with open('text_shifr.txt', 'w', encoding="utf-8") as f1:
      f1.write(new_text)
      print('Шифрованный текст заненсен в файл text_shifr.txt')

encryption_text(text, new_kod)

def decryption_text(kod1):
   '''
   функция дешифрует текст из файла
   '''
   new_text = ''
   kod = int(input('Введите ключ для расшифровки, целое число: '))
   if kod == kod1:
      with open('text_shifr.txt', 'r', encoding="utf-8") as f:
         input_text = f.read()
         print('Зашифрованный текс: '+ input_text)
         for i in input_text:
            s = ord(i)
            s = s - kod 
            new_text += chr(s)
      print('Текст расшифрованный: '+ new_text) 
   else:
      print('Введен неверный ключ')
      decryption_text()

decryption_text(new_kod)


   