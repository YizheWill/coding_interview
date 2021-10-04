# this program is used only for a coding interview at Rentgrata
# Author: Will Wang
# The program is written in Python3, so please prep python env accordingly.

# To run this app:
#   python3 solution.py username1,username2,username3
#   for example "python3 solution.py Maggie,Joe,Jordan"
# PLEASE NOTICE THAT NO SPACE IS ALLOWED BETWEEN TWO USERNAMES, JUST A ',' IS EXPECTED
# you can configure start and end hours by adding two additional args, they have to be intergers and start has to be less than end
# for example "python3 solution.py Maggie,Joe,Jordan 15 21"

# in the Solution.generate_results function, user can change the filter range
# solution.generate_results("2021-07-08", end_date="2021-07-10"):


# program will unify all inputs to be lowercase, so doesn't support FirstnameLastname yet
# Doesn't support multiple users with the same name, users with same name are deemed as same person


import sys
import json
from datetime import date as dt, timedelta as tD
from collections import defaultdict


class Solution:
    # program support configuring working hours
    def __init__(self, users, e_json, u_json, working_start='13:00:00', working_end='21:00:00'):
        # translate the json files into python hashes
        # userhash: {'mary': '1', 'john': '2'}...
        # eventhash: {'1': [{'start_time': '2021-07-02T13:00:00', 'end_time': '2021-07-02T14:00:00}, ...], '2': [{...}]}
        # print('working_start', working_start, 'working_end', working_end)

        def create_hashes(event_json, user_json):
            userhash, eventhash = defaultdict(str), defaultdict(list)
            with open(event_json) as e, open(user_json) as u:
                events = json.load(e)
                users = json.load(u)
                for user in users:
                    userhash[user['name'].lower()] = user['id']
                for event in events:
                    user_id, start_time, end_time = event['user_id'], event['start_time'], event['end_time']
                    eventhash[user_id].append(
                        {'start_time': start_time,
                            'end_time': end_time})
            return (userhash, eventhash)
        self.working_start = working_start
        self.working_end = working_end
        self.users = users
        self.userhash, self.eventhash = create_hashes(e_json, u_json)

    def print_time(self, date, start, end):
        print(date + ' ' + start[:5] + ' - ' + end[:5])

    # this function is to generate the result hash : {'2021-07-05': [], '2021-07-06': [],...}

    def create_result_hash(self, start_date, end_date):
        res = {}
        sy, sm, sd = start_date.split('-')
        sy, sm, sd = int(sy), int(sm), int(sd)
        ey, em, ed = end_date.split('-')
        ey, em, ed = int(ey), int(em), int(ed)
        start_date = dt(sy, sm, sd)
        end_date = dt(ey, em, ed)
        delta = end_date - start_date
        res = {}
        for i in range(delta.days + 1):
            day = start_date + tD(days=i)
            res[str(day)] = []
        return res

    # if ever we want to change filtering dates, we can simply make changes here
    def generate_results(self, start_date="2021-07-05", end_date="2021-07-07"):
        print('')

        res = self.create_result_hash(start_date, end_date)
        # res : {'2021-07-05': [], '2021-07-06': [], '2021-07-07': []}
        # if no events found in a date, the res[date] will be an empty array,
        # program will later make all time slots available for that date if res[date] is empty
        for user in users:
            user_id = self.userhash[user]
            timeslots = filter(
                lambda event: (
                    # making sure date in range
                    start_date <= event['start_time'].split('T')[0] <= end_date and
                    # making sure time in range
                    (self.working_start < event['end_time'].split(
                        'T')[1] < self.working_end
                     or self.working_start <= event['start_time'].split('T')[1] < self.working_end
                     or event['start_time'] <= self.working_start and event['end_time'] >= self.working_end)
                ), self.eventhash[user_id])

            # filtering out all events in the day-time period

            for timeslot in timeslots:
                date, start = timeslot['start_time'].split('T')
                end = timeslot['end_time'].split('T')[1]

                # tinker start and end time if they ever exceed the limits
                start = start if start >= self.working_start else self.working_start
                end = end if end <= self.working_end else self.working_end
                # print(start, end)
                res[date].append((start, end))
        for i in res:
            self.combine_time(i, res[i])
            print('')

    def combine_time(self, date, time_array):
        if not time_array:
            self.print_time(date, self.working_start, self.working_end)
            return
        # logics of sorting the time array, combining inter-sections, and finding the empty slots
        time_array = sorted(time_array, key=lambda x: x[0])
        prev_start = time_array[0][0]
        prev_end = time_array[0][1]

        if prev_start > self.working_start:
            self.print_time(date, self.working_start, prev_start)
        for time in time_array:
            curr_start, curr_end = time
            if curr_start > prev_end:
                self.print_time(date, prev_end, curr_start)
                prev_start, prev_end = curr_start, curr_end
            else:
                if time[1] > prev_end:
                    prev_end = time[1]
        if prev_end < self.working_end:
            self.print_time(date, prev_end, self.working_end)


if __name__ == '__main__':
    args = sys.argv
    start, end = '', ''
    if len(args) != 2 and len(args) != 4:
        print('invalid input, only accept "python3 solution.py John,Mary"(no space allowed between names) or "python3 solution.py John,Mary 13 21", start end has to be in 0-24 range')
        exit()
    if len(args) == 4:
        if args[2].isdigit() and args[3].isdigit() and int(args[2]) < int(args[3]) and int(args[2]) >= 0 and int(args[3] <= '24'):
            # format the start, end time and later pass to the Solution initializer
            start = args[2] + \
                ':00:00' if len(args[2]) == 2 else '0' + args[2] + ':00:00'
            end = args[3] + \
                ':00:00' if len(args[3]) == 2 else '0' + args[3] + ':00:00'
        else:
            print('invalid input, only accept "python3 solution.py John,Mary"(no space allowed between names) or "python3 solution.py John,Mary 13 21", start end has to be in 0-24 range')
            exit()

    users = sys.argv[1].split(',')
    users = map(lambda x: x.lower(), users)
    solution = Solution(users, './events.json', './users.json') if not start else Solution(
        users, './events.json', './users.json', start, end)
    # you can also try: solution.generate_results("2021-07-08", "2021-08-10"):
    solution.generate_results()
    # solution.generate_results("2021-07-08", "2021-09-10")
