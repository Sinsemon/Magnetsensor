# Funktionsregeln

## Poti

- Drehen des Poti auf 0 -> DeepSleep
- Wenn nicht auf 0 aufwachen und Zeit einstellen.

## Reed

- geschlossen & Poti auf 0 -> nichts
- geschlossen & Poti eingestellt -> Timer starten

## Timer

- Wenn er läuft, nicht mehr Poti lesen außer Poti auf 0
- Wenn abgelaufen & Reed geschlossen Beep für 5 min (nicht unendlich)
- Timer abbrechen, wenn Reed offen


# State Machine

## Off

- Deepsleep

Conditions:
- Idle -> Poti != 0

## Idle

- Poti lesen
- Zeit einstellen

Conditions:
- Off -> Poti == 0
- Off -> nach 2 min
- TimerRunning -> Reed == 1

## TimerRunning

- Zeit läuft
- Beep, wenn Abgelaufen

Conditions:
- Idle -> nach 2 min
- Idle -> Reed == 0
- Off -> Poti == 0