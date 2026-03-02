# 🐨 Kojo installieren auf Windows (ohne Admin-Rechte)

Hallo! 😊  
Hier lernst du Schritt für Schritt, wie du Kojo installierst.

---

# 📥 Schritt 1: Kojo herunterladen

Lade Kojo herunter:  
👉 [Kojo_2_9_34.zip](https://github.com/litan/kojo/releases/download/2.9.34_release/Kojo_2_9_34.zip)

Die Datei wird in deinem **Downloads-Ordner** gespeichert.

---

# ☕ Schritt 2: Java herunterladen

Kojo braucht Java. Lade es hier herunter:  
👉 [microsoft-jdk-21.0.10-windows-x64.zip](https://aka.ms/download-jdk/microsoft-jdk-21.0.10-windows-x64.zip)

Die Datei wird in deinem **Downloads-Ordner** gespeichert.

So sieht das aus:

![Downloads](images/02_downloads_folder.png)

---

# 📦 Schritt 3: Kojo ZIP entpacken

Rechtsklick auf **Kojo_2_9_34.zip**  
Dann klicke auf **Alle extrahieren…**

![Kojo ZIP](images/03_kojo_zip_rechtsklick.png)

---

# ☕ Schritt 4: Java ZIP entpacken

Rechtsklick auf **microsoft-jdk-21.0.10-windows-x64.zip**  
Dann klicke auf **Alle extrahieren…**

![JDK ZIP](images/04_jdk_zip_rechtsklick.png)

---

# 📁 Schritt 5: Kojo-Ordner öffnen

Gehe in den Ordner:  
`%userprofile%\Downloads\Kojo_2_9_34\Kojo-z\bin`

So sieht der Ordner aus:

![Kojo Speicherort](images/06_kojo_bin_pfad.png)

---

# 🛠 Schritt 6: kojo.cmd bearbeiten

Rechtsklick auf **kojo.cmd** → **Im Editor bearbeiten**

![kojo.cmd öffnen](images/07_kojo_exe_start.png)

Dort steht eine Zeile mit einem Java-Pfad.  
Ersetze den Java-Pfad durch diesen:

`%USERPROFILE%\Downloads\microsoft-jdk-21.0.10-windows-x64\jdk-21.0.10+7\bin\java`

So sieht das aus:

![kojo.cmd bearbeiten](images/05_kojo_cmd_edit.png)

---

# ▶️ Schritt 7: Kojo starten

Doppelklicke auf **kojo.cmd** im selben Ordner. Kojo startet jetzt mit dem richtigen Java.

---

# 🌍 Schritt 8: Sprache auf Englisch umstellen (wichtig)

Damit alle im Kurs dieselben Menues und Begriffe sehen, stellen wir Kojo **immer auf Englisch** um.

Klicke in Kojo auf: **Sprache → Englisch**

![Sprache auf Englisch](images/08_sprache_englisch.png)

![Kojo neu starten nach Sprachwechsel](images/09_sprache_englisch_neustart.png)

Danach musst du Kojo **selbst schliessen** und **neu starten**.

---

# ✅ Fertig!

Jetzt kannst du mit Kojo programmieren! 🎉
