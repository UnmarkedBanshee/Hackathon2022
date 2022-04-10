import PySimpleGUI as sg
import pandas as pd

def user_preference():
    layout = [[sg.Text('What type of event are you interested in?')],
        [sg.Combo(['Party', 'Sports'], key='1')],
        [sg.Text('How many people would you like to be there?')],
        [sg.Combo(['<10', '10-30'], key='2')],
        [sg.Text('How far would you want the event to be?')],
        [sg.Combo(['<1 miles', '1-2 miles'], key='3')],
        [sg.Text('What day of the week would you prefer?')],
        [sg.Combo(['Weekdays', 'Weekends'], key='4')],
        [sg.Text('What time would you prefer?')],
        [sg.Combo(['12pm - 6pm', '6pm - 12am'], key='5')],
        [sg.Button('Save'), sg.Button('Cancel')]
              ]

    window = sg.Window('User Preferences', layout)
    data_list = []


    event, value = window.read()

    data_list.append(value['1'])
    data_list.append(value['2'])
    data_list.append(value['3'])
    data_list.append(value['4'])
    data_list.append(value['5'])

    window.close()
    return data_list

event_tb = {'EventID': [],
            'Event_Name': [],
            'Category': [],
            'Total_People': [],
            'Location': [],
            'Date': [],
            'Time': []}

RSVP_tb = {'UserID': [],
           'EventID': []}

Preference_tb = {'UserID': [],
                 'Type_Event': [],
                 'Amount_ppl': [],
                 'Type_Location': [],
                 'Day_Pref': [],
                 'Time_Pref': []}

event_df = pd.DataFrame(event_tb)
RSVP_df = pd.DataFrame(RSVP_tb)
Preference_df = pd.DataFrame(Preference_tb)

while True:
    user_preference_list = user_preference()
    Preference_df.loc[len(Preference_df.index)] = ['12422',
                                                   user_preference_list[0],
                                                   user_preference_list[1],
                                                   user_preference_list[2],
                                                   user_preference_list[3],
                                                   user_preference_list[4]]
    print(Preference_df)