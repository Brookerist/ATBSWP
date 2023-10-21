To install:
(1) Place this folder (mcb) inside the user's HOME directory. (ex. c:\users\<Username>)
(2) Place a copy of mcb.bat into the user's home folder.
(3) Add user's home folder to Path. This allows mcb to be called from Run dialog.

#############################
To add folder to Path, 
- press /Win Key + R/ to open Run dialog
- type sysdm.cpl to open system properties
- open the Advanced tab 
- click "Environment Variables" near the bottom
- in 'User variables for <username>' box, select 'Path' and click "Edit"
- click "Browse" and select your home folder 
	(Typically your name or username)
- click "OK" and ensure the folder has been added to the list
- close these windows using "OK"
#############################

mcb usage: 
	Open Run dialog with /Win Key + R/	
	mcb save <keyword> - saves current clipboard to keyword.
        mcb <keyword> - Loads keyword text to clipboard.
        mcb list -  Loads all keywords to clipboard. 
	list is helpful if you've forgotten your keywords