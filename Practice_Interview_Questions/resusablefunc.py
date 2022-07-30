def emails(email):
    emails = {
        "Bot's Email": "no-reply@gmail.com",
        "Service Email": "customer-service@gmail.com",
        "Recipient's Email": ""
    }
    
    emails["Recipient's Email"] += email
    return emails

print(emails(input("Type Your E-Mail: ")))