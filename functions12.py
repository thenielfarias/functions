def pyhelp():
    while True:
        title = 'HELP SYSTEM <PyHelp>'
        line1 = '-'*(len(title)+4)
        print(f'\033[1:37:46m{line1}')
        print(f'{title:^{len(line1)}}')
        print(line1)
        print(f'\033[m')
        userInput = str(input('Please enter a function or library [999 to quit] >>> '))
        if userInput == '999':
            break
        subtitle = f'Accessing manual for command \'{userInput}\''
        line2 = '-'*(len(subtitle)+len(userInput)+4)
        print(f'\033[1:37:42m{line2}')
        print(f'{subtitle:^{len(line2)}}')
        print(line2)
        print(f'\033[m')
        print(f'\033[7m')
        help(userInput)
        print(f'\033[m')   
    print(f'\033[1:37:43mEnding program...\033[m')


pyhelp()


