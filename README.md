# sonicremote
© Jonathan Lacson, 2020

Simple Flask app that serves a webapp that lets a user
play sounds remotely.

## Setup

In the source directory, make a folder called `audio` and
put your audio files in there. They must all be prefixed by
a unique two-digit number followed by a dash.

So, if you wanted to add a file called `song.mp3`, you'd
need to rename it to `XX-song.mp3` where XX is a unique
two digit number.

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

Once the virtual environment is initialized, we need to source it.
Run `source .venv/bin/activate` in the terminal.
(More info on how this works can be found [here](https://virtualenv.pypa.io/en/latest/userguide/).)

Once we're running in the virtual environment, as evidenced by the `(.venv) >`
in our terminal prompts, run `pip3 install -r requirements.txt`. This pulls
our dependencies that we need for the project.

#### (macOS only) PyObjC

I didn't want to add this dependency into `requirements.txt` because it will cause
non Windows/Linux environments to fail.
When running in the virtualenv, run `pip3 install PyObjC`.
