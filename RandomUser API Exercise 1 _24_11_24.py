## Write your code here
from randomuser import RandomUser
import pandas as pd
r=RandomUser()
some_list=r.generate_users(10)
some_list
picture = r.get_picture()
for user in some_list:
    print(user.get_picture())