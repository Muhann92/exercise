emails = ["123whatever@gmail.com","456idontcare@gmail.com","789istilldontmind@hotmail.de","forrealbruvwhatever@gmx.de"]

username = []
email_provider = []


# please fill the two lists with the data from the "emails" list. Use string slicing and methods for extracting what you need
#example:
#  test@mail.com
# usernames = ["test"]
# email_provider = ["mail.com"]






for i in emails:
    username.append(i.split('@')[0])
    email_provider.append(i.split('@') [-1])
print(str('Username_List: '), username)
print(str('Email_Provider_List: '), email_provider)
