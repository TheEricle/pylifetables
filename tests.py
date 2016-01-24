#!/usr/bin/python
import unittest
from LifeTable import LifeTable as lt
 
class LifeTableTests(unittest.TestCase):
    """Sample test case"""
     
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "LifeTableTests:setUp_:begin"
        self.sample_table = lt("sample.csv", "M")
        self.answer_key = lt.preprocess_pop("sample.csv")
        print "LifeTableTests:setUp_:end"
     
    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "LifeTableTests:tearDown_:begin"
        ## do something...
        print "LifeTableTests:tearDown_:end"
     
    # test nmx
    def testnmx(self):
        """Test nmx method"""
        self.assertEqual(self.sample_table.get_pop_nmx().all(), 
            self.answer_key["nmx"].all(), "nMx calculation differs from answer key.")
        print "LifeTableTests:testnmx"

    # test nax
    def testnax(self):
        """Test nax method"""
        self.assertEqual(self.sample_table.get_pop_nax().all(), 
            self.answer_key["nax"].all(), "nax calculation differs from answer key.")
        print "LifeTableTests:testnax"

    # test npx
    def testnpx(self):
        """Test npx method"""
        self.assertEqual(self.sample_table.get_pop_npx().all(), 
            self.answer_key["npx"].all(), "npx calculation differs from answer key.")
        print "LifeTableTests:testnpx"

    # test npx
    def testnqx(self):
        """Test nqx method"""
        self.assertEqual(self.sample_table.get_pop_nqx().all(), 
            self.answer_key["nqx"].all(), "nqx calculation differs from answer key.")
        print "LifeTableTests:testnqx"

        # test npx
    def testnlx(self):
        """Test nlx method"""
        self.assertEqual(self.sample_table.get_pop_nlx().all(), 
            self.answer_key["nLx"].all(), "nlx calculation differs from answer key.")
        print "LifeTableTests:testnlx"

        # test npx
    def testlx(self):
        """Test lx method"""
        self.assertEqual(self.sample_table.get_pop_lx().all(), 
            self.answer_key["lx"].all(), "lx calculation differs from answer key.")
        print "LifeTableTests:testlx"

            # test npx
    def testex(self):
        """Test ex method"""
        self.assertEqual(self.sample_table.get_pop_ex().all(), 
            self.answer_key["ex"].all(), "ex calculation differs from answer key.")
        print "LifeTableTests:testex"
            
            # test npx
    def testtx(self):
        """Test tx method"""
        self.assertEqual(self.sample_table.get_pop_tx().all(), 
            self.answer_key["Tx"].all(), "tx calculation differs from answer key.")
        print "LifeTableTests:testtx"

# Run the test case
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LifeTableTests)
    unittest.TextTestRunner(verbosity=2).run(suite)