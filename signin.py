__author__ = 'Alec Vercruysse'
import sys
import datetime
import time
import _thread
import threading

advocate_email = "alec.vercruysse@menloschool.org"
pwd_file = "pwd.txt"


def send_email(people_checked_in, total_people):
    print("sending email")


def daily_loop(uid_pairs):
    people_checked_in = {}
    date_today = datetime.date.today()
    email_sent = False
    while datetime.date.today() == date_today:
        if time.localtime().tm_hour < 15:
            scan = raw_input_with_timeout()
            if scan is not None and scan in uid_pairs:
                    people_checked_in.add(uid_pairs[scan])
        elif not email_sent:
            send_email(people_checked_in, [name for uid, name in uid_pairs])
        else:
            continue


def raw_input_with_timeout(prompt, timeout=30.0):
    """
    Uses threading. taken from
    https://gist.github.com/atupal/5865214
    updated with 2to3
    :param prompt:
    :param timeout:
    :return:
    """
    timer = threading.Timer(timeout, _thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return astring


def setup_attendance(population):
    """
    First time setup
    :param population: list of names of attendees
    :return: set: key = uid, val = name
    """
    uid_pairs = {}
    for attendee in population:
        print(str(attendee) + ": please scan chip")
        uid = sys.stdin.readline()
        uid_pairs[uid] = attendee
    return uid_pairs

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("fetching name list from " + str(sys.argv[1]))
    else:
        print("err: no name file specified")
        quit()
    names = open(sys.argv[1]).readLines()
    uid_pairs = setup_attendance(names)
    while True:
        daily_loop(uid_pairs)