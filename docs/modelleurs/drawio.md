---
title: Modelleren in draw.io
parent: Voor modelleurs
---

# Modelleren in draw.io
{: .no_toc }

Voor het tekenen van conceptuele informatiemodellen gebruiken we [draw.io](https://www.drawio.com/). Deze tool is gekozen omdat ze vrij beschikbaar is, makkelijk in gebruik, en goed samenwerkt met versiebeheer via GitHub. Draw.io ondersteunt de notatiestijl die wij hanteren voor conceptuele informatiemodellen: entiteit-relatienotatie in Barker-stijl.

## Inhoud
{: .no_toc .text-delta }
1. TOC
{:toc}

## Beginnen met draw.io

1. Ga naar [drawio.com](https://www.drawio.com/) en kies voor de online of desktopversie (**Start** of **Download**).
2. Kies voor **Nieuw diagram aanmaken**.
3. Typ een bestandsnaam, selecteer **Bewerkbaar vector-bestand (.svg)**, kies **Blanco diagram** en klik op **Aanmaken**.
4. Klik op **Meer vormen** en vink aan: **Algemeen** en **Entiteitsrelatie**. Klik daarna op **Toepassen**.
5. Klik op **Weergave** en vink **Paginaweergave** en **Hulplijnen** uit.
6. Klik alvast op **Bestand**, **Opslaan** zodat je je werk niet verliest.

Je bent nu klaar om te gaan tekenen! Uh... modelleren.

## Notatiestijl

Voor de notatie van onze diagrammen gebruiken we, net als [Salesforce](https://architect.salesforce.com/diagrams/framework/data-model-notation), in de basis de [Barker-notatie](https://vertabelo.com/blog/barkers-erd-notation/), vanwege de compacte en goed leesbare weergave van entiteiten en relaties. Waar draw.io Barker niet volledig ondersteunt, vallen we terug op elementen uit de [Information Engineering (IE) Notation](https://medium.com/@ericgcc/dont-get-wrong-explained-guide-to-choosing-a-database-design-notation-for-erd-in-a-while-7747925a7531#918d), die visueel en inhoudelijk goed aansluit. Deze combinatie biedt voldoende expressiviteit voor conceptuele modellen, zonder te vervallen in technische details.

## Vormgeving

De links in bovenstaande paragraaf leggen de notatiestijl gedetailleerd uit. Het diagram hieronder toont welke stijlkeuzen we hebben gemaakt in draw.io.

![Aansluitingenregister]({{ site.baseurl }}/modellen/registers/aansluitingenregister/1.1.2/model.drawio.svg)

Enkele elementen lichten we eruit. Voor bijna elk punt is het achterliggende principe: visuele rust en duidelijkheid!

## Naamgeving

- We gebruiken de Nederlandse spellingsregels. Dus geen PascalCase of snake_case.
- Entiteiten worden aangeduid in het enkelvoud, en moeten een bruikbare meervoudsvorm hebben volgens het woordenboek. Dus geen `Suiker`, maar wel `Suikerklontje`.
- Entiteiten beginnen met een hoofdletter, eigenschappen en relaties met een kleine letter.

## Positionering

- Alle elementen zijn uitgelijnd op een raster, met consistente afstanden tussen de entiteiten.
- Entiteiten lijnen op elkaar uit. Zie bijvoorbeeld de hoge `Aansluiting` en het brede `Overdrachtspunt`.
- Lijnen zijn alleen horizontaal en verticaal. Ze mogen niet kruisen of knikken.
- Bij een-op-veel-relaties staat de entiteit aan de een-zijde standaard links of boven.
- De positie van een relatienaam bepaalt de leesrichting en staat dichtbij de entiteit die haar beheert. Bijvoorbeeld: een `Aansluiting` is `deel van` een `Netgebied`.

## Kleuren

- Entiteiten hebben een [NBility](https://nbility-model.github.io/)-kleur.
- Entiteiten uit andere registers zijn grijs en hebben geen eigenschappen of uitgaande relaties.

## Structuur

- Een entiteit wordt geïdentificeerd door een combinatie van eigenschappen en relaties (aangegeven met een `#`). Zo wordt een `Aftakking` geïdentificeerd door de combinatie van `zijde`, `nominale waarde`, `serienummer` (`Meettransformator`) en `identificatie` (`Primair deel meetinrichting`).
- Specialisaties zijn weergegeven met nesting. Dit maakt overerving van eigenschappen en relaties intuïtief.
- Specialisaties zijn volledig en niet overlappend. Dus elke `Meettransformator` is óf een `Spanningsmeettransformator` óf een `Stroommeettransformator`. Merk op dat de notie van 'abstracte klasse' (zonder instanties) niet kan bestaan in een conceptueel model.
- Een `OF`-boog geeft aan dat slechts één van de relaties geldt.
- Een `en/of`-boog geeft aan dat minimaal één van de relaties geldt.
- Bij een groot model worden 'submodules' gekaderd.

## Symbolen

- `#` voor identificerende eigenschappen en relaties
- `●` voor essentiële (of 'verplichte') eigenschappen
- `○` voor accidentiële (of 'optionele') eigenschappen
- `/` voor entiteiten, eigenschappen of relaties die logisch of computationeel afleidbaar zijn uit andere elementen in het model
- `⏲` voor tijdslijnmarkeringen (zie [Tijdlijnen in conceptuele modellen](tijdlijnen))
