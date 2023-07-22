
def main():
    print("Welcome to my email slicer")
    email = input("Enter your email address:")

    (username,domain) = email.split("@")
    (domain,extension) = domain.split(".")

    print("name:", username)
    print("domain:", domain)
    print("extension:", extension)
    
main()