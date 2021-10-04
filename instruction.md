# this program is used only for a coding interview at Rentgrata

### Author: Will Wang

#### 1. The program is written in Python3, so please prep python env accordingly.

##### 2. To run this app:

##### python3 solution.py username1,username2,username3

##### for example "python3 solution.py Maggie,Joe,Jordan"

##### 3. PLEASE NOTICE THAT NO SPACE IS ALLOWED BETWEEN TWO USERNAMES, JUST A ',' IS EXPECTED

##### 4. you can configure start and end hours by adding two additional args, they have to be intergers and start has to be less than end

##### for example "python3 solution.py Maggie,Joe,Jordan 15 21"

##### 5. in the Solution.generate_results function, user can change the filter range

##### for example solution.generate_results("2021-07-08", end_date="2021-07-10"):

##### 6. program will unify all inputs to be lowercase, so doesn't support FirstnameLastname yet

##### 7. Doesn't support multiple users with the same name, users with same name are deemed as same person
