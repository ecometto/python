DESCRIPTIONS:
This script download PassScripts from NFS (import directory 2024).
Then ask about the "day of year" sub-directory, according to:
	- make modifications in .scl files (date and time format) 
	- analice type of pass (main/backup), AOS, LOS and quantity of TT

After modify each .scl file, new data is saved with the same name.


---------------------------------------------------------------
ACTIONS:

* Copy and paste all the directory 'seeMainOrBackup'

* Go to this directory

* Execute: >> python seeMaionOrBackup.py

* See the file log.txt to see "main" or "backup" type Pass
