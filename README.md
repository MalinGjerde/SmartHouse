

1. Begynn med å lese nøye gjennom [Problembeskrivelsen](https://github.com/selabhvl/ing301public/blob/main/project/index.md) og lag deretter en _domenemodell_ (klassediagramm) av det hele.
   Du skal lage forskjellige klasser for de foskjellige enhetene. Inkluder også de klassene som allerede finnes i `smarthouse/domain.py`.
   Du kan tegne klassedigramm enten på ark/whiteboard (husk å scanne det etterpå eller ta bildet) eller et grafisk verktøy som [diagrams.net](https://www.diagrams.net/) eller [Figma](https://www.figma.com/).
   Klassediagrammet skal lagres enten som PDF eller bildefil (`.jpg`, `.png`, `.svg`) og lastes opp i roten til repo'en med navn `domainmodel.<filtype>` (dette skal være deres første egen commit!). 
2. I neste steg skal klassediagrammet dere har laget oversettes til konkrete klasser i Python ved å utvide `smarthouse/domain.py` filen. 
   Dere betyr at dere skal legge til klasser som representer rom, etasjer og de forskjellige type enheter. 
   Tenk på hva slags attributter (dvs. de som settes i konstruktor: `__init__`-funskjonen) og _metodene_ (funksjoner innen en klasse) hver enkelt klasse trenger.
3. Som neste steg anbefaler vi at dere tar en kikk på klassen `SmartHouse` i `smarthouse/domain.py`: Her finner dere en rekke funksjoner som mangler en korrekt implementasjon.
    Deres oppgave er å skrive funksjonaliteten til hver enkelt funksjon som det er beskrevet i kommentaren ved å bruke deres nylagte klasser.
4. Etterpå kan dere begynne å legge inn et "Demo Hus" som er beskrevet på [denne siden](https://github.com/selabhvl/ing301public/blob/main/project/demo.md). Dette skal gjøres i files `tests/demo_house.py`
    ved å bruke de forskjellige `register_`-funskjonene i `SmartHouse` som dere har nettop implementert. 
5. Til slutt gjenstår det å få alle tester i `tests/test_part_a.py` til å bestå. Sjekk implementasjonskravene nedenfor for å sjekke 
    om dere eventuelt trenger å utvide klassene deres om noen attributter eller metoder. 


### Implementasjonskrav

I de gitte Unit-testene forventes det at objekter som representerer enheter tilbyr spesifikke funksjoner, konkret:

- Alle enheter skal minst følgende attributter: `id`, `supplier`, `model_name` som inneholder den tekniske identifikatoren,
  produsentnavn og modellnavn
- Alle enheter skal minst tilbyr følgende metoder: `is_actuator()`, `is_sensor()`, og `get_device_type()`. Førstnevnte 
 returnerer en boolsk verdi som gir uttrykk for om enheten er en aktuator eller en sensor. Sistnevnte funksjon returnerer en 
 tekst (`str`) som beskriver hva konkret type enhet det er, f.eks `Heat Pump`, `Smart Lock`, osv.
- Alle sensorer skal tilby en metode `last_measurement` som returnerer en objekt av type `Measurement`. Målenheten i målingen
 skal samsvare med måleenheten av sensoren (f.eks. måler en temperaturmåler in enheten celsius: `"°C"`). For verdien kan du velge 
 en helt tilfeldig numerisk verdi (du kan f.eks. bruke [random modulen](https://docs.python.org/3/library/random.html)) og `timestamp`
 skal være en tekstuell representasjon av et tidspunkt (du kan f.eks. bruke [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)).
- Alle aktuatorer skal tilby metodene: `turn_on()`, `turn_off()`, `is_active()`. Sistnevnte skal returnere `True` hvis enheten har blitt slått 
 på med `turn_on()`. Tar også hensyn til at visse aktuatorer kan også gis et "`target_value`" (f.eks. panelovn eller varmepumper kan settes til en ønsket temperatur).

Ta gjerne en titt i [testfilen](https://github.com/selabhvl/ing301-projectpartA-startcode/blob/main/tests/test_part_a.py) for å sjekke hvilke funksjoner forventes av deres domenemodell.

