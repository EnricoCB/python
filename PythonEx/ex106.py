def ajuda():
    while True:
        introdução = 'Sistema de ajuda PyHELP'
        c = len(introdução) + 4
        print('\033[0;32m~' * c)
        print(f'  {introdução}  ')
        print('~' * c)
        msg = str(input('\033[mFunção ou Biblioteca: '))
        
        
        if msg == 'fim':
            msg = 'até logo'
            c = len(msg) + 4
            print('\033[0;31m~' * c)
            print(f'  {msg}  ')
            print('~' * c)
            print('\033[m')
            break
        
        
        msg2 = 'Acessando o manual do comando ' + msg
        c2 = len(msg2) + 4
        print('\033[0;34m~' * c2)
        print(f'  {msg2}  ')
        print('~' * c2)
        print('\033[m')
        print('\033[0;35m')
        help(msg)
        print('\033[m')

ajuda()