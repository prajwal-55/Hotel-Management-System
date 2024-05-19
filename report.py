import tkinter as tk
from tkinter import ttk

class ReportPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.title_label = tk.Label(self, text="Hotel Management System - Report Page", font=("Helvetica", 18))
        self.title_label.pack(pady=10)
        
        self.report_tree = ttk.Treeview(self)
        self.report_tree["columns"] = ("Name", "Room", "Check In", "Check Out")
        
        self.report_tree.heading("Name", text="Name")
        self.report_tree.heading("Room", text="Room")
        self.report_tree.heading("Check In", text="Check In")
        self.report_tree.heading("Check Out", text="Check Out")
        
        self.report_tree.column("#0", width=0, stretch=tk.NO)
        self.report_tree.column("Name", anchor=tk.W, width=150)
        self.report_tree.column("Room", anchor=tk.W, width=100)
        self.report_tree.column("Check In", anchor=tk.W, width=100)
        self.report_tree.column("Check Out", anchor=tk.W, width=100)
        
        self.report_tree.pack(fill=tk.BOTH, expand=True)
        
        self.back_button = tk.Button(self, text="Back", command=self.back_to_home)
        self.back_button.pack(pady=10)
        
    def populate_report(self, data):
        for record in data:
            self.report_tree.insert("", tk.END, values=record)
    
    def back_to_home(self):
        self.controller.show_frame("HomePage")

# Example usage
if __name__ == "__main__":
    class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (HomePage, ReportPage):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("HomePage")

        def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

    class HomePage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.title_label = tk.Label(self, text="Hotel Management System - Home Page", font=("Helvetica", 18))
            self.title_label.pack(pady=10)

            self.report_button = tk.Button(self, text="View Report", command=lambda: self.controller.show_frame("ReportPage"))
            self.report_button.pack(pady=10)

    app = SampleApp()
    app.mainloop()
