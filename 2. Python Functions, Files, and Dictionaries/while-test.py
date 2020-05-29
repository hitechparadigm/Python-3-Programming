import os
while True:
    app = input('Please enter Application Name: ')
    if app == 'quit':
        print('I am done')
        break
    else:
        os.system(app)
        