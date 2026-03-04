# Kojo Aufgabenblatt 4: Picture-Welt

Wenn ihr weitermachen wollt, könnt ihr euch die **Picture-Welt** aussuchen.

## Wiederholung des Befehlsvorrats

1. Starte die Dokumentation des Befehlsvorrats (Menü Tools->Instruction Palette)
2. Wähle "Live help: On"
3. Wähle ganz oben: "Picture"

<img src="images/aufgaben04_02_picture_commands.png" alt="Picture Befehle" width="400">

4. Halte den Mauszeiger über `Picture.rectangle(w, h)` und `Picture.text(w, h)`.
Kombiniere die zwei Beispielprogramme mit dem Text "Klasse 5" in Schriftgröße 30 zu:

<img src="images/aufgaben04_klasse5.png" alt="Picture Befehle" width="150">

5. Wähle ganz oben: "Picture Transforms"

6. Halte den Mauszeiger über `trans(f)` und `rot(a)`.
Kombiniere die zwei Beispielprogramme zu:

<img src="images/aufgaben04_trans_rot.png" alt="Picture Befehle" width="400">

Tipp:
- In den Beispielen unterscheidet sich nur die vorletzte Zeile.

7. Was die Instruction Palette nicht verrät: Man kann mit `scale(fx,fy)` ein Objekt auch verzerren (z.B. Raute),
und man kann mehrere Veränderungen mit `*` auf das gleiche Objekt anwenden:

```scala
cleari()
val rechteck = Picture.rectangle(50, 50)
val vollesRechteck =
  fillColor(lightGray) -> rechteck
draw(scale(2,1) * rot(45) -> vollesRechteck)
```

Tipp:
- Links von `->` steht die Veränderung
- Mehrere Veränderungen sind durch `*` getrennt
- Zwischenständen kann man mit `val` Namen geben

8. Der Fantasie beim Verändern von Kreisen, Linien und Rechtecken sind beim
Zusammensetzen keine Grenzen gesetzt:

```scala
cleari()
val koerper = Picture.rectangle(10, 50)
draw(koerper)
val kopf = Picture.circle(10)
draw(trans(5,60) -> kopf)
val linker_arm = Picture.line(40, 30)
draw(trans(10,30) -> linker_arm)
val rechter_arm = Picture.line(-40, 30)
draw(trans(0,30) -> rechter_arm)
val bein = picCol(
  Picture.ellipse(15, 5),
  trans(10,0)->Picture.ellipse(5, 15)
)
draw(trans(-15,-30) -> bein)
draw(flipY * trans(-25,-30) -> bein)
```

9. Schleifen helfen ungemein, viel Tipparbeit zu sparen:

```scala
cleari()
val karte =
  fillColor(green) -> Picture.rectangle(50, 80)
for (i <- 1 to 4) {
  for (j <- 1 to 2) {
    draw(trans(i*70 - 200,j*100 - 100) -> karte)
  }
}
```

## Beispielprogramme

Kojo hat viele Beispielprogramme. Das ist toll, um Ideen zu bekommen, was man programmieren könnte.
Allerdings ist der Programmcode oft sehr lang und kompliziert.
Im Folgenden sind kurze Programmstücke aus den Beispielen geholt, die ihr verstehen könnt:

### Picture Beispiel 1: Auto mit Tastatur steuern

<img src="images/aufgaben04_car.png" alt="Gruener Kreis" width="300">

```scala
val auto=Picture.image("/media/car-ride/car1.png")
cleari()
draw(auto)
activateCanvas()
animate {
  if (isKeyPressed(Kc.VK_LEFT)) {
    val pVel = Vector2D(-3, 0)
    auto.translate(pVel)
  }
  if (isKeyPressed(Kc.VK_RIGHT)) {
    val pVel = Vector2D(3, 0)
    auto.translate(pVel)
  }
}
```

### Picture Beispiel 2: Mausklick auf Karte als Vorbereitung für Memory

<img src="images/aufgaben04_memory.png" alt="Gruener Kreis" width="300">

```scala
def zeige_nummer(
  x: Double, y: Double,
  mouse_x: Double, mouse_y: Double) {
  draw(trans(x+20, y+60)
    -> Picture.text("1", Font("Serif", 30)))
  draw(trans(mouse_x, mouse_y)
    -> Picture.ellipse(3,3))
}

cleari()
val karte
  = fillColor(green) -> Picture.rectangle(50, 80)
for (i <- 1 to 4) {
  for (j <- 1 to 2) {
    val x = i*70 - 200
    val y = j*100 - 100
    val verschobene_karte = trans(x,y) -> karte
    verschobene_karte.onMouseClick(
      (mouse_x, mouse_y)
      => zeige_nummer(x, y, mouse_x, mouse_y)
    )
    draw(verschobene_karte)
  }
}
```
