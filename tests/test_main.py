"""Test cases for the main module.
"""
from app import main


def test_app_creation():
  """Test that the App class can be instantiated.
  """
  app = main.App()
  assert isinstance(app, main.App)


def test_button_click():
  """Test that the button click changes the label text.
  """
  app = main.App()
  button = app.button
  button.invoke()  # Simulate button click
  assert app.label.cget("text") == "Button Clicked!"


if __name__ == "__main__":
  import pytest
  pytest.main()
