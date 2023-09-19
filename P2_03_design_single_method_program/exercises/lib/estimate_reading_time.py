# File: lib/estimate_reading_time.py


def estimate_reading_time(text):
    """Returns time taken to read text"""
    read_speed = 1/200
    if not text:
        raise Exception("Cannot give estimate of reading time if no text is given.")
    reading_time = len(text.split()) * read_speed
    return f"This text will take {reading_time} mins to read"