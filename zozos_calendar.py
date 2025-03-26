import re
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, filedialog


# Function to create the start screen "zozos"
def create_start_screen(callback):
    # Create the main window
    root = tk.Tk()
    root.title("Zozo's Calendar Events Creation :)")

    # Set the window size + background color here 
    root.geometry("600x400")
    root.configure(bg='hotpink')

    # Create a label with Comic Sans font -- wanted that font
    welcome_label = tk.Label(root, text="Welcome to Zozo's Calendar Events Creation :)", font=("Comic Sans MS", 25), bg='hotpink', fg='black', wraplength=550)
    welcome_label.pack(pady=50, padx=20)  # Added padding around the label to improve positioning

    # Create a button with black background and white text -- to be consistent with themed
    start_button = tk.Button(root, text="Start", font=("Comic Sans MS", 20), bg='white', fg='black', command=lambda: [callback(root)])
    start_button.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()


# Function to create an ICS file for all events
def create_ics(events_details, save_path):
    # Get current date for file naming
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Count the number of events and create the file name
    num_files = len(events_details)
    file_name = f"zozo's cal - {current_date} - {num_files} events.ics"
    file_path = f"{save_path}/{file_name}"

    # Start creating the ICS content
    ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//NONSGML iCal 1.0//EN"""

    # Add each event to the ICS content
    for event in events_details:
        event_name, event_start_time, event_end_time = event
        # Format the event date and time
        start_time = event_start_time.strftime("%Y%m%dT%H%M%S")
        end_time = event_end_time.strftime("%Y%m%dT%H%M%S")  # assuming event duration is 1 hour

        # Event content
        ics_content += f"""
BEGIN:VEVENT
SUMMARY:{event_name}
DTSTART:{start_time}
DTEND:{end_time}
DESCRIPTION:{event_name}
LOCATION:Online
BEGIN:VALARM
TRIGGER:-PT15M
DESCRIPTION:Reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT"""

    # End the ICS file
    ics_content += "\nEND:VCALENDAR"

    # Write the ICS file to disk
    with open(file_path, 'w') as file:
        file.write(ics_content)

    print(f"ICS file created at: {file_path}")
    messagebox.showinfo("Success", f"All events have been saved in {file_name}")


# Function to process the input data line by line (including flexible formats)
def process_events(input_data, save_path):
    # Split the input data by lines
    events = input_data.strip().split('\n')

    if not events:
        messagebox.showerror("Error", "Invalid Format")
        return

    # List to store event details
    events_details = []

    # Regular expression pattern to match time ranges and event descriptions
    event_pattern = r'(\d{1,2}:\d{2}\s*[APM]{2})\s*(?:[-to–]?\s*(\d{1,2}:\d{2}\s*[APM]{2}))?\s*(.+)'

    # Process each line to extract event details
    for event in events:
        match = re.search(event_pattern, event.strip())
        if match:
            start_time_str, end_time_str, event_description = match.groups()

            # If no end time is specified --  assume it's 1 hour to be helpful 
            if not end_time_str:
                end_time_str = (datetime.strptime(start_time_str, "%I:%M %p") + timedelta(hours=1)).strftime("%I:%M %p")
            
            # Convert time to 24-hour format to work universally 
            start_time = datetime.strptime(start_time_str, "%I:%M %p")
            end_time = datetime.strptime(end_time_str, "%I:%M %p")

            # Add event details to the list 
            events_details.append((event_description.strip(), start_time, end_time))
        else:
            messagebox.showerror("Error", f"Invalid event format: {event}")
            return

    # Create the ICS file with all events -- easier to download 
    create_ics(events_details, save_path)


# Function to create the dashboard page -- after Start button when clicked
def create_dashboard(root):
    # Create the dashboard window -- with title and options 
    root.destroy()  # Close the start screen window
    dashboard = tk.Tk()
    dashboard.title("Zozo's Calendar Dashboard")

    # Set the window size and background color
    dashboard.geometry("600x400")
    dashboard.configure(bg='hotpink')

    # Create a label for copy and paste 
    dashboard_label = tk.Label(dashboard, text="Paste your event(s) here", font=("Comic Sans MS", 20), bg='hotpink', fg='black')
    dashboard_label.pack(pady=20)

    # Create a text box for input (where the user can paste events) -- format is not constrained to help 
    event_text_box = tk.Text(dashboard, width=50, height=10, font=("Comic Sans MS", 14), bg='black', fg='white')
    event_text_box.pack(pady=10)

    # Create a button so when they are done the events will be processed and converted 
    def on_download_click():
        save_path = filedialog.askdirectory(title="Select Folder to Save ICS Files")
        if save_path:  # Only process if a directory is selected
            process_events(event_text_box.get("1.0", "end-1c"), save_path)

    download_button = tk.Button(dashboard, text="Download your calendar event(s) now.", font=("Comic Sans MS", 16), bg='white', fg='black', 
                               command=on_download_click)
    download_button.pack(pady=20)

    # Run the dashboard window
    dashboard.mainloop()


# Example usage
if __name__ == "__main__":
    create_start_screen(create_dashboard)
