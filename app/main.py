""" Main application file.
"""

import tkinter as tk


class App(tk.Tk):
  """Main application class.
  """

  def __init__(self) -> None:
    super().__init__()

    self.title("Vampire Survivors Profiler")
    self.configure(bg="#7A0019")
    width, height, x, y = self._find_bounds()
    self.geometry(f'{width}x{height}+{x}+{y}')
    self.resizable(False, False)

  def _find_bounds(self) -> tuple[int, int, int, int]:
    """Find the center of the screen.
    """
    width = 650
    height = 800
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    return width, height, x, y


def main() -> None:
  """Main function.
  """
  app:App = App()
  app.mainloop()


if __name__ == "__main__":
  main()
