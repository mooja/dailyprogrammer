import getpass

from ConfigParser import SafeConfigParser


def get_login_credentials():
    username = raw_input("Please enter your username: ")
    password = getpass.getpass(prompt="Please enter your password: ")

    return (username, password)


def get_password(username):
    parser = SafeConfigParser()
    parser.read("simplepasswords.ini")
    return parser.get(username, 'password')


def main():
    while True:
        username, password = get_login_credentials()
        if get_password(username) == password:
            print "You are authorized!"
            return
        print "Wrong login/password!"


if __name__ == '__main__':
    main()
