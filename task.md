 

### Aufgabe: Implementierung und Erweiterung des `GroupCalculator`

#### Beschreibung der Funktionalität

Der `GroupCalculator` ist eine Python-Klasse, die Gruppen von Schülern basierend auf der Anzahl der Schüler und der gewünschten Gruppengröße erstellt.  
Die Klasse stellt sicher, dass alle Schüler gleichmäßig und zufällig auf die Gruppen verteilt werden und fügt bei Bedarf "Joker" hinzu,  
um ungerade Verteilungen auszugleichen.  
Zusätzlich berechnet die Klasse, wie viele einzigartige Gruppenkombinationen möglich sind,  
und erstellt die möglichen Gruppen in mehreren Runden, um diese Kombinationen zu ermitteln.  
Man kann somit die Methode **`create_groups`** mehrmals aufrufen, um verschiedene Gruppenkombinationen zu erhalten.  
Diese enthalten keine Doppeleinträge, d.h. ein Schüler ist bei jeder neuen Gruppenzusammenstellung in einer anderen Gruppe.  
Allerdings funktioniert dies maximal **`can_repeat()`**\-mal, da danach alle möglichen Gruppenkombinationen durchgespielt sind.  
Die Gruppennamen heißen dabei Group 1A, Group 1B, Group 1C .... In der zweiten Runde dann Group 2A, Group 2B, Group 2C ... .

In der GroupCalculator-Klasse wird ein Dictionary verwendet, um die Gruppen zu speichern.  
Dieses Dictionary self.groups hat die folgende Struktur:

{ 
1: { 
"A": \[1, 2, 3, 4\],  
"B": \[5, 6, 7, 8\]  
},  
2: {  
"A": \[6, 5, 9, 10\],  
"B": \[2, 1, 8, 3\]  
}, ...  
}

- Key: Der erste Key ist eine Zahl, der die Runde benennt. Der zweite Key ist die Gruppenkennung.  
In diesem Fall wird die Gruppe durch einen Buchstaben repräsentiert (A, B, C, ...).  
- Value: Der Value ist eine Liste von Schülern, die in dieser Gruppe sind. Jeder Schüler wird durch eine eindeutige Nummer repräsentiert.  
Wenn ein "Joker" hinzugefügt wird, um ungerade Verteilungen auszugleichen, wird dieser durch den Wert -1 repräsentiert.

Die Methode **`reset_groups_rounds`** setzt die Rundenanzahl und die Gruppen zurück.

Nicht sinnvolle Eingaben werden abgefangen und mit einer Exception quittiert.

Das von mir vorgestellte Layout dient lediglich dazu **eine** Gruppenzusammenstellung zu visualisieren. Für die Ausgabe weiterer Gruppenzusammenstellungen  
(Runden) und das Zurücksetzen muss die GUI angepasst werden. Evtl. kann eine "Blätterfunktion" eingeführt werden, die die verschiedenen Runden anzeigen kann

#### Add on

Es wird eine beliebige CSV Datei eingelesen und der User wird gefragt, welche Spalten er für den Namen verwenden möchte.  
Die Gruppen werden daraufhin mit den Einträgen unter diesem Spaltennamen erstellt. Die Applikation stellt dann  
selbstständig die Anzahl der Schüler fest und erstellt die Gruppen.

#### Schnittstelle der Klasse

*   **Konstruktor (`__init__`)**: Initialisiert die Klasse mit der Anzahl der Schüler und der Gruppengröße. Überprüft, ob die Anzahl der Schüler größer oder gleich der Gruppengröße ist.
*   **`reset_groups`**: Setzt die Rundenanzahl und die Gruppen zurück.
*   **`create_groups`**: Erstellt die Gruppen basierend auf der aktuellen Runde. Vermeidet Wiederholungen von Schülern in den gleichen Gruppen über mehrere Runden hinweg.
*   **`visualize_groups`**: Gibt die erstellten Gruppen in der Konsole aus. Die Gruppen heißen 1A, 1B ... 2A, 2B usw.
*   **`can_repeat`**: Berechnet die maximale Anzahl einzigartiger Gruppierungen, die möglich sind.
*   **`get_current_groups`**: Gibt die aktuell generierte Gruppe zurück.
*   **`get_all_groups`**: Liefert sämtliche generierten Gruppen zurück.
*   **`select_from_csv_file`**: Diese Methode liest eine CSV-Datei ein. Füge auch den restlichen Code zu Auswahl des Namens hinzu.  
    Dies umfasst zusätzlich ein Mapping von Namen zu Studentennummern und schließt die Steuerelemente der GUI mit ein.

#### Aufgabe

1.  **Erstellen der Klasse**: Erstelle den Code der `GroupCalculator`\-Klasse.
2.  **Erweiterung der Funktionalität**: Füge eine Methode `select_from_csv_file` hinzu, die eine CSV Datei einliest (s.o.).
3.  **Erweiterung der Funktionalität**: Erläutere schriftlich wie Du die Funktionalität geprüft hast oder liefere einen Unit Test mit.

#### Abgabe

Reiche das Projekt inkl. requirements.txt ein. Stelle sicher, dass dein Code gut dokumentiert (Sphinx) und lesbar ist.

### Benotung

Dei der Notenvergabe werden folgende Kriterien geprüft:  
- **Korrektheit**: Der Code funktioniert wie beschrieben und erfüllt die Anforderungen.  
- **Dokumentation**: Der Code ist gut dokumentiert (Sphinx) und leicht zu verstehen.  
- **Code Review**: Wir werden euren Algorithmus gemeinsam besprechen. Ihr solltet eure Lösung erklären können.  
- **Erweiterung**: Für sehr gute Noten(>12Pt) sollte die Erweiterung der Funktionalität korrekt implementiert und dokumentiert sein.