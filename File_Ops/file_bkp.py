# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:44:24 2020
@author: Manish Sharma
www.RebellionRider.com
www.instagram.com/RebellionRider
www.YouTube.com/RebellionRider
"""

import shutil
from datetime import date
import datetime

def take_backup (src_file_name, dst_file_name=None, src_dir='', dst_dir=''):
    
    #This module work for today's date
    today = date.today()
    date_format =today.strftime("%d_%b_%Y_")

    #this module will work for the date of previous day
    #Un-Comment The Following two statements To Use the 'Previous_day' variable 
    # previous_day = datetime.date.today()-datetime.timedelta(days=1)
    # date_format =previous_day.strftime("%d_%b_%Y_")
   
    #Name of the source file
    src_dir=src_dir+src_file_name
    
    #If Block Will Work When User Enter Either 'None' or empty String ('')
    if dst_file_name is None or not dst_file_name:
        dst_file_name = src_file_name
        dst_file_name = dst_dir+date_format+dst_file_name
        print('if')
    #elif block will work when user Enter an empty string with one or more spaces (' ')    
    elif dst_file_name.isspace():
        dst_file_name = src_file_name
        dst_file_name = dst_dir+date_format+dst_file_name
        print('elif')
    #else block will work when user Enter an a name for the backup copy.    
    else:
        dst_file_name = dst_dir+date_format+dst_file_name
        print('else')
       
    #Take The Backup
    shutil.copy2(src_dir,dst_file_name)
    
    #Success Message
    print("Backup Successful")