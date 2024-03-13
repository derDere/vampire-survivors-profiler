"""
This script is used to build the project using pyinstaller.
"""


import subprocess


def build() -> None:
  """Build the project using pyinstaller.
  """
  check = subprocess.run(['pyinstaller', 'project.spec'], check=True)
  if check.returncode == 0:
    print("Build successful.")
