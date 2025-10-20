---
title: LinkML
parent: Voor modelleurs
---

{: .warning }
Deze website is in opbouw. Pagina's kunnen onvolledige of onjuiste informatie bevatten.

# Modelleren in LinkML

[LinkML](https://linkml.io/) (Linked Modeling Language) is een gestructureerde taal om informatiemodellen op te stellen in YAML-formaat. Het lijkt qua vorm op JSON Schema, maar is gericht op semantische duidelijkheid, herbruikbaarheid en documentatie van concepten.

Wij gebruiken LinkML om onze conceptuele informatiemodellen expliciet, formeel en machineleesbaar vast te leggen, zónder te vervallen in database- of API-techniek. Daarmee kunnen we:

- definities vastleggen in samenhang (klassen, eigenschappen, relaties)
- verwijzen naar standaarden zoals NEN 3610
- consistent documentatie en validatieregels genereren
- tooling gebruiken om modellen te controleren en publiceren

Voor modelleurs betekent dit: we leggen het wat en waarom van het model vast, niet het hoe van de implementatie. LinkML dwingt ons om keuzes expliciet te maken en ondersteunt samenwerking in een versiebeheeromgeving zoals GitHub.

## Versies
Versioneringspatroon `major`.`minor`:

- `major`: verhoog bij wijzigingen waardoor bestaande data niet eenduidig naar het nieuwe model kan worden gemigreerd, zoals een nieuwe verplichte eigenschap zonder duidelijke standaardwaarde.
- `minor`: verhoog bij alle andere wijzigingen met impact op de data.

## Classes
- Gebruik `description` voor definitie
- `see_also` verwijst naar definitiebron (bijv. Juriconnect)

## Typen
- Gebruik enkel `Tekst`, `Getal`, `Datum`, etc.

## Mapping
- Gebruik `exact_mappings`, `meaning` voor NBNL-referenties

## Tools
- Validatie met `linkml-lint`
- Documentatie genereren met `linkml gen-doc`
