druk: 
	python3 narzedzia/drukuj.py

html:
	python3 narzedzia/drukuj.py --bez-pdf

sprawdz:
	python3 narzedzia/sprawdz.py tresc/plansze-*.md

online:
	python3 narzedzia/eksport_gry.py

.PHONY: druk html sprawdz online
