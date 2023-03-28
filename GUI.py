import tkinter as tk
from ExcelManager import ExcelManager


class GUI:
    def __init__(self):
        # Create the main window and set its title
        self.root = tk.Tk()
        self.root.title("Oboeta")

        # Set the background color of the window to black
        self.root.configure(bg="black")

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set the size and position of the window
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.5)
        x_pos = int((screen_width - window_width) / 2)
        y_pos = int((screen_height - window_height) / 2)
        self.root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_pos, y_pos))

        # Create the text label and input field
        self.text_label = tk.Label(self.root, text="Enter some text:", fg="white", bg="black", font=("Helvetica", 24))
        self.text_label.pack(pady=(50, 20))

        self.input_field = tk.Entry(self.root, bg="gray", fg="white", font=("Helvetica", 18))
        self.input_field.pack(pady=20)

        # Bind the "Enter" key to the input field so that it calls the submit_text method
        self.input_field.bind("<Return>", self.submit_text)

        # Create a label to display the output
        self.output_field = tk.Label(self.root, text="", fg="white", bg="black", font=("Helvetica", 18))
        self.output_field.pack(pady=20)

    # Define a method to be called when the user presses Enter in the input field
    def submit_text(self, event):
        text = self.input_field.get()
        self.output_field.config(text=text)

    def run(self):
        # Start the main event loop
        self.root.mainloop()


# Create an instance of the GUI and run it
manager = ExcelManager("D:\Oboeta Git\Oboeta\B1.xlsx")
gui = GUI()
print(manager.fill_bus())


def bus_test():
    for card in manager.bus:
        print(card.A)


bus_test()
#print("among us")
print(manager.save_bus())
gui.run()
