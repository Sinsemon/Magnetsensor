# Magnet Sensor
# Ziel

Ziel ist es einen möglichst leichtgewichtigen Sensor zu bauen, der feststellt ob ein Fenster/Tür oder
ähnliches offen ist. Nach einer zuvor festgelegten Zeit soll der/die Nutzer*in über ein Tonsignal benachrichtigt das
Fenster oder die Tür zu schließen. Der Sensor selbst soll dabei bewusst keine Internet Anbindung haben.
## MVP

- [x] Messen ob Fenster offen
- [x] Timerfunktion mit einstellbarer Zeit
- [x] Zeitanzeige über Display
- [x] Drehregler zum Einstellen (~30s Schritte) (alternativ Taster)
- [x] Alarm bei 0s
- [x] Ausschalten bei -30s
- [x] ALARM wenn Zeit abgelaufen ist

## Optional

- Smart Home Anbindung über evtl. ZigBee

# Einkaufsliste

- 3x [ESP8266](https://www.amazon.de/AZDelivery-NodeMCU-ESP8266-ESP-12E-Development/dp/B0754HWZSQ?ref_=ast_sto_dp&th=1)
- 3x [OLED Display](https://www.amazon.de/dp/B07BY6QN7Q/ref=twister_B07ZT329J1?_encoding=UTF8&psc=1) oder [LCD Display (relativ groß)](https://www.amazon.de/AZDelivery-HD44780-Display-Schnittstelle-Hintergrund/dp/B079T1BW6T/ref=sr_1_11?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=4KVPL2HHDPWY&keywords=arduino%2Breflective%2Blcd%2Bdisplay&qid=1669644099&sprefix=arduino%2Breflective%2Blcd%2Bdisplay%2Caps%2C81&sr=8-11&th=1)
- 3x [Drehgeber (mit knopf und unendlich drehbar)](https://www.amazon.de/AZDelivery-Drehwinkelgeber-Drehgeber-Encoder-Arduino/dp/B079H3C98M/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3VSB2ZZBWB70V&keywords=potentiometer%2Bazdelivery&qid=1669642393&s=industrial&sprefix=potentiometer%2Bazdelivery%2Cindustrial%2C66&sr=1-4&th=1) oder 1x [Potentiometer](https://www.amazon.de/Aihasd-Adjustment-Single-Linear-Potentiometer-100K/dp/B01NBBAQR0/ref=sr_1_6?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2T874AOTIDJP1&keywords=potentiometer%2B100k&qid=1669642783&s=industrial&sprefix=potentiometer%2B100k%2Cindustrial%2C116&sr=1-6&th=1)
- evtl [Taster (zum löten)](https://www.amazon.de/Youmile-100er-Pack-Miniatur-Mikro-Taster-Tastschalter-Qualit%C3%A4tsschalter-Miniature-6-x-5-mm/dp/B07Q1BXV7T/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=AGIGZAUYAMVW&keywords=arduino+taster&qid=1669642977&s=industrial&sprefix=arduino+taste%2Cindustrial%2C123&sr=1-5) oder [Taster zum stecken](https://www.amazon.de/AZDelivery-KY-004-Schalter-Schl%C3%BCsselschalter-Arduino/dp/B07DPSMRJ6/ref=sr_1_20?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=AGIGZAUYAMVW&keywords=arduino+taster&qid=1669643122&s=industrial&sprefix=arduino+taste%2Cindustrial%2C123&sr=1-20)
- [Piezo buzzer zum stecken](https://www.amazon.de/AZDelivery-KY-006-Passives-Buzzer-Arduino/dp/B07DPR4BTN/ref=sr_1_6?keywords=piezo+buzzer&qid=1669643272&sr=8-6) oder [Piezo buzzer zum löten](https://www.amazon.de/ARCELI-Elektronische-Magnetic-Dauerton-Arduino/dp/B07RDHNT1P/ref=sr_1_9?keywords=piezo+buzzer&qid=1669643375&sr=8-9)
- [Breadboard mit Kabeln und Netzteil](https://www.amazon.de/AZDelivery-102-Breadboard-Kit-Steckbr%C3%BCcken/dp/B07VC9ZRW1/ref=sr_1_12?keywords=breadboard&qid=1669644482&sprefix=bread%2Caps%2C129&sr=8-12&th=1)
- [Reed schalter mit Magneten](https://www.amazon.de/QUCUMER-Reedschalter-Reed-Schalter-Magnetischer-Induktionsschalter/dp/B097PK2MLT/ref=sr_1_7?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2JBFT7HTXZTKI&keywords=reed+schalter&qid=1669645077&sprefix=reed+schalter%2Caps%2C105&sr=8-7)
# Implementation
Die Implemenation des Projektes findet sich [hier](implementation)

# Dokumentation
Die Implemenation des Projektes findet sich [hier](documentation/documentation.md)