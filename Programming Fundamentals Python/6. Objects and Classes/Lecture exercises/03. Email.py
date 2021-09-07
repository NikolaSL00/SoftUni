# Create class Email. The __init__ method should receive sender, receiver and a content.
# It should also have a default set to False attribute called is_sent.
# The class should have two additional methods:

# ⦁	send() - sets the is_sent attribute to True
# ⦁	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by single space) until you receive the command "Stop".
# The first element will be the sender, the second one – the receiver and the third one – the content.
# On the final line you will be given the indices of the sent emails separated by comma and space ", ".

# Call the send() method for the given indices of emails. For each email call the get_info() method.

# Note: submit all of your code including the class

# INPUT:
# Peter John Hi,John
# John Peter Hi,Peter!
# Katy Lilly Hello,Lilly
# Stop
# 0, 2

# EXPECTED OUTPUT:
# Peter says to John: Hi,John. Sent: True
# John says to Peter: Hi,Peter!. Sent: False
# Katy says to Lilly: Hello,Lilly. Sent: True


class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


new_email_line = input()
all_mails = []

while new_email_line != "Stop":
    sender, receiver, content = new_email_line.split()
    new_mail = Email(sender, receiver, content)
    all_mails.append(new_mail)
    new_email_line = input()

indexes = [int(el) for el in input().split(", ")]

for index in indexes:
    all_mails[index].send()

for mail in all_mails:
    print(mail.get_info())
