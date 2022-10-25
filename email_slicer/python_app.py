# collect email from user
# splite the mail using the @, the first part as the user name, the second part is gonna be saved as domain
# split domain using ., 
# hello@codewithtomi.com

from distutils import extension


def main():
    print(" Welocme to the email slicer")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


while True: 
    main()

    

