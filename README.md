# Create folders

## Introduction

Many times you have to create a list of folders starting from a menù or a list of topics. The idea is to run an exe file from any folder on the PC and paste in the command window the folders name you want to create. An option to enumerate the folders would be handy 

## Software and Libraries

This project uses Python 3.8.5 and the following libraries:
* [pyinstaller](https://www.pyinstaller.org/)
* [argparse](https://docs.python.org/3/library/argparse.html)

## Build

To build the .exe file and place it in **%USERPROFILE%\AppData\Local\Programs\Python\Python38\Scripts** you have to run `deploy.cmd`

## Running the code

From any folder of your PC you can open a command promt and run `create_folders.exe`, then you have to paste the list of folder you want to create in the current folder. You can also use the `create_folders.exe --enumerate` to enumerate the folders and `create_folders.exe -h` to view the help

![example](images/example.PNG)

## Acknowledgements

Thank you
