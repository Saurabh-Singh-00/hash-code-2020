from os import path
import globals.globals as GLOBALS
from classes.library import Library, Book
from solver.solver import Solver

global GLOBALS


def path_(_root, _file):
    return path.join(_root, _file)


if __name__ == "__main__":    
    GLOBALS.BOOKS_SCANNED = [0 for _ in range(100009)]

    # Change this below variable accroding to the test case, range [0-5].
    scan_file = 5
    with Solver.read_file(path_(GLOBALS.INPUT_FOLDER_NAME, GLOBALS.FILES[scan_file])) as file:

        GLOBALS.TOTAL_BOOKS, GLOBALS.TOTAL_LIBRARIES, GLOBALS.TOTAL_DAYS = list(
            map(int, file.readline().split(' ')))

        GLOBALS.BOOK_SCORE = list(map(int, file.readline().split(' ')))

        for _ in range(GLOBALS.TOTAL_LIBRARIES):
            book, signup, scan = list(map(int, file.readline().split(' ')))
            book_ids = list(map(int, file.readline().split(' ')))
            books = []
            for i in range(book):
                books.append(Book(book_ids[i], GLOBALS.BOOK_SCORE[i]))
            GLOBALS.LIBRARIES.append(Library(
                books_count=book, signup_days=signup, scans_per_day=scan, book_ids=books, index=_))

    GLOBALS.LIBRARIES.sort(reverse=True)
    Solver.solve(path_(GLOBALS.OUTPUT_FOLDER_NAME,
                       GLOBALS.FILES[scan_file]))
