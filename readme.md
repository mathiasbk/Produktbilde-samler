# Produktbilde-samler

Et enkelt Python-script for å kopiere produktbildemapper basert på produktnumre.

## Beskrivelse

Dette scriptet søker gjennom en spesifisert mappe med produktbilder og kopierer hele mapper som matcher angitte produktnumre til en destinasjonsmappe.

## Funksjonalitet

- Søker rekursivt gjennom en kildemappe etter mapper med navn som matcher produktnumre
- Kopierer hele mapper (inkludert alt innhold) til en destinasjonsmappe
- Støtter flere produktnumre samtidig (kommaseparert)

## Bruk

1. Kjør scriptet:
   ```
   python main.py
   ```

2. Når prompted, oppgi:
   - **Output path**: Stien til hvor du vil kopiere bildene
   - **Produktnumre**: Kommaseparerte produktnumre (f.eks: "610,639,641")

## Eksempel

```
Enter output path: C:/temp/produktbilder
Enter productnumbers. Comma sepparated: 610,639,641
```

## Forutsetninger

- Python 3.x
- Tilgang til kildemappe og destinasjonsmappe

## Notater

- Kildemappe er hardkodet i scriptet og må endres hvis nødvendig
- Scriptet overskriver eksisterende mapper i destinasjonen
