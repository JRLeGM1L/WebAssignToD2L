Please read.

These programs were designed to create a file to be uploaded to D2L with the student's WebAssing grades.
I am sharing this file hoping that it will make the rather tedious process of updating the D2L gradebook with
WebAssign scores a bit faster. During the Spring 2024 semester, I used this software and it made my life easier.
That being said, the programs were not created with the intention of sharing, and therefore they are not very robust. They worked for me and I am sharing the 'as is'.

Here are a few points to note.

1. The programs run well on a Unix or Linux machine. I did not bother to try them on a Windows machine and
I highly suspect they won't work, simply because of the bash scripts and the file paths.

2. There are three bash scripts and a Python file to which you need to give execution permissions. You only need to do this once. In the corresponding folder, type the following: chmod 744 <name_of_file>
For example, in the WebAssignGradeToD2L folder you will type chmod 744 move_files.sh
Do the same for the main.py and the other two bash scripts in D2LFiles folder and WebAssignFiles folder.

3. The move_files.sh script moves the last two files that were added to your Downloads folder to their respective folder. If you have not messed with your computer, documents downloaded from the internet will be saved in the Downloads folder by default. If you have changed this, modify the script accordingly.
On that same note, the very first thing you need to do is download two files: One from WebAssign with the scores, and one from D2L. It is important to do that in the following way, to avoid errors.

  - On D2L, go to Grades>Enter Grades>Export. Make sure NONE of the User Details boxes is checked. Also make sure you are only selecting the WebAssign activities that already have a score in WebAssign, and that you select all of them.
Stated otherwise, there must be a bijection between the set of WebAssign activities with grades and the set of grades on D2L you will update.

  - Both of the files you download, the one from WebAssign and the one from D2L, must be .csv files.

4. The file you upload to D2L is called Uploadable+date.csv. This helps keep a record of what was done when in case you want to check something later.

5. You need to have python installed on your machine. To check if you do, open a terminal and type python3 and press enter. If you see Python 3.x.x then you have it. Otherwise you need to install it. However, I think that Macs have python intalled by default, and the departments chivo machines (which all run linux) certainly have Python installed.
   
5. Finally, there are several ways to run the program. The easiest is to type ./main.py on the terminal in the WebAssigGradesToD2L folder.
6. 
