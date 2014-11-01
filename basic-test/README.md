Running a simple Needle test
============================
This code snippet is actually from the needle doc. I figured it's a good way to test that your installation of
needle, and its dependant modules, were successfully installed.

Instructions
------------
1) The first time you run the test your going to need to create your baseline image. This is the image you will always use to compare with current screenshots of the css image you want to test.

    $ nosetests test_bbc.py --with-save-baseline

Confirm that /screenshots/baseline/bbc-masthead.png exist.

2) Now run the test without the --with-save-baseline option:

    $ nosetests test_bbc.py

The test should pass without a hitch and there should now be a /screenshots/bbc-masthead.png file.

3) Now let's set the test up to fail. Open test_bbc.py and edit line 8 to look like the following:

    self.driver.get('http://www.bbc.co.uk')

4) Save the file with the changes and rerun the test again without the baseline option:

    $ nosetests test_bbc.py

The test should fail and there should be a /screenshots/bbc-masthead.diff.png file that will contain the visual diff between the header on the homepage and header on the news page.
