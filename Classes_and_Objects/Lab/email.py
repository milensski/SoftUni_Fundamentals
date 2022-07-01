class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


emails = []

while True:
    command = input().split()

    if command[0] == "Stop":
        break

    sender = command[0]
    receiver = command[1]
    content = command[2]

    email = Email(sender, receiver, content)

    emails.append(email)

# send_emails = list(map(lambda x: int(x), input().split(", ")))

[emails[int(x)].send() for x in input().split(", ")]

# for digit in send_emails:
#     emails[digit].send()

for email in emails:
    email.get_info()
