PD=pandoc

.PHONY: slides

default: rebuild

###
### build the tool
###

rebuild:
	stack clean
	stack build

build:
	stack build

buildw:
	stack build --file-watch


###
### generates site
###
freizl:
	stack exec freizl build

watch:
	stack exec freizl watch

refreizl:
	stack exec freizl clean
	stack exec freizl build

########## Mirror to github

deploy:
	stack exec freizl build
	cp -r _site/* ../

########## Compile slides

## just being lazy not to cut off md file ext.
slides:
	for f in `ls -1 slides/*.md`; do \
	$(PD) -t dzslides -s "$$f" -o "$$f".html; \
	done;
