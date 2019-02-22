# RoboCar

Greetings!

This was the first semester project that we (a group of 3 people) had to do as students in the IT Technology AP programme at the Business Academy Aarhus. It was a pretty big project consisting of multiple parts/challenges. Below, at the end, I will leave the full description of the assignment given to us by the teachers. The project was also intended to be used in a competition vs the other students and i'm proud to say that we got the first place in both challenges (fastest timing on line following and getting the boxes out). WOOHOO! ![robocar competition scoreboard](https://user-images.githubusercontent.com/47772881/53250000-c7c5f600-36b9-11e9-944e-56a23b9482ce.jpg)


I was in charge of the programming and the developing of the Python code/algorithms for our RoboCar and the code for our Web controlling interface. Of course, to see if my programming was right i also had to test it a lot in the real world conditions and to make adjustments. I only upload the code needed to run the RoboCar for the line following and ultrasound/boxes challenges because that was my main focus in this project. And also some videos/pictures of the RoboCar at different stages in the project.

### Description of the setup

Car chassis with 4 electrical motors, right motors connected in series (same for left). Motors connected to H2 Bridge to control their states (OFF, forward, backward). The inputs (4 in total, 2 for each side) from the H Bridge were outputs for the Raspberry PI 3 Model B+ which was controlled by Python 3.6 code using the GPIO module. Raspberry PI's operating system was Raspbian Stretch Lite (Linux distro no GUI) which we setup for remote management (SSH) and also installed git for pulling or pushing code and an apache2 webserver for the webinterface. We also connected 3 infrared/light detection sensors and 1 ultrasound sensor (for measuring distance) to the Raspberry PI. 

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
## ASSIGNMENT DESCRIPTION


### Purpose of the project

- Carry out a multidisciplinary project combining several courses from the First Semester
- Build a RoboCar to meet the requirements
- Establish and work in a team
- Compete with the other RoboCars
- Present your team’s work in various forms, including a video and an oral presentation
- Write a project report


### Requirements for the RoboCar

The project shall be completed using only electronic hardware and the car chassis provided by the college.
Requirements: a list of items/functionality that the final product is to be able to perform
1) Line following
Complete a line following course, marked with Black tape on standard school White Desktop as specified by the teacher
2) Remote control
Build a web-based remote controller, which allows the robot car to be controlled by a browser interface from e.g. a smartphone, laptop, tablet or other device. As a minimum, commands to drive forwards, backwards, left and right, and to stop shall be provided. This feature shall be used in a football (soccer) competition.
3) Ultrasound/boxes challenge
The RoboCar will start in the middle of the arena, facing towards one of the ends of the arena. Four plastic boxes will be places in fixed spots around the arena. The actual positioning of the boxes will not be known for the competitors before the battle starts.
The challenge is for the RoboCar to locate and push the four boxes out of the arena in the fastest time possible.
The winner will be the RoboCar with the fastest time.
Each team gets two tries to set a best time.


### Requirements for the process

- Establish your team and make a work contract
- Plan the project, show it and control it in Trello
- Make a mid-term status Hand in see Canvas
- Keep a log or dairy


### Requirements for the delivery/hand-in

- Project Report ( Not less than 48000 characters (This is rated as 20 normal pages but more than 20 pages are allowed)
  - You will be provided with guidance on the format and content of the report as part of the project process but it should include:
    - Reflections on your collaboration, your planning and implementation of the project.
      - A technical description of the full system made by the team:
        - A Block Schematic
        - A Full Wiring Diagram
        - A simple Network description
          - IP-number configuration for Client and Server and Gateway
            - Network
            - Netmask
        - Description of the RaspberryPi installation/Configuration
          - What is installed/configured (why and how)
        - Description of the software modules made
          - Purpose
        - Source-Code in appendix
    - Conclusion and lessons learned.


### Requirements for the delivery/hand-in, in connection with the presentation

- YouTube Video (maximum length 3 minutes)
  - This is your opportunity to “sell” your product and tell about all the great features you have built into it.
- Presentation including product demonstration (15 minutes including questions)
  - This presentation will be for the whole class and every group member should take an active part in the presentation.
  - The presentation material should be provided as an electronic presentation : .ppt, .pdf, link to Prezi or some other web-based presentation.


### Competitions. There will be 2 competitions during the project:

1. Practical Competition in the Basement/Cantina/Somewhere else: Line following, ultrasound challenge and a Football competition.

    Rules for the competitions are as follows (in case of doubt, the teachers’ decisions are final and binding):

    - Line Following
        - The RoboCar shall be able to follow a line , using onboard systems and software.
        - No external control is allowed in the line following competition.
        - Credit will be given for the speed with which the task is completed. Hint: Completing the course in the fastest possible time requires that the RoboCar reacts both smoothly and quickly

    - Ultrasound challenge (boxes)
        - The RoboCar will start in the middle of the arena, facing towards one of the ends of the arena. Four plastic boxes will be places in fixed spots around the arena. The actual positioning of the boxes will not be known for the competitors before the battle starts.
        - The challenge is for the RoboCar to locate and push the four boxes out of the arena in the fastest time possible.
        - The winner will be the RoboCar with the fastest time.
        - Each team gets two tries to set a best time.

    - Remote controlled Football Game (soccer)
        - The RoboCar shall be steerable via a network interface hosted on a remote computer.
        - This shall be a Web-based (browser and HTTP) application.
        - Make the car able to interact in a remote controlled football Game. There are a lot of
        different soccer games to be found on the internet (try googling “robot soccer”). This is the first time we will try this, so the rules may not be quite set yet but
        - The football field will be 2x3 meters with sidewalls
        - The cars may use a servocontrolled “kick” device.
        - The goal will be 1 meter wide in each end of the lane
        - There will be two halvs of each 7 minutes (A third half if the score is unsettled)
        - 4 robots on each team and the teams will be set on the day of the game

  **NB: shall = mandatory**

2. Presentations in the Class. You will present your project, including relevant reflections, and show your YouTube video. We will end the presentations with prizes for the best:
    - Teamwork
    - Report
    - Presentation
    - Line following
    - Ultrasound/boxes challenge
    - YouTube of the RoboCar
    - Best player of the soccer match
     The activities will end with evaluation, prize giving and refreshments

### Provided hardware
- 1 x RaspberryPi per student
- 1 x 5V power pack with USB connector to supply RaspberryPi
- 1 x 7.4V LIPO battery to supply motors (each group will need to manage charging, to ensure that they always have a “live” battery available for testing and competition)
- 1 x Self build RoboCar chassis with motors (4) and wheels (4)
- 1 x TB6612FNG H bridge MotorController
- 4 x Infra-red reflecting line-following sensors, which can be mounted on the chassis
- 2 x Ultrasonic sensors, used to measure distance for the ultrasound/boxes challenge
- DuPont cables, tie wrap, breadboards etc. as required
