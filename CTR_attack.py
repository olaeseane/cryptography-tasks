'''
К письму с текстом "Направляю пароль от моего аккаунта в банке. Расписку картинкой" приложено два зашифрованных файла: 
MyPassword.txt.encrypted и Note.bmp.encrypted. Нужно восстановить пароль.
'''

encrypted_file1 = './MyPassword.txt.encrypted'
encrypted_file2 = './Note.bmp.encrypted'
bmp_file = './picture.bmp'

with open(encrypted_file1, 'rb') as f:
    content_MyPassword = f.read(54)

with open(encrypted_file2, 'rb') as f:
    content_Note = f.read(54)

with open(bmp_file, 'rb') as f:
    content_bmp = f.read(54)

for i in range(len(content_MyPassword)-1):
    print(chr(int(content_MyPassword[i]) ^ int(
        content_Note[i]) ^ int(content_bmp[i])), end='')
