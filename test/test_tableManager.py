import unittest
from utils.classes.tableManager import TableManager
from utils.classes.table import Table


class TestTableManager(unittest.TestCase):

    def setUp(self):
        self.manager = TableManager()
        self.table1 = Table(1, 4, "V")
        self.table2 = Table(2, 2, "B")

    def test_init(self):
        table_manager = TableManager()
        self.assertEqual(table_manager.tables, [], "L'attribut table est initiée à vide")
        self.assertNotEqual(table_manager.tables, ["something"], "L'attribut table ne devrait pas avoir de contenu")

    def test_addTable(self):
        self.manager.addTable(self.table1)
        self.assertIn(self.table1, self.manager.tables, "La table Table(1,4,'V') a été ajoutée à l'attribut tables")
        self.assertNotIn(Table(3, 4, "B"), self.manager.tables,
                         "La table Table(3,4,'B') ne devrait pas être contenue dans l'attribut tables")

        with self.assertRaises(TypeError):
            self.manager.addTable("something")

        with self.assertRaises(TypeError):
            self.manager.addTable(2)

        with self.assertRaises(ValueError):
            self.manager.addTable(self.table1)

    def test_removeTable(self):
        self.manager.addTable(self.table1)
        self.manager.removeTable(self.table1)
        self.assertNotIn(self.table1, self.manager.tables,
                         "self.table1 du setUp ne devrait pas être contenu dans self.manager.tables")

        with self.assertRaises(ValueError):
            self.manager.removeTable(self.table1)

        with self.assertRaises(ValueError):
            self.manager.removeTable(self.table2)

    def test_findTableWithNumber(self):
        self.manager.addTable(self.table1)
        found_table = self.manager.findTableWithNumber(1)
        self.assertEqual(found_table, self.table1,
                         "La table trouvée avec la méthode findTableWithNumber correspond bien à celle qui porte le numéro 1")

        with self.assertRaises(ValueError):
            self.manager.findTableWithNumber(999)

        with self.assertRaises(TypeError):
            self.manager.findTableWithNumber("something")

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

    '''    
    def test_afficher_table(self):
        table_manager = TableManager()
        table_manager.addTable(self.table1)
        table_manager.addTable(self.table2)
        expected_output = "\n".join(str(table) for table in table_manager.tables)
        output = StringIO()  # StringIO pour capturer la sortie
        with patch('sys.stdout', new=output):
            print(table_manager.tables)
            output = output.getvalue().strip()

        self.assertEqual(output, expected_output)
'''

if __name__ == '__main__':
    unittest.main()
