---
title: Modelleren in Drawio
parent: Voor modelleurs
---

# Modelleren in draw.io
{: .no-toc }

Voor het tekenen van conceptuele informatiemodellen gebruiken we [draw.io](https://www.drawio.com/). Deze tool is gekozen omdat ze vrij beschikbaar is, makkelijk in gebruik, en goed samenwerkt met versiebeheer via GitHub. Draw.io ondersteunt de diagramnotaties die we nodig hebben en maakt het mogelijk modellen visueel en consistent vast te leggen.

## Inhoud
{: .no_toc .text-delta }
1. TOC
{:toc}

## Beginnen met draw.io

1. Ga naar [drawio.com](https://www.drawio.com/) en kies voor de online of desktopversie (**Start** of **Download**).
2. Kies voor **Nieuw diagram aanmaken**.
3. Selecteer **Blanco diagram** en klik op **Aanmaken**.
4. Klik op **Meer vormen** en vink aan: **Algemeen** en **Entiteitsrelatie**. Klik daarna op **Toepassen**.
5. Klik op **Weergave** en vink **Paginaweergave** en **Hulplijnen** uit.
6. Klik alvast op **Bestand**, **Opslaan** zodat je je werk niet verliest.

Je bent nu klaar om te gaan tekenen! Uh... modelleren.

## Notatiestijl
Voor de notatie van onze diagrammen gebruiken we, net als [Salesforce](https://architect.salesforce.com/diagrams/framework/data-model-notation), in de basis de [Barker-notatie](https://vertabelo.com/blog/barkers-erd-notation/), vanwege de compacte en goed leesbare weergave van entiteiten en relaties. Waar draw.io Barker niet volledig ondersteunt, vallen we terug op elementen uit de [Information Engineering (IE) Notation](https://medium.com/@ericgcc/dont-get-wrong-explained-guide-to-choosing-a-database-design-notation-for-erd-in-a-while-7747925a7531#918d), die visueel en inhoudelijk goed aansluit. Deze combinatie biedt voldoende expressiviteit voor conceptuele modellen, zonder te vervallen in technische details.

## Vormgeving
De links in bovenstaande paragraaf leggen de notatiestijl gedetailleerd uit. Het diagram hieronder toont welke stijlkeuzen we hebben gemaakt in draw.io.

[embed]

Enkele elementen lichten we eruit:

- Alle lijnen zijn horizontaal of verticaal.

## Symbolen
- `#` voor identificerende eigenschappen.
- `●` voor essentiële (of 'verplichte') eigenschappen.
- `○` voor accidentiële (of 'optionele') eigenschappen.
- Tijdslijnmarkering

## Kleuren
- NBility-kleuren
- Externe registers
- Niet aanpasbaar

## Structuur
- Nesting bij specialisaties
- Verwijzingen naar externe registers
