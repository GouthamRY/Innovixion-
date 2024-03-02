import tkinter as tk
from tkinter import messagebox
import time

class AlarmClock:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")

        self.label = tk.Label(master, text="Set Alarm Time (HH:MM):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.set_button = tk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack()

    def set_alarm(self):
        alarm_time = self.entry.get()
        try:
            alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
            current_time = time.localtime()
            current_hour, current_minute = current_time.tm_hour, current_time.tm_min

            if (
                0 <= alarm_hour < 24
                and 0 <= alarm_minute < 60
                and (alarm_hour > current_hour or (alarm_hour == current_hour and alarm_minute >= current_minute))
            ):
                time_difference_seconds = (alarm_hour - current_hour) * 3600 + (alarm_minute - current_minute) * 60
                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
                self.master.after(time_difference_seconds * 1000, self.alert)
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid time in HH:MM format")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid time in HH:MM format")

    def alert(self):
        messagebox.showinfo("Alarm", "Wake up!")

def main():
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
