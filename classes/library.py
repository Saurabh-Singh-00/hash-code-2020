import globals.globals as GLOBALS
from math import ceil
global GLOBALS


class Book:

    def __init__(self, index, score):
        self.index = index
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __repr__(self):
        return "Book({}, {})".format(self.index, self.score)


class Library:

    def __init__(self, *args, **kwargs):
        self.books_count = kwargs['books_count']
        self.signup_days = kwargs['signup_days']
        self.scans_per_day = kwargs['scans_per_day']
        self.book_ids = kwargs['book_ids']
        self.book_ids.sort(reverse=True)        
        self.throughput = 0
        self.index = kwargs['index']
        # Per day efficiency
        if GLOBALS.TOTAL_DAYS - self.signup_days > 0:
            self.throughput = sum([GLOBALS.BOOK_SCORE[_.index]
                                   for _ in self.book_ids]) / (self.signup_days + ceil(self.books_count/self.scans_per_day))

    def __lt__(self, other):
        return self.throughput < other.throughput

    def __gt__(self, other):
        return self.throughput > other.throughput

    def __eq__(self, other):
        return self.throughput == other.throughput

    def __le__(self, other):
        return self.throughput <= other.throughput

    def __ge__(self, other):
        return self.throughput >= other.throughput

    def __repr__(self):
        return "{} - Library({}, {}, {}, {})".format(self.index, self.books_count, self.signup_days, self.scans_per_day, str(self.book_ids))
