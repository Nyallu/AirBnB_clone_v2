import unittest
import MySQLdb

class TestCreateState(unittest.TestCase):
    def setUp(self):
        # Connect to the database
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="mydb")
        self.cursor = self.db.cursor()
        
        # Save the initial number of records
        self.initial_count = self.get_record_count()
        
    def tearDown(self):
        # Close the database connection
        self.db.close()
        
    def test_create_state(self):
        # Execute the console command to create a new state
        # Assuming the command is: INSERT INTO states (name) VALUES ('California')
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.db.commit()
        
        # Get the current number of records
        current_count = self.get_record_count()
        
        # Check if the difference is +1
        self.assertEqual(current_count, self.initial_count + 1)
        
    def get_record_count(self):
        # Execute a query to get the number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count = self.cursor.fetchone()[0]
        return count
    
if __name__ == '__main__':
    unittest.main()
