import datetime

#Give a format date for a recibed date 
class DateFormat():

    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date, "%d/%m/%Y")