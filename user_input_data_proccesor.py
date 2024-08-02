

def name_check():
    name = input("Please enter your first and last name:")
    first_name = name.split()[0]
    last_name = name.split()[1]
    if len(first_name) < 2 or len(last_name) < 2:
        print('Please make sure that your first and last name are both longer than 2 characters please!tim ')
    else:
        print('You are all good!')


name_check()