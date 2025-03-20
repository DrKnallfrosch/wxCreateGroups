import wx
import wx.grid
import csv
import random
from collections import defaultdict
import math


class GroupCalculator:
    """Eine Klasse zur Berechnung und Verwaltung von Schülergruppen.

    :param num_students: Die Anzahl der Schüler.
    :type num_students: int
    :param group_size: Die gewünschte Gruppengröße.
    :type group_size: int
    :raises ValueError: Wenn die Anzahl der Schüler kleiner als die Gruppengröße ist.
    """

    def __init__(self, num_students, group_size):
        """Initialisiert die GroupCalculator-Instanz."""
        if num_students < group_size:
            raise ValueError("Die Anzahl der Schüler muss größer oder gleich der Gruppengröße sein.")

        self.num_students = num_students
        self.group_size = group_size
        self.groups = defaultdict(dict)
        self.previous_combinations = set()
        self.round_counter = 1
        self.student_list = list(range(1, num_students + 1))  # Schüler als Zahlen (1, 2, 3, ...)
        self.delimiter = ","
        self.skip_header = False
        self.first_name_col = 0
        self.last_name_col = 1

    def reset_groups(self):
        """Setzt alle Gruppen und Runden zurück."""
        self.groups.clear()
        self.round_counter = 0

    def create_groups(self):
        """Erstellt Gruppen für die aktuelle Runde."""
        if not self.student_list:
            return

        # Schülerliste neu mischen
        random.shuffle(self.student_list)
        current_groups = {}
        available_students = set(self.student_list)
        group_id = 'A'

        while len(available_students) >= self.group_size:
            group = set()
            for student in list(available_students):
                if len(group) < self.group_size:
                    group.add(student)
                    available_students.remove(student)
            current_groups[group_id] = list(group)
            group_id = chr(ord(group_id) + 1)

        remaining_students = list(available_students)
        if remaining_students:
            group_keys = list(current_groups.keys())
            for i, student in enumerate(remaining_students):
                current_groups[group_keys[i % len(group_keys)]].append(student)

        self.round_counter += 1
        self.groups[self.round_counter] = current_groups

    def get_current_groups(self):
        """Gibt die Gruppen der aktuellen Runde zurück.

        :return: Ein Dictionary mit den Gruppen der aktuellen Runde.
        :rtype: dict
        """
        return self.groups.get(self.round_counter, {})

    def get_round_count(self):
        """Gibt die Anzahl der erstellten Runden zurück.

        :return: Die Anzahl der Runden.
        :rtype: int
        """
        return self.round_counter

    def select_from_file(self, file_path):
        """Lädt Namen aus einer CSV-Datei mit den konfigurierten Optionen für Delimiter und Header.

        :param file_path: Der Pfad zur CSV-Datei.
        :type file_path: str
        """
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)
            if self.skip_header:
                next(reader, None)  # Überspringt die Kopfzeile, falls eingestellt

            self.student_list = [f"{row[self.first_name_col]} {row[self.last_name_col]}" for row in reader
                                 if len(row) > max(self.first_name_col, self.last_name_col)]

    def visualize_groups(self):
        """Gibt die aktuellen Gruppen aus."""
        for round_num, groups in self.groups.items():
            print(f"Runde {round_num}:")
            for group_name, students in groups.items():
                print(f"  Gruppe {round_num}{group_name}: {students}")
            print()

    def can_repeat(self):
        """Berechnet die maximale Anzahl an möglichen Gruppierungen ohne Wiederholung gleicher Paarungen.

        :return: Die maximale Anzahl der möglichen Runden ohne Wiederholungen.
        :rtype: int
        """
        num_pairs_per_round = (self.num_students // self.group_size) * (self.group_size * (self.group_size - 1) // 2)
        total_unique_pairs = math.comb(self.num_students, 2)
        return total_unique_pairs // num_pairs_per_round if num_pairs_per_round > 0 else 1


class GroupApp(wx.Frame):
    """Eine wxPython-basierte GUI-Anwendung zur Erstellung und Verwaltung von Schülergruppen."""

    def __init__(self):
        """Initialisiert die GroupApp-Instanz."""
        super().__init__(None, title="Gruppengenerator", size=(800, 600))
        self.panel = wx.Panel(self)
        self.gc = GroupCalculator(group_size=3, num_students=10)
        self.current_round = 0

        # Schriftart für die UI
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        # Tabelle
        self.grid = wx.grid.Grid(self.panel)
        self.grid.CreateGrid(5, 2)
        self.grid.SetColLabelValue(0, "Gruppe")
        self.grid.SetColLabelValue(1, "Teilnehmer")
        self.grid.SetColSize(0, 150)  # Breite der ersten Spalte
        self.grid.SetColSize(1, 500)  # Breite der zweiten Spalte
        self.grid.SetDefaultRowSize(30)  # Zeilenhöhe
        self.grid.SetLabelFont(font)
        self.grid.SetDefaultCellFont(font)

        # Buttons
        self.load_button = wx.Button(self.panel, label="CSV laden", size=(150, 40))
        self.generate_numbers_button = wx.Button(self.panel, label="Schüler als Zahlen", size=(150, 40))
        self.next_round_button = wx.Button(self.panel, label="Nächste Runde", size=(150, 40))
        self.prev_round_button = wx.Button(self.panel, label="Vorherige Runde", size=(150, 40))
        self.reset_button = wx.Button(self.panel, label="Reset", size=(150, 40))

        # Eingabefelder
        self.spin_group_size = wx.SpinCtrl(self.panel, min=2, max=10, initial=3, size=(100, 40))
        self.spin_students = wx.SpinCtrl(self.panel, min=1, max=100, initial=10, size=(100, 40))

        # Einstellungs-Widgets
        self.delimiter_text_ctrl = wx.TextCtrl(self.panel, value=self.gc.delimiter, size=(50, 40))
        self.skip_header_checkbox = wx.CheckBox(self.panel, label="Header überspringen")
        self.skip_header_checkbox.SetValue(self.gc.skip_header)
        self.first_name_col_input = wx.SpinCtrl(self.panel, min=0, max=10, initial=self.gc.first_name_col, size=(100, 40))
        self.last_name_col_input = wx.SpinCtrl(self.panel, min=0, max=10, initial=self.gc.last_name_col, size=(100, 40))

        # Rundenanzeige
        self.round_label = wx.StaticText(self.panel, label=f"Aktuelle Runde: {self.current_round}")
        self.round_label.SetFont(font)

        # Layout mit wx.GridBagSizer für präzise Platzierung
        sizer = wx.GridBagSizer(10, 10)  # Abstand zwischen den Elementen

        # Tabelle
        sizer.Add(self.grid, pos=(0, 0), span=(1, 4), flag=wx.EXPAND | wx.ALL, border=10)

        # Buttons
        sizer.Add(self.load_button, pos=(1, 0), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(self.generate_numbers_button, pos=(1, 1), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(self.prev_round_button, pos=(1, 2), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(self.next_round_button, pos=(1, 3), flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(self.reset_button, pos=(1, 4), flag=wx.ALL | wx.ALIGN_CENTER, border=5)

        # Gruppengröße und Anzahl der Studenten
        sizer.Add(wx.StaticText(self.panel, label="Gruppengröße:"), pos=(2, 0), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        sizer.Add(self.spin_group_size, pos=(2, 1), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        sizer.Add(wx.StaticText(self.panel, label="Anzahl der Studenten:"), pos=(2, 2), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        sizer.Add(self.spin_students, pos=(2, 3), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)

        # CSV-Einstellungen
        sizer.Add(wx.StaticText(self.panel, label="CSV Delimiter:"), pos=(3, 0), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        sizer.Add(self.delimiter_text_ctrl, pos=(3, 1), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        sizer.Add(self.skip_header_checkbox, pos=(3, 2), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)

        # Spalten für Vor- und Nachname
        sizer.Add(wx.StaticText(self.panel, label="Spalte für Vorname:"), pos=(4, 0), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        sizer.Add(self.first_name_col_input, pos=(4, 1), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        sizer.Add(wx.StaticText(self.panel, label="Spalte für Nachname:"), pos=(4, 2), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        sizer.Add(self.last_name_col_input, pos=(4, 3), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)

        # Rundenanzeige
        sizer.Add(self.round_label, pos=(5, 0), span=(1, 4), flag=wx.ALL | wx.ALIGN_CENTER, border=5)

        # Sizer anpassen
        self.panel.SetSizer(sizer)
        sizer.AddGrowableRow(0)  # Tabelle wächst vertikal
        sizer.AddGrowableCol(0)  # Erste Spalte wächst horizontal
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(2)
        sizer.AddGrowableCol(3)

        # Event-Bindings
        self.load_button.Bind(wx.EVT_BUTTON, self.on_load_csv)
        self.generate_numbers_button.Bind(wx.EVT_BUTTON, self.on_generate_numbers)
        self.next_round_button.Bind(wx.EVT_BUTTON, self.on_next_round)
        self.prev_round_button.Bind(wx.EVT_BUTTON, self.on_prev_round)
        self.reset_button.Bind(wx.EVT_BUTTON, self.on_reset)
        self.skip_header_checkbox.Bind(wx.EVT_CHECKBOX, self.on_toggle_header_skip)
        self.spin_students.Bind(wx.EVT_SPINCTRL, self.on_students_changed)
        self.spin_group_size.Bind(wx.EVT_SPINCTRL, self.on_group_size_changed)  # Event-Handler für Gruppengröße

    def on_prev_round(self, event):
        """Wechselt zur vorherigen Runde.

        :param event: Das auslösende Ereignis.
        :type event: wx.Event
        """
        if self.current_round > 1:
            self.current_round -= 1
            self.update_grid(self.gc.groups[self.current_round])
            self.next_round_button.Enable()
        if self.current_round == 1:
            self.prev_round_button.Disable()

        # Rundenanzeige aktualisieren
        self.update_round_label()

    def on_next_round(self, event):
        """Erstellt eine neue Runde oder wechselt zur nächsten Runde.

        :param event: Das auslösende Ereignis.
        :type event: wx.Event
        """
        # Gruppen erstellen
        self.gc.create_groups()
        self.current_round = self.gc.get_round_count()
        self.update_grid(self.gc.get_current_groups())

        # Buttons aktivieren/deaktivieren
        self.prev_round_button.Enable()
        if self.gc.get_round_count() >= self.gc.can_repeat():
            self.next_round_button.Disable()

        # Rundenanzeige aktualisieren
        self.update_round_label()

    def on_reset(self, event):
        """Setzt alle Gruppen, Runden und die Tabelle zurück.

        :param event: Das auslösende Ereignis.
        :type event: wx.Event
        """
        self.gc.reset_groups()
        self.current_round = 0
        self.update_grid({})
        self.next_round_button.Enable()
        self.prev_round_button.Disable()

        # Rundenanzeige aktualisieren
        self.update_round_label()

        wx.MessageBox("Alle Gruppen und Runden wurden zurückgesetzt.", "Reset", wx.ICON_INFORMATION)

    def on_load_csv(self, event):
        """Lädt die CSV-Datei und zeigt eine Bestätigung an.

        :param event: Das auslösende Ereignis.
        :type event: wx.Event
        """
        with wx.FileDialog(self, "CSV-Datei auswählen", wildcard="CSV files (*.csv)|*.csv",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            file_path = fileDialog.GetPath()
            self.gc.delimiter = self.delimiter_text_ctrl.GetValue()
            self.gc.skip_header = self.skip_header_checkbox.GetValue()
            self.gc.first_name_col = self.first_name_col_input.GetValue()
            self.gc.last_name_col = self.last_name_col_input.GetValue()

            self.gc.select_from_file(file_path)
            wx.MessageBox(f"{len(self.gc.student_list)} Namen geladen!", "Erfolg")

            # Gruppen erstellen
            self.gc.create_groups()
            self.current_round = self.gc.get_round_count()
            self.update_grid(self.gc.get_current_groups())
            self.next_round_button.Enable()
            self.prev_round_button.Disable()

            # Rundenanzeige aktualisieren
            self.update_round_label()

    def on_generate_numbers(self, event):
        """Generiert Schüler als Zahlen basierend auf der eingegebenen Anzahl.

        :param event: Das auslösende Ereignis.
        :type event: wx.Event
        """
        num_students = self.spin_students.GetValue()
        self.gc.num_students = num_students
        self.gc.student_list = list(range(1, num_students + 1))  # Schüler als Zahlen (1, 2, 3, ...)
        self.gc.reset_groups()  # Gruppen zurücksetzen

        # Gruppen erstellen
        self.gc.create_groups()
        self.current_round = self.gc.get_round_count()
        self.update_grid(self.gc.get_current_groups())
        self.next_round_button.Enable()
        self.prev_round_button.Disable()

        # Rundenanzeige aktualisieren
        self.update_round_label()

        wx.MessageBox(f"{num_students} Schüler als Zahlen generiert.", "Erfolg")

    def on_students_changed(self, event):
        """Aktualisiert die Schülerliste, wenn die Anzahl der Schüler geändert wird.

        :param event: Das auslösende Ereignis.
        :type event: wx.Event
        """
        num_students = self.spin_students.GetValue()
        self.gc.num_students = num_students
        self.gc.student_list = list(range(1, num_students + 1))  # Schüler als Zahlen (1, 2, 3, ...)
        self.gc.reset_groups()  # Gruppen zurücksetzen

        # Gruppen erstellen
        self.gc.create_groups()
        self.current_round = self.gc.get_round_count()
        self.update_grid(self.gc.get_current_groups())
        self.next_round_button.Enable()
        self.prev_round_button.Disable()

        # Rundenanzeige aktualisieren
        self.update_round_label()

    def on_group_size_changed(self, event):
        """Aktualisiert die Gruppengröße und erstellt neue Gruppen.

        :param event: Das auslösende Ereignis.
        :type event: wx.Event
        """
        group_size = self.spin_group_size.GetValue()
        self.gc.group_size = group_size
        self.gc.reset_groups()  # Gruppen zurücksetzen

        # Gruppen erstellen
        self.gc.create_groups()
        self.current_round = self.gc.get_round_count()
        self.update_grid(self.gc.get_current_groups())
        self.next_round_button.Enable()
        self.prev_round_button.Disable()

        # Rundenanzeige aktualisieren
        self.update_round_label()

    def update_grid(self, groups):
        """Aktualisiert die Tabelle mit den aktuellen Gruppen.

        :param groups: Die aktuellen Gruppen.
        :type groups: dict
        """
        self.grid.ClearGrid()
        self.grid.SetRowLabelSize(0)

        if len(groups) > self.grid.GetNumberRows():
            self.grid.AppendRows(len(groups) - self.grid.GetNumberRows())

        for row_idx, (group_name, students) in enumerate(groups.items()):
            self.grid.SetCellValue(row_idx, 0, group_name)
            self.grid.SetCellValue(row_idx, 1, ", ".join(map(str, students)))  # Schüler als Zahlen oder Namen darstellen

        self.grid.ForceRefresh()

    def update_round_label(self):
        """Aktualisiert die Rundenanzeige."""
        self.round_label.SetLabel(f"Aktuelle Runde: {self.current_round}")

    def on_toggle_header_skip(self, event):
        """Aktiviert oder deaktiviert das Überspringen des Headers.

        :param event: Das auslösende Ereignis.
        :type event: wx.Event
        """
        self.gc.skip_header = self.skip_header_checkbox.GetValue()


if __name__ == "__main__":
    app = wx.App(False)
    frame = GroupApp()
    frame.Show()
    app.MainLoop()