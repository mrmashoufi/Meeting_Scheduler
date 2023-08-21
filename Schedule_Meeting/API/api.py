# import the FastAPI module , Optional and List types for type hints
#import the BaseModel class from the Pydantic module to define our class
#import dependencies from other modules

import fastapi
from typing import List
from pydantic import BaseModel
from Models.models import Meeting , meetings_list , Room , room_list 
from fastapi import Depends , status , Response , HTTPException 
from datetime import datetime
import CSP.constraint


router = fastapi.APIRouter()


@router.get('/')
async def root():
    '''
    This method returns a welcome message and user Guied when accessed.
    - **Response**: Welcome message and user Guied
    '''
    return f'Hi . Welcome to Meeting Scheduler'

@router.get('/meetings' )
async def get_meetings() -> list[Meeting] :
    '''
    This method returns a list of all scheduled meetings.
    - **Response**: List of all meetings
    - **Raises**: HTTPException 404 if no meeting is found
    '''
    return CSP.constraint.get_meeting()

@router.get('/rooms' , status_code=status.HTTP_200_OK)
async def get_rooms() -> list[Room]:
    '''
    This method returns a list of all defined rooms.
    - **Response**: List of all rooms
    - **Raises**: HTTPException 404 if no room is found
    '''
    return CSP.constraint.get_room()

@router.post('/add_room' , status_code=status.HTTP_201_CREATED)
async def add_room(room : Room ):
    '''
    This method adds a new meeting room to the room list.
    It checks if the new room id already exists and returns an error message if it does.
    - **Parameters**:
      - **room**: Room object with room details
        - **Room_id**: Room identifier (integer)
        - **Room_capacity**: Room capacity (integer)
        - **Room_name**: Room name (string)
    - **Response**: Success message
    - **Raises**: HTTPException 409 if room id already exists
    '''
    return CSP.constraint.post_add_room(room)

@router.post('/schedule_meeting', status_code=status.HTTP_201_CREATED)
async def schedule_meeting(meeting: Meeting):
    '''
    This method adds a new meeting to the meetings list.
    It validates if the new meeting can be added based on certain constraints.
    - **Parameters**:
      - **meeting**: Meeting object with meeting details
        - **Room_id**: Room id of the room being scheduled (integer)
        - **attendance**: Number of attendance in the meeting (integer)
        - **start_date**: Start time of the meeting (datetime)
        - **end_date**: End time of the meeting (datetime)
    - **Response**: Success message
    - **Raises**: HTTPException 400 if invalid request . explained more in the body
    '''
    return CSP.constraint.post_schedule_meeting(added_meeting= meeting , post_meeting_list=meetings_list , room_list= room_list)

