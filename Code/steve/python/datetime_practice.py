from datetime import datetime


# Create Date ==================================================================
# Write a function that creates and returns a new datetime given the components

def create_date(month, day, year):
    return datetime(month, day, year)


def test_create_date():
    assert type(create_date(2021, 4, 20)) == datetime
    assert str(create_date(2021, 4, 20)) == '2021-04-20 00:00:00'


# Get Year =====================================================================
# Write a function that returns the year of a given datetime

def get_year(dt):
    return dt.year


def test_get_year():
    assert type(get_year(datetime(2021, 4, 20))) == int
    assert get_year(datetime(2021, 4, 20)) == 2021


# Parse Date ===================================================================
# Write a function that converts the given string into a datetime
# Hint: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

def parse_date(date_string):
    return datetime.strptime(date_string, '%B %d, %Y')


def test_parse_date():
    assert type(parse_date('April 20, 2021')) == datetime
    assert str(parse_date('April 20, 2021')) == '2021-04-20 00:00:00'


# # Parse Datetime ===============================================================
# # Write a function that converts a given string into a datetime
def parse_datetime(date_string):
    return datetime.strptime(date_string, '%B %d, %Y %I:%M %p')


def test_parse_datetime():
    assert type(parse_datetime('April 20, 2021 09:30 AM')) == datetime
    assert str(parse_datetime('April 20, 2021 09:30 AM')
               ) == '2021-04-20 09:30:00'

# # Format Datetime ==============================================================
# # Write a function that converts the given datetime into a string


def format_datetime(dt):
    return dt.strftime('%B %d, %Y %I:%M %p')


def test_format_datetime():
    assert type(format_datetime(datetime(2021, 4, 20, 9, 30))) == str
    assert format_datetime(datetime(2021, 4, 20, 9, 30)
                           ) == 'April 20, 2021 09:30 AM'
