Dear users,
the exampleInstaller.flw installs files to the following locations:

1. MyFirstBundle

In your FL's Macros folder:
	Mark/Blue.py
	Mark/Green.py
	Mark/Red.py
	System/Modules/Mark/Mark.py
It also produces Mark.pth file in your Python's site-packages
to add the previous path to the Mark.py module to the Python environment.

2. MySecondBundle
This one is here just to show you can transfer binary files as well.

In your FL's Macros folder:
	Dilbert/dilbert.png
	Dilbert/dilbert.py
	Dilbert/README.txt (it is this README)



Dear programmers,

the exampleInstaller.flw was produced with the buildInstaller script:

$ buildInstaller exampleInstaller.yaml exampleInstaller.flw

using enclosed files.