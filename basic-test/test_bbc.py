from needle.cases import NeedleTestCase

class MyTests(NeedleTestCase):
    engine_class = 'needle.engines.perceptualdiff_engine.Engine'
    
    def test_masthead(self):
        self.driver.implicitly_wait(10)
        self.driver.get('http://www.bbc.co.uk/news')
        self.assertScreenshot('#blq-mast', 'bbc-masthead')
