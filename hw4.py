def rep_char(c, n):
    print(c*n)

def welcome_msg(name):
    
    msg1 = f'Hello + {name}'
    msg2 = 'Welcome to Seoul. '

    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

    rep_char('-', nstr + 1)
    print(f' Hello {name},\n Welcome to Seoul.')
    rep_char('-', nstr + 1)



welcome_msg(input('Input his/her name:'))
