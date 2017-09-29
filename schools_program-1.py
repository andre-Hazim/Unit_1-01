# created by andre hazim
# created on Sept 2017
# created for ICS3U
# Creates a school gui in 3 ways

import ui

def mt_touch_up_inside (sender):
    #displays the Mt 
    view['school_name_label'].text = ('Mother Tersea High School')
    view['School_team_name_label'].text = ('Mother Tersea Titans')
    
def st_joes_touch_up_inside (sender):
    #displays the St Joes
    view['school_name_label'].text = ('St Joesph High School')
    view['gSchool_team_name_label'].text = ('St Joes Jaguars')
    
def st_mark_touch_up_inside (sender):
    #displays the st mark 
    view['school_name_label'].text = ('Mark High School')
    view['School_team_name_label'].text = ('St Marks Lions')

view = ui.load_view()
view.present('sheet')
