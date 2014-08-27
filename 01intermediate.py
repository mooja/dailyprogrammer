from datetime import datetime, timedelta
import random



class Event(object):
    def __init__(self, dt, title):
        self.dt = dt
        self.title = title

    def __str__(self):
        return "<{} on {}".format(self.title, self.dt)

class Schedule(object):
    def __init__(self):
        self.num_events = 0
        self.events = {}

    def add_event(self, event):
        self.events[self.num_events] = event
        self.num_events = self.num_events + 1

    def remove_event(self, event_id):
        del self.events[event_id]

def display_events(sched):
    if not sched.events.keys():
        print "No events currently schedueled"
        return False

    for id, event in sched.events.iteritems():
        date = "{0:<5}".format(str(event.dt.date()))
        time = "{0:%H:%M%S}".format(event.dt.time())
        print "ID: {0:>2} {1} | {2} | {3}".format(id, time, date, event.title)


def display_menu():
    print "1: View the schedule"
    print "2: Add an Event"
    print "3: Remove an event"
    print "4: Exit"


def ask_for_action():
    choice = raw_input("Action: ")
    return int(choice)

def ask_add_event():
    date_string = raw_input("Please enter date in 'YEAR MONTH DAY' format: ")
    time_string = raw_input("Please enter time in '23:13' format: ")
    title = raw_input("Please enter title: ")

    dt = datetime.strptime(date_string + " " + time_string, "%Y %m %d %H:%M")

    return Event(dt, title)

def ask_remove_event():
    remove_id = raw_input("Enter event id to remove: ")
    return int(remove_id)


def menu_loop(schedule):
    choice = None
    while not choice == 4:
        display_menu()
        choice = ask_for_action()
        if choice == 1:
            display_events(schedule)
        elif choice == 2:
            e = ask_add_event()
            schedule.add_event(e)
        elif choice == 3:
            rem_id = ask_remove_event()
            schedule.remove_event(rem_id)
        else:
            print "Exiting."

if __name__ == '__main__':
    sched = Schedule()

    # create some events
    for i in range(10):
        td = timedelta(days=random.randint(0, 10), hours=random.randint(0, 23))
        title = "My birthday number {0}!".format(i)
        e = Event(datetime.today()+td, title)
        sched.add_event(e)

    menu_loop(sched)
