rem Build the executable file and place it in the python Scripts folder

pyinstaller --onefile -c "create_folders.py"

copy dist\create_folders.exe %USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts