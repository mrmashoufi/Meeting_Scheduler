# From pydantic import BaseModel to create a pydantic model
# also input datetime to declare datetime object type
# typing is used to list and type
from datetime import datetime
from typing import  List
from pydantic import BaseModel

# Defining the Meeting class inheriting from BaseModel
# In next version , room id could be optional and system would define it according to rooms situations
class Meeting(BaseModel):
    Room_id : int
    attendance : int
    start_date : datetime
    end_date : datetime

# Defining the Room class inheriting from BaseModel

class Room(BaseModel):
    Room_id : int
    Room_name : str
    Room_capacity : int

meetings_list : list[Meeting] = list()# Initializing an empty list to store instances of the Meeting class
room_list: list[Room] = list() # Initializing an empty list to store instances of the Room class
date_format = '%Y%m%d%H%M' #Setting the date format for converting to int

