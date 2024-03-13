""" Main application file.
"""

import tkinter as tk


class App(tk.Tk):
  """Main application class.
  """

  def __init__(self):
    super().__init__()

    self.title("Professional Tkinter App")
    self.geometry("400x300")

    self.label = tk.Label(self, text="Welcome to the App!", font=("Helvetica", 16))
    self.label.pack(pady=20)

    self.button = tk.Button(self, text="Click Me", command=self.on_click)
    self.button.pack()

  def on_click(self):
    """Button click event handler.
    """
    self.label.config(text="Button Clicked!")


def main():
  """Main function.
  """
  app = App()
  app.mainloop()


if __name__ == "__main__":
  main()
