druk: 
	python3 narzedzia/drukuj.py

html:
	python3 narzedzia/drukuj.py --bez-pdf

sprawdz:
	python3 narzedzia/sprawdz.py tresc/plansze-*.md

.PHONY: druk html sprawdz
