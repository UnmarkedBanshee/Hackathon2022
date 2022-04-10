"""import PySimpleGUI as sg"""
from re import L
from tkinter import *
from PIL import ImageTk, Image
"""
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
            'Day_of_Week': [],
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


user_preference_list = user_preference()
Preference_df.loc[len(Preference_df.index)] = ['12422',
                                                   user_preference_list[0],
                                                   user_preference_list[1],
                                                   user_preference_list[2],
                                                   user_preference_list[3],
                                                   user_preference_list[4]]
print(Preference_df)
"""
# BUTTONS IN 1 EVENT
   # 1. Add to calender
   # 2. find event
   # 3. RSVP

root = Tk()
WINDOW_WIDTH = '1600'
WINDOW_HEIGHT = '1000'
WINDOW_DIMENSIONS = (WINDOW_WIDTH + 'x' + WINDOW_HEIGHT)
root.title('ANTISOCIAL CLUB')

root['background']='#355C7D'
#backgorund Image of main window
image_open = Image.open(r"C:\Users\daxpr\Desktop\Hackathon 20222\\intro-background.jpg")
bk_img = ImageTk.PhotoImage(image_open)
bg = PhotoImage(file = 'disco-dba865f1.png')
bg_label = Label(root, image = bk_img)
bg_label.pack()
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)


root.geometry(WINDOW_DIMENSIONS)


'''
event name
catagory
total people
location
date
time
'''


class Event():
   def __init__(self, name, catagory, time, people, place):
       self.name = name
       self.catagory = catagory
       self.time = time
       self.people = people
       self.place = place



"""    
if __name__ == '__main__':
    top = tk.Tk()
    entry_field_variable = tk.StringVar()
    entry = tk.Entry(top, textvariable=entry_field_variable)
    entry.pack()
    tk.Button(top, text="save", command=save).pack()

    top.mainloop()"""



def open_create_event_window():
    def get_field_information():
        user_event_list = []
        name = name_of_event_entry.get()
        catagory = catagory_selected.get()
        total_people = amount_of_people_selected.get()
        place = location_of_event_entry.get()
        day_of_week = day_of_week_selected.get()
        time_of_day = time_of_day_selected.get()

        user_event_list.append(name)
        user_event_list.append(catagory)
        user_event_list.append(total_people)
        user_event_list.append(place)
        user_event_list.append(day_of_week)
        user_event_list.append(time_of_day)
        return user_event_list
    def save():
        event_name = EventName.get()
        event_location = EventLocation.get()
        fopen = open('data.txt', 'a')
        fopen.write('\n')
        fopen.write("Event Name: {event_name}\n").format(event_name)
        fopen.write("Event Location: {event_name}\n").format(event_location)
        fopen.close()

    new_window = Toplevel(root)

   # sets the title of the
   # Toplevel widget
    new_window.title("New Window")

   # sets the geometry of toplevel
    new_window.geometry(WINDOW_DIMENSIONS)
    EventName = StringVar()
    EventLocation = StringVar()
    name_of_event_label = Label(new_window, text='Name of the event')
    name_of_event_label.place(relx=0.1, rely=0.2)
    name_of_event_entry = Entry(new_window, textvariable=EventName)
    name_of_event_entry.place(relx = 0.5, rely=0.2)

    catagories_of_events = ['Party', 'Sports', 'Studying', 'Hanging']


    catagory_selected = StringVar(new_window)
    catagory_selected.set('Party')  # default value
    catagory_of_event_label = Label(new_window, text='Catagory of event')
    catagory_of_event_label.place(relx=0.1, rely=0.3)
    catagory_of_event_dropdown = OptionMenu(new_window, catagory_selected, *catagories_of_events)
    catagory_of_event_dropdown.place(relx=0.5,rely=0.3)

    # Times aspect of creating event
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times_of_day = ['12:00am-3:00am', '3:00am-6:00am', '6:00am-9:00am', '9:00am-12:00pm', '12:00pm-3:00pm', '3:00pm-6:00pm', '6:00pm-9:00pm', '9:00pm-12:00am']
    time_of_event_label = Label(new_window, text='When will the event take place')
    time_of_event_label.place(relx=0.1, rely = 0.5)
    time_of_event_frame = Frame(new_window)
    time_of_event_frame.place(relx=0.5,rely=0.5)
    day_of_week_selected = StringVar(new_window)
    day_of_week_selected.set('Monday')  # default value
    time_of_event_day = OptionMenu(time_of_event_frame, day_of_week_selected, *days_of_week)
    time_of_event_day.grid(row=1,column=0)

    time_of_day_selected = StringVar(new_window)
    time_of_day_selected.set(times_of_day[0])  # default value
    time_of_event_hours = OptionMenu(time_of_event_frame, time_of_day_selected, *times_of_day)
    time_of_event_hours.grid(row=1, column=1)

    # Amount of people going to the event
    amount_of_people_at_event_options = ['1-10', '11-30', '31-50', 'Unlimited']
    amount_of_people_selected = StringVar(new_window)
    amount_of_people_selected.set('Unlimited')  # default value
    amount_of_people_at_event_label = Label(new_window, text='How many people will be at the event')
    amount_of_people_at_event_label.place(relx=0.1, rely= 0.7)
    amount_of_people_at_event_dropdown = OptionMenu(new_window, amount_of_people_selected, *amount_of_people_at_event_options)
    amount_of_people_at_event_dropdown.place(relx=0.7, rely=0.7)

    location_of_event_label = Label(new_window, text='Location of the event')
    location_of_event_label.place(relx=0.1, rely=0.8)
    location_of_event_entry = Entry(new_window)
    location_of_event_entry.place(relx=0.5, rely=0.8)

    # Finished creating event button
    finished_creating_event_button = Button(new_window, text='Create event', command = save(), width=10, height=1,bg='green')
    finished_creating_event_exit_button = Button(new_window, text='Exit', command=lambda: new_window.destroy())
    finished_creating_event_button.place(relx =0.1, rely =0.85, relwidth = 0.8, relheight = 0.15)
    finished_creating_event_exit_button.place(relx =0.1, rely =0.05, relwidth = 0.4, relheight = 0.15)

# Create event button on bottom

create_event_button = Button(root, text='Create event', command=open_create_event_window)
create_event_button.place(rely= 0.85, relwidth = 1, relheight = 0.15)

event = Frame(root, bg='white')
event.place(relx = 0.1, width = 400, height = 100)

event_title = Label(event, text = 'This is the event title', justify='center')
event_title.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)
event_rsvp_button = Button(event, text = 'RSVP')
event_rsvp_button.place(relx = 0.1, rely = 0.7)

event_add_to_calendar_button = Button(event, text= 'Add to calendar')
event_add_to_calendar_button.place(relx = 0.3, rely = 0.7)

event_find_event_button = Button(event, text= 'Find event')
event_find_event_button.place(relx = 0.7, rely=0.7)

root.mainloop()
"""
event_list = get_field_information()
event_df.loc[len(Preference_df.index)] = ['12422',
                                                   event_list[0],
                                                   event_list[1],
                                                   event_list[2],
                                                   event_list[3],
                                                   event_list[4],
                                                   event_list[5]]
print(event_df)"""