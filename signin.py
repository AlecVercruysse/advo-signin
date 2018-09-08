__author__ = 'Alec Vercruysse'
import sys
import datetime
import time
import _thread
import threading
import smtplib
from email.mime.text import MIMEText

advocate_email = "alec.vercruysse@menloschool.org"
pwd_file = "pwd.txt"


def send_email(people_checked_in, total_people, date):
    print("sending email")
    msg = "Hello, \n\n It looks like " + str(len(people_checked_in)) + " people checked in today. \n\nAttendance:\n\n"
    for person in total_people:
        msg += str(person) + ":\t" + ("PRESENT" if person in people_checked_in else "ABSENT") + "\n"
    msg = MIMEText(msg)
    msg['Subject'] = "Attendance: " + str(date)
    bot_email_info = open(pwd_file, "r").readlines()
    msg['From'] = bot_email_info[0]
    msg['To'] = advocate_email
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(bot_email_info[0], bot_email_info[1])
        server.sendmail(bot_email_info[0], advocate_email, msg.as_string())
        server.close()
        print("email successfully sent")
    except:
        print("failed to send mail")


def daily_loop(uid_pairs):
    people_checked_in = set()
    date_today = datetime.date.today()
    email_sent = False
    while datetime.date.today() == date_today:
        if time.localtime().tm_hour < 23:
            scan = raw_input_with_timeout()
            if scan == "send_mail": #DEBUGGING
                send_email(people_checked_in, [name for uid, name in uid_pairs.items()], datetime.date.today())
            if scan is not None and scan in uid_pairs:
                    people_checked_in.add(uid_pairs[scan])
                    print(str(uid_pairs[scan]) + " checked in.")
        elif not email_sent and len(people_checked_in) != 0:
            send_email(people_checked_in, [name for uid, name in uid_pairs.items()], datetime.date.today())
            email_sent = True
        else:
            continue


def raw_input_with_timeout(timeout=30.0):
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
        astring = input()
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
        uid_pairs[uid.rstrip()] = attendee.rstrip()
    print("Setup done. Starting bot.\nRecipient: " + str(advocate_email))
    return uid_pairs


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("fetching name list from " + str(sys.argv[1]))
    else:
        print("err: no name file specified")
        quit()
    names = open(sys.argv[1], "r").readlines()
    uid_pairs = setup_attendance(names)
    while True:
        daily_loop(uid_pairs)
