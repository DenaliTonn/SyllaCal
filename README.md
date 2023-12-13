# SyllaCal
(The original proposal can be found in the proposal.txt file)
## Project Description:
  Our proposed application aims to streamline the process of converting important dates in syllabuses into personalized calendars. Our idea will revolutionize the academic field by integrating user-friendly features to allow students to effortlessly input syllabus data that include things like exam schedules, due dates, and office hours into a comprehensive calendar. The program takes each syllabus included in the syllabi directory and will automatically send an email with attachments holding the important dates for each syllabus that you can click to instantly create a personalized calendar view of your courses in seconds. By effortlessly creating a visual timeline of events, students save countless hours of scheduling and organizing, as they gain easier access to managing their daily lives and ensure that they will never miss a deadline again.

## Feature Specification:
 - Calendar Generation:
    - SyllaCal allows users to run python code locally for as many syllabi pdfs as they want.
    - The program will then take each pdf and convert it to text in order for AI to analyze it for important dates that can be turned into ics calendar events, such as office hours, test dates, class times, and more.
    - The ics code output from each AI generated response will be turned into an ics file.
    - All of the ics files will then be mailed to a recipient as email attachments.
    - This allows users to easily click the attachment for each syllabus, and instantly add the important dates from that course into their local calendar.

  SyllaCal aims to simplify the academic lives of students by providing a comprehensive, user-friendly solution for managing course schedules, enhancing organization, and ultimately improving academic performance.

## Technical Specification:
We will be designing/building this app using Python. The host who runs the SyllaCal program locally has to be on a Mac due to the use of poppler. Although the final email result can be sent to any user on any machine type, we found the ics intigration from email attachment to Calendar works most seemlessly with Apple Calendar, so we suggest the end user be on a Mac as well. 

## Prerequisites:
   From a from a Mac/linux environment, you will need have the following installed in order to run this program locally:
   - python (ex: brew install python)
   - poppler (ex: brew install poppler)
   - pdf2image (ex: python3 -m pip install pdf2image)
   - pytesseract (ex: python3 -m pip install pytesseract)
   - openai (ex. python3 -m pip install openai==0.28) 
   - yagmail (ex. python3 -m pip install yagmail)

## How to Run:
   - Open the config file and change the receipient variable to whatever email you want the code to send the final output of ics files to (likely your own email). Save the file after making this update.
   - Run the syllacal.py file and watch as the terminal gives you updates about what step the program is on.
   - Once the program writes that it has successfully sent you an email, go to you email and open said email. (Ignore any Google Calendar shortcuts if that pops up on the email, as this program works best with Apple Calendar).
   - Download each attachment one at a time. After each single ics download, repeat the following steps: 
      - Opening the download will create an "add event" pop up for your local Calendar on your homescreen. (If you get a "importing calendar data" pop up as well, just ignore it.)
      - We suggest clicking the drop down and selecting "new calendar" for each syllabus you add for organization. Then click "okay" and watch your calendar be filled with syllabus dates! 
      - Repeat for next ics file until all ics files have been added to your calendar.
   - Now you will see your syllabus's calendar dates displayed on your calendar! (Make sure your desired calendar(s) is/are being displayed using the checkboxes on the left column of the Calendar)
