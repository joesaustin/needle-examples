Selenium Needle Examples
========================
Needle is a tool for testing your CSS with Selenium and nose. It checks that CSS renders correctly by taking
screenshots of portions of a website and comparing them against known good screenshots. It also provides tools for
testing calculated CSS values and the position of HTML elements.


Dependencies
------------
1) If you haven't already(especially if your on OSx 10.9 or above) make sure you install xcodes command line developer tools:

    $ xcode-select --install

2) Install the required dependencies Pillow (Python Imaging Library), Needle (), and nose.

    $ pip install -r requirements.txt

3) Install Percetualdiff. Percetualdiff is a command line tool for compairing differences between images:

    $ brew install perceptualdiff

