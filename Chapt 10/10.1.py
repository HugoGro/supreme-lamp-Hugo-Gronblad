s = input('skriv ett tal')
for e in s:
    if  '0' <= e <= '9':
        print('talet är okej')
    else:
        print('talet är inte okej')
        break