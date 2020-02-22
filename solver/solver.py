import globals.globals as GLOBALS
global GLOBALS


class Solver:

    @staticmethod
    def solve(output_file_name):
        days_remaining = GLOBALS.TOTAL_DAYS
        signed_up_libraries = 0
        file = open(output_file_name, 'w+')
        file.write(" " + "\n")
        exhausted = 0
        while days_remaining > 0 and exhausted < GLOBALS.TOTAL_LIBRARIES:

            for library in GLOBALS.LIBRARIES:

                if library.signup_days < days_remaining:
                    days_remaining -= library.signup_days
                    signed_up_libraries += 1
                    books_scanned = 0
                    scanned = []
                    for b_id in library.book_ids:

                        if GLOBALS.BOOKS_SCANNED[b_id.index] == 0:
                            GLOBALS.BOOKS_SCANNED[b_id.index] = 1
                            books_scanned += 1
                            scanned.append(b_id.index)
                    if books_scanned == 0:
                        days_remaining += library.signup_days
                        signed_up_libraries -= 1
                    else:
                        file.write(
                            '{} {}'.format(library.index, books_scanned)+"\n")
                        file.write(' '.join([str(_) for _ in scanned])+"\n")
                exhausted += 1
        file.close()
        file = open(output_file_name, 'a+')
        file.seek(0, 0)
        file.write(" -- \n\n")
        file.seek(0, 0)
        file.write(str(signed_up_libraries).rstrip("\n"))
        file.close()

    @staticmethod
    def read_file(file_name):
        return open(file_name, 'r')
