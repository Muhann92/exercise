import re  # import the regular expression library


text_to_be_searched = """"Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""
text2 = "lol"

pattern = r"([\w]+?@[\w]+\.[a-z]+)"  # the actual regular expression (r stands for raw string)
pattern2 = r"\w{4}"

x = "\n".join(re.findall(pattern,text_to_be_searched))

y = re.sub(pattern2,"lol",text_to_be_searched)

print(f'Email_list:\n{x} Words:\n{y}')  # printing out the match





