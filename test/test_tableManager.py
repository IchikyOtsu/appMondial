import unittest
from utils.classes.tableManager import Table, TableManager

class TestTableManager(unittest.TestCase):

    def setUp(self):
        self.manager = TableManager()
        self.table1 = Table(1, 4, "V")
        self.table2 = Table(2, 2, "B")

    def test_addTable(self):
        self.manager.addTable(self.table1)
        self.assertIn(self.table1, self.manager.tables)

    def test_removeTable(self):
        self.manager.addTable(self.table1)
        self.manager.removeTable(self.table1)
        self.assertNotIn(self.table1, self.manager.tables)

    def test_findTableWithNumber(self):
        self.manager.addTable(self.table1)
        found_table = self.manager.findTableWithNumber(1)
        self.assertEqual(found_table, self.table1)
        self.assertIsNone(self.manager.findTableWithNumber(999))  # Test avec un numéro inexistant

    def test_to_json(self):
        self.manager.addTable(self.table1)
        self.manager.addTable(self.table2)
        expected_output = {
            "tables": [self.table1.to_json(), self.table2.to_json()]
        }
        self.assertEqual(self.manager.to_json(), expected_output)

    def test_from_json(self):
        data = {
            "tables": [self.table1.to_json(), self.table2.to_json()]
        }
        manager_from_json = TableManager.from_json(data)
        self.assertEqual(len(manager_from_json.tables), 2)
        self.assertEqual(manager_from_json.tables[0].numTable, 1)
        self.assertEqual(manager_from_json.tables[1].numTable, 2)

if __name__ == '__main__':
    unittest.main()
