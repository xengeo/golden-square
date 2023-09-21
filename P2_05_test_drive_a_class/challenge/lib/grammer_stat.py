


class GrammarStats:
    def __init__(self):
        self._num_checks_run = 0
        self._num_pass = 0
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if not text:
            raise Exception("Cannot verify if grammar is correct if no text is given.")
        if text[0].isupper() and text[-1] in '?!.':
            # pass
            self._num_pass += 1
            self._num_checks_run += 1
            return True
        # fail
        self._num_checks_run += 1
        return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.

        return (self._num_pass / self._num_checks_run) * 100 if self._num_checks_run else 0