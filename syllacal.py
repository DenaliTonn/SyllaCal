import mailer
import openai
import conversion
import os
import config

openai.api_key = config.openai_api_key
syllabus_directory = config.syllabus_directory
user = config.user
app_password = config.app_password
recipient = input("Enter your email address: ")

try:
    ics_files = conversion.syllabus_conversion(syllabus_directory)
    mailer.ics_mailer(ics_files, user, app_password, recipient)

    for file in ics_files:
        os.remove(file)

except Exception as e:
    print(f"Error occurred: {e}")