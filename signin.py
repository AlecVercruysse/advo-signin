__author__ = 'Alec Vercruysse'
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("fetching name list from " + str(sys.argv[1]))
    else:
        print("err: no name file specified")
        quit()
    while true:
        main_loop()


def main_loop():
    return


def input_recieved(uid):
    '''

    :param uid: int with unique identifier per person
    :return:
    '''


def get_chip_input():
    '''
    Wait until there is a input with a uid
    :return: uid
    '''


def setup_attendance(population):
    '''

    :param population: list of names of attendees
    :return: set: key = uid, val = name
    '''
    uid_pairs = {}
    for attendee in population:
        print(str(attendee) + ": please scan chip")
        uid = get_chip_input()
        uid_pairs[uid] = attendee
    return uid_pairs