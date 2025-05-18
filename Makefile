akedit:
	pyinstaller akedit.py
install:
	cp dist/akedit/akedit /usr/local/bin/akedit
	rm -r /usr/local/bin/_internal
	cp -r dist/akedit/_internal /usr/local/bin/_internal
uninstall:
	rm /usr/local/bin/akedit
	rm -r /usr/local/bin/_internal
clean:
	rm -r build dist
	rm akedit.spec
