# Project AI: ASHI&DAVID
Project for CPE106L - B3  
  

  
**Project Members**  
  1.  Capuno, John Cedric
  2.  Dionisio, Maria Annegela C.
  3.  Montecillo, Carl Lemuel Z.
  4.  Nerpio, Rayden Vincent M. 
  5.  Selda, Jose Mari S.
  6.  Tapado, Edward Hannes

**Requirements**  
• Python 3.7  
• MySQL  
• Google Calendar Api  
• WolframAlpha API  
• OpenWeather API

**Running the Program**  
1. Install all requirements
2. Run in terminal 'python main.py'  

# [USER MANUAL](https://bit.ly/3f8Yuav)

# Project Documentation
Written by:

# Introduction
  With the advancements and breakthroughs made in technology in the current generation, AI or Artificial Intelligence is widely being utilized to aid humans in further towards improving the lives of individuals through technology. Creating a machine with AI nowadays have several purposes, some AIs are industrial purposes like creating machines with the aid of AIs to make it adapt to certain environments, an example of this is Curiosity - the rover that was sent to Mars to explore the crater Gale. Next, some are utilized for human services, like Alexa, she can help with searching for information in the net without typing, set reminder all with Voice Recognition. For this project the group of students have created a simple AI that can help users with some basic necessities while using their pesonal computers.  
  
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

**Reference**  
  
**Overview**  
  The students created a program that utilizes speech recognition to create an assistant for daily use. The students used the knowledge they obtained in their Software Design Course, and created a project that helps the user to make some tasks easier. The program reacts to sound and does tasks whenever hearing sound that has a corresponding function.
# Use Cases #  

**Actors**  
    • Customer Users - The customers are users who are beneficiaries of the software. They will be able to utilize it for same reasons but can be for different purposes which are: (1) Set reminders via google calendar, (2) Open other applications, (3) Write and read in notepad.   
    • Software Developer -  The software developers created the program using AI, or Artificial Intelligence, that recognizes speech that has functions linked to it. They are in charge of the which applications will have functions linked to them, and the database management. 
  
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
      - This use case describes the main interface of the software application. It shows the flow of the program from when the user starts to run and it and starts asking some queries. The dynamic queries such as the temperature of a certain place or asking to solve some mathematical equations, the API will take over and handle the queries of the user. The user can access the database by saying or writing the *add command*. After all the queries of the user has been handled, the terminal will show the answer on the user's query.  
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

**System Architecture**

# System Interfaces #   
• User Interface - The program starts with the Windows Assistant greeting the user, then the can type any command within the applications scope and will execute it. The user can also use write mode by typing in the program's console or voice mode by talking while the program is listening to execute the user's commands. One feature command is that the user can set a reminder on a date and the program can fetch for the user any time and on the exact day and time of the reminder. 
• Software Interfaces -  
# Constraints and Assumptions #  
• **List Assumptions**  
• **List of Dependencies**  

# System Object Model #  
</br>  

