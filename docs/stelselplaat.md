---
title: Stelsel van registers
---

# Stelsel van registers

![Diagram](stelselplaat.drawio.svg)

Een register bevat gegevens over een bepaalde verzameling dingen in de werkelijkheid. Grijsgekleurde registers worden extern beheerd en behoren veelal tot het [Stelsel van basisregistraties](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/).

Een relatie tussen twee registers betekent dat in het berichtenverkeer vanuit het ene register wordt verwezen naar gegevens in het andere register. Dit gebeurt aan de hand van zogenaamde verwijssleutels zoals EAN-codes. De richting van de pijl geeft aan in welk register de relatie wordt onderhouden. Zo wordt de relatie tussen meetinrichting en aansluiting onderhouden in het meetinrichtingenregister. Omwille van overzicht zijn de relaties naar de bronhouder (telkens een marktpartij) niet afgebeeld.

Welke registers gegevens bij elkaar opvragen, is niet afgebeeld. Zo vraagt bijvoorbeeld het energietoerekeningsregister gegevens op bij het energie-uitwisselingsregister, maar zonder ernaar te verwijzen in het berichtenverkeer.

Van sommige registers is een conceptueel informatiemodel beschikbaar via het navigatiemenu.

## Relatie naar NBility
Onderstaande tabel toont de relatie met [NBility](https://nbility-model.github.io/).

| Register | NBility v2.2 |
| :--- | :--- |
| Aangeslotenenregister | C.6.2.1. Aansluitingen/allocatiepunten beheren<br/>(gebruikt C.1.1.4. Relatie met klanten onderhouden) |
| Aansluitingenregister | C.6.2.1. Aansluitingen/allocatiepunten beheren<br/>(gebruikt C.3.1.8. Opdracht voor uitvoeren van netaanpassing verstrekken, bewaken en administratief verwerken) |
| Energiediefstalregister |C.1.4.5. Energiediefstal bestrijden |
| Installatieregister | C.6.2.2. Installaties achter aansluitingen beheren |
| Marktactiviteitenregister | C.6.3.1. Marktprocedures uitvoeren |
| Marktpartijenregister | C.6.1.1. Relatie met marktpartijen onderhouden |
| Energie-uitwisselingsregister | C.6.3.3. Energie-uitwisseling vaststellen |
| Energietoerekeningsregister | C.6.3.4. Energie-uitwisseling toewijzen aan marktpartijen |
| Meetinrichtingenregister | C.6.2.1. Aansluitingen/allocatiepunten beheren<br/>(gebruikt C.3.1.8. Opdracht voor uitvoeren van netaanpassing verstrekken, bewaken en administratief verwerken) |
| Metingenregister | C.4.2.3. Metingen beschikbaar maken |
| Regelbaar-vermogenregister | C.6.3.5. Opregel- en afregelbehoefte communiceren<br/>C.6.3.6. Opregel- en afregelaanbod beheren |
| Tarievenregister | C.6.2.1. Aansluitingen/allocatiepunten beheren<br/>(gebruikt C.1.2.3. Producten en diensten ontwikkelen en beheren) |
| Toestemmingenregister | C.6.4.3. Toestemmingen beheren |
