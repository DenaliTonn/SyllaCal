class ICSConverter:
    def convert(self, json_data):
        template = 'BEGIN:VCALENDAR\n'
        template += 'VERSION:2.0\n'
        template += 'PRODID:-//Example Corp.//CalDAV Client//EN\n'

        for event in json_data.get('important_event_dates', []):
            template += self.convert_event(event, 'IMPORTANT')

        for event in json_data.get('class_meeting_times', []):
            template += self.convert_event(event, 'CLASS')

        for office_hour in json_data.get('office_hours', []):
            template += self.convert_office_hour(office_hour)

        template += 'END:VCALENDAR\n\n'
        return template

    def convert_event(self, event, event_type):
        template = 'BEGIN:VEVENT\n'

        # Check if 'event' and 'date' keys exist in the event dictionary
        event_name = event.get('event', 'N/A')
        event_date = event.get('date', 'N/A')

        template += 'SUMMARY:%s\n' % event_name
        template += 'DTSTART:%s\n' % event_date
        template += 'DTEND:%s\n' % event_date

        # Check if 'location' key exists in the event dictionary
        location = event.get('location', 'N/A')

        template += 'LOCATION:%s\n' % location
        template += 'DESCRIPTION:%s %s\n' % (event_type, event_name)
        template += 'END:VEVENT\n\n'
        return template

    def convert_office_hour(self, office_hour):
        template = 'BEGIN:VEVENT\n'
        template += 'SUMMARY:Office Hours\n'
        template += 'DTSTART:%s\n' % self.combine_date_time(office_hour['day'], office_hour['start_time'])
        template += 'DTEND:%s\n' % self.combine_date_time(office_hour['day'], office_hour['end_time'])
        template += 'LOCATION:%s\n' % office_hour['location']
        template += 'DESCRIPTION:Office Hours\n'
        template += 'URL:%s\n' % office_hour['zoom_link']
        template += 'END:VEVENT\n\n'
        return template

    def combine_date_time(self, date, time):
        return f"{date}T{self.convert_time_format(time)}"

    def convert_time_format(self, time):
        return time.replace('pm', 'PM').replace('am', 'AM')

    def save_to_file(self, ics_template, file_path='output.ics'):
        with open(file_path, 'w') as file:
            file.write(ics_template)
        return file_path

    def generate_and_save_ics(self, json_data, file_path='output.ics'):
        ics_template = self.convert(json_data)
        output_file_path = self.save_to_file(ics_template, file_path)
        return output_file_path
