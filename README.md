**Abstract:
**This Python-based application is designed to simplify the process of creating calendar events and exporting them as .ics (iCalendar) files. Using the Tkinter library, the application provides an intuitive graphical user interface (GUI) for users to input event details, such as event descriptions, start times, and optional end times.

The application allows users to paste multiple events in various flexible formats, such as time ranges (e.g., 9:30 - 10:00 AM) or individual times (e.g., 9:30 AM). The program employs regular expressions to parse the input data and handle varying formats. Once parsed, the events are processed and saved in a single .ics file that users can download and import into their calendar applications.

Key functionalities of the program include:

Event Parsing: The program can handle both event start times with or without end times, defaulting the end time to an hour if not specified.

Graphical Interface: A user-friendly interface allows users to paste event details into a text box, and upon clicking the “Download your calendar event(s) now” button, the application generates and saves the events as an .ics file in the user-specified directory.

File Naming: The .ics file is named dynamically, including the current date and the number of events, ensuring organized and easily identifiable file naming.

This tool is particularly useful for individuals or organizations that need to quickly convert multiple events into a calendar format for scheduling or sharing purposes, automating a process that would otherwise require manually inputting events into a calendar application.
