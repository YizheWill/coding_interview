# this program is used only for a coding interview at Rentgrata

### Author: Will Wang

#### approach:

1. first thing first, I'd need to translate the jsons into python hashes: userhash and eventhash.

2. Obtain the users' names from the input.

3. Generate a result hash, which has the desired dates as the keys, and arrays of (start, end) pairs to be the values

4. Use the user names to search the user id in user hash, and then use the user id to find all the events (or we can call them (start, end) pairs) that happened in the desired date-time range. Then append the (start, end) pair into the result hash according to the date.

5. Use a logic to calculate the empty slots that available for all the users in a certain day.

6. Display the results

### Instructions:

1.  The program is written in Python3, so please prep python env accordingly.

2.  To run this app:

        python3 solution.py username1,username2,username3

        for example "python3 solution.py Maggie,Joe,Jordan"

3.  PLEASE NOTICE THAT NO SPACE IS ALLOWED BETWEEN TWO USERNAMES, JUST A ',' IS EXPECTED

4.  you can configure start and end hours by adding two additional args, they have to be intergers and start has to be less than end

        for example:
        python3 solution.py Maggie,Joe,Jordan 15 21

5.  in the Solution.generate_results function, user can change the filter range

        for example change code on solution.py:153 to
        solution.generate_results("2021-07-08", "2021-07-10")

6.  Program will unify all inputs to be lowercase, so doesn't support FirstnameLastname yet

7.  Program doesn't support multiple users with the same name, users with same name are deemed as same person
