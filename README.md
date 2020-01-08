# sonicremote
© Jonathan Lacson, 2020

Simple Flask app that serves a webapp that lets a user
play sounds remotely.

## Development Environment

### Prerequisites
* Python 3
* `pip` (normally comes with Python 3)

### Setting Up

_I think Visual Studio Code should do most of this automatically._
_I'm also assuming you're using a UNIX machine,_
_so the instructions may be different for Windows._

In a terminal, run `pip3 install virtualenv`. Once this completes, run `virtualenv .venv`. 
This initializes a virtual environment for Python (in the .venv folder) so that our 
dependencies for this project don't clog up our local machine.

Once we're running in the virtual environment, as evidenced by the `(.venv) >`
in our terminal prompts, run `pip install -r requirements.txt`. This pulls
our dependencies that we need for the project.