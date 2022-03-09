def get_usernames_from_email(emails):
    """
    Return usernames from multiple email addresses.
    """
    return [username.split("@")[0] for username in emails]


if __name__ == "__main__":
    email = "agyapong.louis@gmail.com"
    emails = [
        "user@org.com",
        "agyapong.louis@gmail.com",
        "py@mail.com",
        "zion.agyapong@gmail.com",
    ]
    usernames = get_usernames_from_email(emails)
    print(usernames)
