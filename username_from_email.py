def get_usernames_from_email(emails: list) -> list:
    """
    Return usernames from multiple email addresses.
    """
    return [username.split("@")[0] for username in emails]


def return_username(email: str) -> str:
    """
    Return username from email address.
    """
    return email.split("@")[0]


if __name__ == "__main__":
    email = "agyapong.louis@gmail.com"
    print(email.split("@")[0])
    emails = [
        "user@org.com",
        "agyapong.louis@gmail.com",
        "py@mail.com",
        "zion.agyapong@gmail.com",
    ]
    usernames = get_usernames_from_email(emails)
    print(usernames)

    x = input("Enter email: ")
    print(return_username(x))
