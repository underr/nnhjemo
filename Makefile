html:
	python nnhejmo.py

clean:
	rm index.html

watch:
	wendy -m 8 links.ho -f tmpl.html -e make

update:
	git pull && python nnhejmo.py
