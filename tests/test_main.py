"""Test cases for the main module.
"""
from app import main


def test_app_creation():
  """Test that the App class can be instantiated.
  """
  app = main.App()
  assert isinstance(app, main.App)


if __name__ == "__main__":
  import pytest
  pytest.main()
