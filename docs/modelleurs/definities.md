---
title: Definities opstellen
parent: Voor modelleurs
---

# Definities opstellen

Deze pagina beschrijft de richtlijnen voor het formuleren van begripsdefinities binnen het informatiemodel.

## Doel

Definities leggen de betekenis vast van klassen en eigenschappen. Ze maken hergebruik mogelijk en zorgen voor semantische helderheid binnen en buiten het model.

## Praktische richtlijnen

- Schrijf definities in de vorm van een volledige zin, zonder formele logica.
- Gebruik **genus-differentia**: benoem het type en het onderscheid.
- Vermijd circulaire verwijzingen.
- Vermeld bij voorkeur een bron in `see_also`.
- Geef context alleen als die essentieel is voor betekenis.

## Voorbeelden

| Klasse         | Definitie                                                                       |
|----------------|----------------------------------------------------------------------------------|
| Aansluiting    | Een fysiek punt waarop een installatie is verbonden met het net.                |
| Netbeheerder   | Een organisatie die verantwoordelijk is voor het beheer van een energie-infrastructuur. |

## Technische toepassing in LinkML

- Gebruik `description` voor de formele definitie.
- Gebruik `see_also` voor juridische of semantische bronverwijzing.
- Gebruik `annotations` als toelichting of om statussen te markeren (bijv. conceptueel, voorlopig).

## Hulpmiddelen

- Juriconnect
- NBNL-begrippenkader
- NL-SBB
