# Skrypt organizujący pliki

## Opis

Jest to prosty skrypt napisany w Pythonie, który organizuje pliki w określone katalogi na podstawie ich rozszerzeń. Można go użyć do automatycznego sortowania plików ze zdjęciami, filmami, dokumentami tekstowymi, plikami zip itp.

## Instrukcje użycia

1. Uruchom skrypt `main.py`.


## Zależności

Skrypt wymaga środowiska Python 3.x oraz biblioteki shutil.

## Struktura katalogów

- `pobrane_pdf/` - Katalog zawierający pliki PDF.
- `pobrane_video/` - Katalog zawierający pliki wideo.
- `pobrane_text/` - Katalog zawierający pliki tekstowe.
- `pobrane_pictures/` - Katalog zawierający pliki ze zdjęciami.
- `pobrane_zip/` - Katalog zawierający pliki spakowane.
- `pobrane_exe/` - Katalog zawierający pliki wykonywalne.
- `inne/` - Katalog zawierający pliki, które nie pasują do żadnej z powyższych kategorii.

## Przykłady

```bash
python main.py
