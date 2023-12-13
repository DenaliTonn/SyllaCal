import yagmail


def ics_mailer(file_name, user, app_password, recipient):
    # If passed ics file(s), compose details of email that will send file(s) to recipient
    if file_name:
        subject = 'Syllabus'
        body = ['Hello!', 'Click the ics files attached to this email to add important dates from your syllabuses to your calendar. We suggest creating a new calendar for each course file you add to help with organization.', 'Thank you for using SyllaCal!']
        try:
            # Connect to SMTP server and send the email with attachments
            with yagmail.SMTP(user, app_password) as yag:
                yag.send(recipient, subject, body, file_name)
                print(f'SyllaCal successfully sent {recipient} an email!')
        except Exception as e:
            # Handle exceptions if there is an error sending the email
            print('Error sending email')
    else: 
        print('No files found to send. No email sent.')