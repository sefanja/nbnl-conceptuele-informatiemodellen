---
title: Modelleren in LinkML
parent: Voor modelleurs
nav_order: 2
---

# Modelleren in LinkML

Conventies voor het opstellen van LinkML-YAML-bestanden.

## Basiselementen
- Gebruik `description` voor definitie
- `see_also` verwijst naar definitiebron (bijv. Juriconnect)

## Typen
- Gebruik enkel `Tekst`, `Getal`, `Datum`, etc.

## Mapping
- Gebruik `exact_mappings`, `meaning` voor NBNL- en NL-SBB-referenties

## Tools
- Validatie met `linkml-lint`
- Documentatie genereren met `linkml gen-doc`
