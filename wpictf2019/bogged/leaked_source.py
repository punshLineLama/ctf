import hashlib

secret = ""

def generate_command_token(command, secret):
    hashed = hashlib.sha1(secret+command).hexdigest() 
    return hashed

def validate_input(command, token_in):
    token = hash_command(command, secret)

    if token == token_in:
        return True
    else:
        return False

while(True):
    print("Command:")
    command = raw_input(">>>")
    print(command)
    print('Auth token:')
    token = raw_input(">>>")
    print
    if validate_input(command, token) == False:
        print("Error: Auth token does not match provided command..")
    else:
        execute_command(command)
    print 
