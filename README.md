# Project AI: ASHI&DAVID
Project for CPE106L - B3  
  
<p align="center">
  <img width="max" height="max" src="/Imgs/project_ai.png">
</p>
 
<br />

 | Project Members | Position |
| --- | :---: |
| Capuno, John Cedric | Backend |
| Dionisio, Maria Annegela C. | Backend | 
| Montecillo, Carl Lemuel Z. | Backend |
| Nerpio, Rayden Vincent M. | Backend |
| Selda, Jose Mari S. | Backend |
| Tapado, Edward Hannes M. | Full Stack |
 
<br />

**Requirements**  
• [requirements.txt](requirements.txt)  
• [Nircmd](https://www.nirsoft.net/utils/nircmd.html)  


**Running the Program**  
1. Install all requirements
2. Run in terminal 'python main.py'  

# [USER MANUAL](https://bit.ly/3f8Yuav)

# Project Documentation
Written by:  
• Capuno, John Cedric  
• Montecillo, Carl Lemuel Z.
• Selda, Jose Mari S.  
• Tapado, Edward Hannes M.  

# Introduction
  With the advancements and breakthroughs made in technology over the current generation, Artificial Intelligence or AI is widely being utilized to aid humans towards improving the lives of individuals through technology. Creating a machine with AI nowadays have several purposes. Some AIs are used for industrial purposes such as creating machines. With the aid of AIs, they are able to adapt to certain or various environments wherever they are placed. One example is "Curiosity" - the rover that was sent to Mars to explore the crater Gale. Some AIs are utilized for human services, like Alexa or other voice recognition AIs. She can help with searching for information on the internet without typing. You can also set reminders with Voice Recognition. For this project the group of students have created a simple AI that can help users with some basic necessities while using their pesonal computers.  
  
# Purpose  
• To help organize calendar reminders    
• To aid opening and managing applications in the computer  
• To give access to computer's miscellaneous just by speaking or writing  
• Gain access on wolfram 
• Check weather on different places based on the user's query  
• search something on the internet like google and youtube  
• Allows the user to add and get data from database  

**Scope**
  
  • For the creation of the application: The project only includes VsCode, python interpreter, anaconda, MySQL  
  • For the user: This software can be used by all for their personal use. It can only be utilized with its functions within the computer. It also does not gather the user's personal information.  
  
**Definitions, Acronyms, and Abbreviations**  
• **Google Calendar API** - This API allows you to sync and get data from your google calendar.  
• **Wolfram Alpha**  - This API returns an answer based on the query of the user. You can get answer based on these topics (Math, Science, Social, Culture, and Everyday Life).  
• **Open Weather API** - This API gives you access to their weather monitoring system.  


**Overview**  
  The students created a program that utilizes speech recognition to create an assistant for daily use. The students used the knowledge they obtained from their Software Design Course, and created a project that helps users to accomplish tasks easier. The program reacts to sound and does tasks whenever hearing sound that has a corresponding function.
# Use Cases #  

**Actors**  
    • Customer Users - The customers are the users that will benefit from the software. They will be able to utilize it for same reasons but can be for different purposes which are: (1) Set reminders via google calendar, (2) Open other applications, and (3) Write and read in notepad.   
    • Software Developer -  The software developers created the program using AI or Artificial Intelligence that recognizes speech which has functions linked to it. They are in charge of the which applications will have functions linked to them, and the database management. 
  
# List of Use Cases #  
  - User Use Cases
    - Display Status (Overview)
      - The user wants to see the overview of the program, thus the application will show a Command prompt user interface.
    - Display Data 
      - The user wants to search in the web, then the application will show results from queries that will be shown in the command prompt. 
      - If it is an online query, the default browser will be launched and the online results will be shown.
    - Calendar Reminders
      - If the user wants to create calendar reminders, the application will set reminders on Google Calendar. 
      - The user will also be given notifications about upcoming reminders in the Google Calendar.
    - Questions
      - If the user asks a question, the application will return an answer from Wolfram's cloud.
  
## [Use Case Diagram](https://mymailmapuaedu-my.sharepoint.com/:i:/g/personal/etapado_mymail_mapua_edu_ph/EZFgzrJYj39Fqg-DOBc3icoBbtX4C912Nm1-XUPrqL06bQ?e=m9TvNb)  

**Use Cases**  
  - **Brief Description:**  
      - The use case describes the main interface of the software application. It shows the flow of the program from when the user starts to run it and starts asking some queries. The dynamic queries such as the temperature of a certain place or asking to solve some mathematical equations will be taken over by the API and will handle the user's queries. The user can access the database by saying or using the *add command*. After all the queries of the user has been handled, the terminal will show the answer on the user's query.  
  - **Goal:**  
      - To provide answers to the user's queries.  
  - **Trigger:**  
      - The user has two options for the program. They can either speak their query or they can type their query.
  - **Typical Flow of Events:**  
      1. A window is generated and another window will be generated once *add command* is entered.
      2. The data is pulled from database and websites using API.
      3. The user views the answer on their queries on the terminal.
# Design Overview

**Introduction**
In this section we will discuss the design overview of the application. The application will have a graphical user interface (GUI), interaction, database, API, synthesizer, recognizer, and google calendar authenticator. The main control of the application will be the GUI where user can input their queries via typing or speaking. The user's queries can be answered by hard-coded answers or by APIs. The user can also add some commands and response to the database.  

# System Interfaces #   
• User Interface - The program starts with the Windows Assistant greeting the user. Then they can type any command within the applications scope and will execute it. The user can also use the write mode feature by typing in the program's console or voice mode by talking while the program is listening to execute the user's commands. One feature command is that the user can set a reminder on a date and the program can fetch for the user any time and on the exact day and time of the reminder.  

# Constraints and Assumptions #  
• **List Assumptions**  
    - It is assumed that the database is in MySQL format.  
• **List of Dependencies**  
    - The application requires python 3.7 to run. All modules will be included in the requirements.txt.  

</br>  

