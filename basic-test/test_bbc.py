from needle.cases import NeedleTestCase
import os

class MyTests(NeedleTestCase):
    engine_class = 'needle.engines.perceptualdiff_engine.Engine'
    
    def test_masthead(self):
        self.driver.implicitly_wait(10)
        self.driver.get(os.environ.get('NEEDLE_URL'))
        self.assertScreenshot('#blq-mast', 'bbc-masthead')
