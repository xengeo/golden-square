# File: lib/diary.py

from lib.diary_entry import DiaryEntry

class Diary:

    def __init__(self):
        self._diary_entries = []


    def add_entry(self, entry) -> None:
        """        
        Parameters: entry: an instance of DiaryEntry
        Returns:    Nothing
        Side-effects:   Adds the entry to the entries list
        """
        if not isinstance(entry, DiaryEntry):
            raise Exception("Entry must be DiaryEntry object")
        
        self._diary_entries.append(entry)


    def list_all_entries(self) -> list:
        """Returns: A list of instances of DiaryEntry"""
        return self._diary_entries


    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        if minutes == 0:
            raise Exception("Minutes can't be 0")
        for entry in self._diary_entries:
            if entry.reading_time(wpm) <= minutes:
                return entry


    def list_all_contacts(self):
        """
        For each diary entry, retreive the names and their respective phone numbers
        Returns: a user friendly message of contacts
        """
        contacts = []

        for entry in self.list_all_entries():
            for contact in entry.list_contacts():
                contacts.append(contact.format())

        contacts_formatted = '\n'.join(contacts)
        
        return f"All contacts:\n{contacts_formatted}"
        

    def list_all_tasks(self):
        """
        For each diary entry, retreive the task and its respective completion status
        Returns: a user friendly message of tasks
        """
        tasks = []

        for entry in self.list_all_entries():
            for my_task in entry.list_tasks():
                tasks.append(f"{my_task.task}")


        tasks_formatted = '\n'.join(tasks)
        return f"All tasks:\n{tasks_formatted}"

        
            
