import openai
import pdf2image
from PIL import Image
import pytesseract
import os

# Prompt Engineering: SyllaCal configuration to directly prompt and guide AI on what we want it to do.
syllacal_preamble = 'Extract all important times and dates for the events out of this syllabus.'
prompt = 'Next I will provide the syllabus to analyze and summarize. Pay particular attention to office hours, class meeting times, exams, and important dates.'
response_format = 'Format results in ics code for Zap Calendar ical events. For classes in the fall, only include calendar dates between the months of August to January. For classes in the spring, only include calendar dates between the months of January to June. Make any frequency calendar dates only repeat until the final exam calandar date, and then stop. Note the class name for each calendar event in the summary or description. In cases of duplicate calendar events, only keep exams and completely ignore holidays.'


# Function to generate AI response using OpenAI's ChatCompletion model
def generate_response(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}],
        n=1,
        temperature=0,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    return response['choices'][0]['message']['content']


# Caroline collaborated with Denali for the following function:
# Function to convert all syllabus PDFs to iCalendar (ics) format
def syllabus_conversion(syllabus_directory):
    response_files = []
    # Iterate through each syllabus file in the specified directory of syllabi
    for syllabus in os.listdir(syllabus_directory):
        detected_text = ''
        print(f"SyllaCal is analyzing {syllabus}")

        # Check if the file is a PDF
        if syllabus.endswith(".pdf"):
            PDFfile = os.path.join(syllabus_directory, syllabus)
            try:
                # Convert PDF to images and extract text using Tesseract OCR
                image = pdf2image.convert_from_path(PDFfile)
                for pagenumber, page in enumerate(image):
                    detected_text += pytesseract.image_to_string(page)

                # Generate AI response based on configured syllabus content
                response = generate_response(
                    syllacal_preamble + " " + prompt + " " + response_format + " " + detected_text)

                # Create an output ics file and write the AI-generated response
                output_ics = f"output_{syllabus[:-4]}.ics"
                with open(output_ics, "w") as file:
                    file.write(response)
                    response_files.append(output_ics)

                print(
                    f"SyllaCal successfully pulled all the important dates from {syllabus}")
            except Exception as e:
                print(f"Error for {syllabus}" + e)
    return response_files
