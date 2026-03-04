# Programmieren mit Kojo

## Aufgaben

### Aufgabe 1

- Starte das Anfängertraining (Menü Tools->Beginner Challenges).
- Löse Level 1
- Löse Level 7 und 8: das Quadrat mit und ohne `repeat(4) { ... }`.

<img src="images/aufgaben01_01_level7.png" alt="Aufgabe 1 - Level 7" width="400">
<img src="images/aufgaben01_02_level8.png" alt="Aufgabe 1 - Level 8" width="400">

### Aufgabe 2

- Starte die Schildkrötensteuerung (Menü Tools->Turtle Controller).
- Male eine Figur, bei der die Schildkröte am Start wieder ankommt, aber leicht verdreht ist (z.B. 10 Grad verdreht).
- Kopiere den Code vom Ausgabefenster(Output Pane) in den Programmierbearbeiter(Script Editor)  
  (Click Output Pane, Ctrl-A, Ctrl-C, Click Script Editor, Ctrl-A, Ctrl-V).
- Wiederhole den Code (ohne `clear()`) so oft, dass eine Drehfigur entsteht (z.B. `repeat(36) { ... }`).
- Programm kann beliebig oft gestartet werden mit dem grünen Pfeil im Script Editor.
- Wenn Dir die Schildkröte zu langsam ist, kannst Du zu Aufgabe 3 springen und danach nochmal schönere Drehfiguren 
produzieren.

<img src="images/aufgaben01_03_flag.png" alt="Aufgabe 2 - Figur" width="400">

<img src="images/aufgaben01_04_turn_figure.png" alt="Aufgabe 2 - Drehfigur" width="400">

### Aufgabe 3

- Starte die Dokumentation des Befehlsvorrats (Tools->Instruction Palette).

<img src="images/aufgaben01_05_turtle_commands.png" alt="Aufgabe 3 - Schildkrötenbefehle" width="400">

- Wähle "Live help: On".
- Halte den Mauszeiger über den Turtle Befehl `setSpeed(s)`.
- Füge den Befehl `setSpeed(...)` in Dein Programm aus Aufgabe 2 ein, um die Geschwindigkeit der Schildkröte zu 
verändern. In der Dokumentation werden mögliche Werte genannt: "Possible values are ...". 
Probiere verschiedene Werte aus, um die Auswirkungen zu beobachten.

### Aufgabe 4

Zeichne Dein eigenes Quadrat mit Hilfe des Befehlsvorrats. Verwende dabei den `forward`-Befehl nur einmal. 

<img src="images/aufgaben01_06_square.png" alt="Aufgabe 5 - Verschachtelte Wiederholung" width="200">

Tipps: 
- Verwende Wiederholung/repeat
- Ganz oben im Befehlsvorrat gibt es "Flow"
- Dort gibt es Hilfe zum Befehl `repeat [command]`


### Aufgabe 5

- Zeichne Deine eigene Drehfigur mit Hilfe des Quadrats aus Aufgabe 4 (z.B. durch `repeat` innerhalb `repeat(n) {...}`). 
- Spiele mit `setPenColor` und `setPenThickness`, um die Figur abwechslungsreich zu gestalten.
- Versuche auch folgende Figur zu zeichnen.

<img src="images/aufgaben01_07_turn_figure.png" alt="Aufgabe 5 - Verschachtelte Wiederholung" width="400">

Tipps:
- Die Wiederholungszahl mal der leichten Drehung sollte 360 Grad ergeben (z.B. `repeat(30) { ... right(12) }`)