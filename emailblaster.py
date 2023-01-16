import csv
import smtplib
import ssl

file = input("Enter a file path: ")

# send email
port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    sender_email = "emails.tedxcmu@gmail.com"
    subject = "TEDxCMU Sponsorship Request"
    server.login(sender_email, password)

    # Open and read CSV file, send an email!
    with open(file) as CSVfile:
        readCSV = csv.reader(CSVfile, delimiter=',')
        next(readCSV)

        # column indices can be edited based on the csv file we feed in
        for row in readCSV:  # For each entry
            name = row[0]  # Change this as necessary
            email1 = row[1]  # Change this as necessary
            email2 = row[2]  # Change this as necessary
            personal_message = row[3]  # Change this as necessary

            message = f"add message here: {personal_message}"
            # print(message) # for testing

            sendmail_input = input(f"Send email to {email1}, {email2}? (y/n): ")
            if sendmail_input.lower() == "y":
                server.sendmail(sender_email, email1, message, subject)  # send to email1
                server.sendmail(sender_email, email2, message, subject)  # send to email2

    print("Successfully sent all emails.\n")
