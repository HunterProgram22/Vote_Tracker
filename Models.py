from tkinter import StringVar, IntVar, Text


class Case(object):
    """The base class of a case."""
    def __init__ (self):
        self.case_number = StringVar()
        self.vote = IntVar()
        self.data_fields = [ ('Case Number', self.case_number),
                             ('Vote', self.vote)]
        self.vote.set(0)
        self.options = ['Accept',
                      'Decline',
                      'Hold for Conference']


    def input_vote(self, vote):
        self.vote = vote

    def print_case_data(self):
        print(str(self.case_number) + " " + self.vote)

    def return_data_fields(self):
        return self.data_fields
