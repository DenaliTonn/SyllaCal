import mailer
import openai
import conversion


# TODO: put all these hardcoded variables/api-keys in a "config" file and import/read the config file^.
openai.api_key = "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"
syllabus_directory = "syllabi"
user = 'syllacalcmsi3801@gmail.com'
app_password = 'mfdi dbwb dvbo ztru'
recipient = 'dylankrim@gmail.com'  # this is hardcoded directly in code if want to change email recipient.


ics_files = conversion.syllabus_conversion(syllabus_directory)
# TODO: error handling for if this^ fails.
mailer.ics_mailer(ics_files, user, app_password, recipient)

# TODO: delete ics_files from directory, since mailer has sent them and are no longer needed.
# ^(When you run the program and create the ics files, a copy of the ics files appear in your
# directoty, which you will see if you run the program. Delete these AFTER they are sent out.)