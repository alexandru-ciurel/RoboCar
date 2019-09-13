# RoboCar

This was the first-semester project that we (a group of 3 people) had to do as students in the IT Technology AP programme at the Business Academy Aarhus. It was a pretty big project consisting of multiple parts/challenges. Below I will leave the full description of the assignment given to us by the teachers. The project was also intended to be used in a competition vs the other students and in the end we actually managed to get the first place in both challenges (line following and getting the boxes out)

I was in charge of the programming and developing of the Python code/algorithms for our RoboCar and the code for our Web controlling interface. Considering that this was a real-world enviroment project/goal, I've devolped the code alongside thoroughly testing the RoboCar which resulted in a lot of adjustments being made to the whole system. My main focuses in this priject were the line following and ultrasound/boxes challenges. Some [videos](https://www.youtube.com/playlist?list=PLQ_rnhlgQIKJ_0Fx1rame-8r3_Qewp8hX) of the RoboCar at different stages in the project.

### Description of the setup

A metal car chassis with 4 electrical motors attached to plastic wheels - both motors on each side (left and right) being connected in series. As a logical view, this meant we only had to deal with 2 variables (left and right). These motors were connected to an H2 Bridge, which could control their states by adjusting 4 inputs (2 for each side, giving us the oportunity to have 4 states, but only 3 were needed: OFF=STOP, forward, backward). The inputs were controlled by Python 3.6 code, mainly using the GPIO library. As for the OS for the Raspberry PI, we've used the Raspbian Stretch Lite (Linux distro no GUI) on top of which  we installed "git", for easy delopyment of the code, and an apache2 webserver for the webinterface. Besides controlling the movement of the car, we've also connected 3 light sensors  and 1 ultrasound sensor to the Raspberry PI pins for getting the much needed information regarding the present state and an overview of the system/car, which in the end was used for the two competitions. Light sensors - am i on the right track, following the line? Ultrasound sensor - measuring distance in front of the car for determining if an object was there or not.

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
