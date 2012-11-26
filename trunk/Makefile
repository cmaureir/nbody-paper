TEXFILE=nbody-paper

all:
	rubber -d ${TEXFILE}
	@if [ ! -d ../publish ];then mkdir ../publish;fi
	@mv ${TEXFILE}.pdf ../publish/

clean:
	rubber --clean ${TEXFILE}

distclean: clean
	rm -rf ../publish
x:
	okular ../publish/${TEXFILE}.pdf &> /dev/null &

.PHONY: all clean distclean
