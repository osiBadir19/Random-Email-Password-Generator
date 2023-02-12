class RandomUser:
    """
    generate random user email, password combinations for any number required
    """
    # importing necessary modules
    import random
    import string

    def __init__(self, mail_extension: str, pass_length=7):
        self.email_ext = mail_extension
        self.pass_len = pass_length

    def email_generator(self):
        """
        generate a random email
        :return: a random email
        """
        # make a list that contains all letters in lowercase
        chars = list(self.string.ascii_lowercase)
        return "".join(self.random.sample(chars, 7))+"@"+self.email_ext


    def password_generator(self):
        """
        :return: a random password
        """
        elements = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*")
        return "".join(self.random.sample(elements, self.pass_len))


    def print_details(self, users) -> list:
        """
        :param users: a list of users email/password combinations
        :return: prints users details seprated, and a list to use for later
        """
        for user in users:
            print("\n-  -  -  -  -  -  -  -  -  -  -  -\n"
                  "user email :   {0}"
                  "\nuser password: {1}\n-  -  -  -  -  -  -  -  -  -  -  -"
                  .format(user.get('email'), user.get('password')))

        return users

    def generate_users(self, users_num: int):
        """
        :param users_num: the number of required users to generate
        :return: a list of users.
        """
        # a list to contain <dict> of user details
        users = []
        for x in range(users_num):
            users.append({'email': self.email_generator(),
                          'password': self.password_generator()})
            continue

        # give the admin the option to print details or skip printing process
        if input("do you want to print users? Y/n\n").lower() == 'y':
            return self.print_details(users)
        else:
            return users




