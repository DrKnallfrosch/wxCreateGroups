import unittest
import os
import tempfile
from collections import defaultdict
from GroupCalculator.GroupCalculator import GroupCalculator  # Ersetze 'your_module' durch den Namen deines Moduls


class TestGroupCalculator(unittest.TestCase):
    def setUp(self):
        """Initialisiert den GroupCalculator für die Tests."""
        self.num_students = 10
        self.group_size = 3
        self.gc = GroupCalculator(self.num_students, self.group_size)

    def test_initialization(self):
        """Testet die Initialisierung der GroupCalculator-Instanz."""
        self.assertEqual(self.gc.num_students, self.num_students)
        self.assertEqual(self.gc.group_size, self.group_size)
        self.assertEqual(self.gc.round_counter, 1)
        self.assertEqual(len(self.gc.student_list), self.num_students)

    def test_create_groups(self):
        """Testet das Erstellen von Gruppen."""
        self.gc.create_groups()
        groups = self.gc.get_current_groups()
        self.assertGreater(len(groups), 0)

        # Überprüft, ob alle Schüler in den Gruppen sind
        all_students_in_groups = set()
        for group in groups.values():
            all_students_in_groups.update(group)
        self.assertEqual(all_students_in_groups, set(self.gc.student_list))

    def test_reset_groups(self):
        """Testet das Zurücksetzen der Gruppen."""
        self.gc.create_groups()
        self.gc.reset_groups()
        self.assertEqual(len(self.gc.groups), 0)
        self.assertEqual(self.gc.round_counter, 0)

    def test_load_from_csv(self):
        """Testet das Laden von Schülern aus einer CSV-Datei."""
        # Erstelle eine temporäre CSV-Datei
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as temp_file:
            temp_file.write("Vorname,Nachname\n")  # Kopfzeile
            temp_file.write("Max,Mustermann\n")    # Schüler 1
            temp_file.write("Erika,Musterfrau\n")  # Schüler 2
            temp_file_path = temp_file.name

        # Setze skip_header auf True, um die Kopfzeile zu überspringen
        self.gc.skip_header = True

        # Lade die CSV-Datei
        self.gc.select_from_file(temp_file_path)
        self.assertEqual(len(self.gc.student_list), 2)  # Erwarte 2 Schüler
        self.assertIn("Max Mustermann", self.gc.student_list)
        self.assertIn("Erika Musterfrau", self.gc.student_list)

        # Lösche die temporäre Datei
        os.remove(temp_file_path)

    def test_can_repeat(self):
        """Testet die Berechnung der maximalen Anzahl möglicher Runden ohne Wiederholungen."""
        max_rounds = self.gc.can_repeat()
        self.assertGreater(max_rounds, 0)

    def test_invalid_group_size(self):
        """Testet die Initialisierung mit einer ungültigen Gruppengröße."""
        with self.assertRaises(ValueError):
            GroupCalculator(num_students=2, group_size=3)


if __name__ == "__main__":
    unittest.main()