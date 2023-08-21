'''
  import typing to declare List types
  import datetime to declare datetime item type
  import cpmpy to validate meetings schedule
  import models module from Models to use Meeting , Room and  

'''
from typing import List 
from datetime import datetime
from cpmpy import *
from Models.models import Meeting  , Room , date_format , meetings_list , room_list  
from fastapi import Depends , status , Response , HTTPException 

def is_overlaped(new_meeting : Meeting , old_meeting :Meeting)-> bool:
    '''
    Checks if a new meeting overlaps with an existing meeting.
    '''
    before_but_continue = (new_meeting.start_date<=old_meeting.start_date) and (new_meeting.end_date>old_meeting.start_date)
    new_in_old = (new_meeting.start_date>old_meeting.start_date) and (new_meeting.end_date<=old_meeting.end_date)
    old_in_new = (new_meeting.start_date<=old_meeting.start_date) and (new_meeting.end_date>=old_meeting.end_date)
    inold_but_more = (new_meeting.start_date< old_meeting.end_date) and (new_meeting.end_date>old_meeting.end_date)
    if (before_but_continue or new_in_old or old_in_new or inold_but_more):
        return True
    else :
        return False
        
def meeting_validation(current_meeting: Meeting, meeting_list: list[Meeting],rooms_list : list[Room]):
    """
    Validates a meeting by checking if it overlaps with existing meetings and meets capacity requirements.
    """
    for item in rooms_list :
        if item.Room_id == current_meeting.Room_id :
            selected_room_capacity = item.Room_capacity
    #selected_room_capacity = next(item.Room_capacity for item in rooms_list if item.Room_id == current_meeting.Room_id)
    curunt_room_meetings =[item for item in meeting_list if item.Room_id == current_meeting.Room_id]
    
    if len(meeting_list) == 0:
      print (f'First meeting added')
      return f'first_meeting_added'
    elif current_meeting.Room_id not in [item.Room_id for item in rooms_list]:
      print (f'Unvalid room id')
      return f'unvalid_room_id'
    elif current_meeting.attendance> selected_room_capacity:
        print (f'Capacity overloaded')
        return f'capacity_overloaded'
    else :
        for item in curunt_room_meetings:
            if is_overlaped(new_meeting=current_meeting, old_meeting = item):
                print (f'Time overlapped')
                y = f'time_overlapped'
            else :
                print (f'Added successfully')
                y = f'added_successfully'
                
                
        return y

def post_schedule_meeting(added_meeting : Meeting, post_meeting_list: list[Meeting], room_list: list[Room]):
    """
    Handles the scheduling of a meeting by validating it and adding it to the meeting list.
    """
    x = meeting_validation(current_meeting= added_meeting , meeting_list= post_meeting_list , rooms_list= room_list)

    if len(room_list) == 0:
        raise HTTPException(status_code=400 , detail="No Room Defined . Please First Define a Room")
    elif x == 'first_meeting_added':
        meetings_list.append(added_meeting)
        return Response(status_code=status.HTTP_201_CREATED,content='Successfully Added')
    if x == 'unvalid_room_id':
       raise HTTPException(status_code=400 , detail="Unvalid Room ID passed")
    elif x == 'capacity_overloaded':
        raise HTTPException(status_code=400 , detail="Attendance are more than capacity of selected room")
    elif x == 'time_overlapped':
        raise HTTPException(status_code=400 , detail="Meetings are overlapping with scheduled meetings")
    elif x == 'added_successfully' :
        meetings_list.append(added_meeting)
        return Response(status_code=status.HTTP_201_CREATED,content='Successfully Added')

def post_add_room(post_room : Room):
    """
    Adds a new room to the list of rooms if the room ID is not already present.
    """
    if post_room.Room_id in [item.Room_id for item in room_list]:
        print (f'Room id is already added')
        raise HTTPException(status_code=409, detail="Room id is already added")
    else :
        room_list.append(post_room)
        print (f'Room sucsessfully added')        
    return Response(status_code=status.HTTP_201_CREATED, content='Room sucsessfully added')

def get_meeting():
    """
    Returns the list of meetings if there are any, otherwise raises exception.
    """
    if len(meetings_list) == 0:
        print(f'No meeting found')
        raise HTTPException(status_code=404, detail="No Meeting found")
    else :
        print(f'Meetings found')
    return meetings_list

def get_room():
    """
    Returns the list of rooms if there are any, otherwise raises exception.
    """
    if len(room_list) == 0:
        print (f'No room found')
        raise HTTPException(status_code=404, detail="No Room found")
    else :
        print (f'Room found')
    return room_list
