"""Test cases for the main module.
"""
from app import main


def test_app_creation() -> None:
  """Test that the App class can be instantiated.
  """
  app = main.App()
  assert isinstance(app, main.App)
  assert app.cget("bg") == main.BG_COLOR
  assert app.logo_img is not None
  assert isinstance(app.logo_img, main.tk.PhotoImage)
  assert isinstance(app.logo, main.tk.Label)


if __name__ == "__main__":
  import pytest
  pytest.main()
