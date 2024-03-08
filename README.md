<h1 align="center">👩‍🍳 HOME TASTE 👨‍🍳</h1>
Home Taste is a global culinary hub where home chefs from diverse backgrounds converge to showcase their passion for food. The website facilitates home chef registration and login via the frontend user interface (UI). Upon successful registration and login, home chefs gain access to profile features and can share their culinary schedules, social network profiles, current locations, contact details, specialties, and captivating dish photos. Visitors (general users) can easy to navigate the website and explore chefs based on location (region, country, city), making it simple to find and connect with local talent. Additionally, visitors can share their experiences and feedbacks by leaving comments on chefs’ profiles. Whether you’re seeking to find home chef to order home-cooked meals, planning for events or simply appreciating home culinary artistry, Home Taste invites you to join this flavorful journey.

![Site view across devices](static/images/readme/amiresponsive.png)

###### The website files on Github can be accessed at the following link: [View Project Files on Github](https://github.com/alakeldev/home-taste-pp4)

###### The live website on Heroku platform can be accessed at the following link: [View my Live Website](https://home-taste-2aece88c850a.herokuapp.com/)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [App Purpose](#app-purpose)
  - [App Goals](#app-goals)
  - [Audience](#audience)
  - [Communication](#communication)
  - [Current User Goals](#current-user-goals)
  - [New User Goals](#new-user-goals)
  - [Future Goals](#future-goals)
- [Logic](#logic)
  - [Diagrams-App](#diagrams-app)
- [Design](#design)
  - [Colour](#colour)
  - [Existing Features](#existing-features)
  - [Hidden Features](#hidden-features)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
- [Technologies Used](#technologies-used)
  - [Main Languages Used](#main-languages-used)
  - [Python Packages-Modules](#python-packages-modules)
  - [Tools](#tools)
- [Deployment](#deployment)
  - [How to deploy](#how-to-deploy)
  - [How to clone](#how-to-clone)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## UX

### Site Purpose

It is website that bridges the gap between passionate home chefs and food enthusiasts. Our mission is to empower home cooks by providing them with a dedicated space to showcase their culinary talents. Chefs can register, create personalized profiles, and share essential information such as contact details, cooking schedules, and captivating images of their signature dishes. Visitors, in turn, have the privilege of exploring comprehensive chef profiles, accessing public information, and leaving valuable feedback through comments.

### Site Goals

- Empowerment: to empower home cooks by providing them with a website to express their creativity, share their love for cooking, and connect with a community of like-minded individuals.
- Visibility: to increase the visibility of home chefs and their unique offerings, allowing them to reach a broader audience.
- Interaction: to foster connection between chefs and visitors, encouraging feedback, culinary discussions, and appreciation.

### Audience

Home Taste caters to two main audiences:

- Home Chefs: Passionate home cooks who want to showcase their skills, build a personal chef profile, and connect with fellow food enthusiasts.
- Food Enthusiasts and Visitors: Individuals who appreciate home-cooked meals, seek culinary inspiration, and enjoy engaging with chefs through comments, social media networks, emails.

### Communication

Our website design ensures clarity, simplicity, and ease of navigation for both home chefs and food enthusiasts.
Here is how we achieve it:

- Clean Layout: Our uncluttered design allows users to focus on what matters most—the culinary talents of our home chefs.
- User-Friendly Experience: Whether you’re an home chef or a visitor food enthusiast, our intuitive layout guides you effortlessly through the platform.
- Clear Pathways: From chef profiles to dish images, we’ve organized everything logically, making exploration a delightful journey.

At Home Taste: communication isn’t just about words—it’s about creating a visual language that speaks to your taste buds.

### Current User Goals

- Showcase Information and Talent: Home chefs aim to display their information, profiles on social networks and culinary expertise, share their passion for cooking, and gain recognition.
- Expand Reach: Home chefs aspire to reach a wider audience beyond their immediate circles.
- Discover New Flavors: Visitors(General Users) explore chef profiles to discover unique cooking styles, regional specialties, and innovative dishes.
- Engage and Appreciate: Visitors(General Users) want to leave comments, express appreciation, and engage in meaningful feedback with chefs.
- Find Local Talent: Visitors(General Users) seek talented home chefs in their vicinity for personalized culinary experiences.

### New User Goals

- New users arrive at Home Taste with curiosity. They want to explore the diverse world of home chefs, discover unique cooking styles, and find hidden home culinary gems behind the chefs.
- Fresh visitors seek interaction. They want to engage with home chefs, leave comments, and express appreciation for mouthwatering dishes.
- Newcomers desire an intuitive experience. They aim to explore chef profiles, understand the platform’s features, and find their way around without any hassle. Whether they’re searching for a specific cuisine or browsing randomly, seamless navigation is key.

### Future Goals

- We envision Home Taste transcending geographical boundaries. Imagine a global culinary community where home chefs from diverse cultures share their flavors, techniques, and stories. From a cozy kitchen in Tokyo to a bustling food market in Marrakech, our platform will connect passionate cooks worldwide.
- We will host virtual cooking workshops. Imagine home chefs leading live sessions, demonstrating their signature dishes, and sharing tips. Participants—both seasoned cooks and beginners—will cook together, ask questions, and learn in real time. It’s a culinary classroom where creativity knows no bounds.
- We will list home chefs delectable dishes, and visitors can place orders directly through our platform. Imagine browsing a chef’s profile, selecting your favorite meal, and having it delivered to your doorstep—all with a few clicks. Secure online payments will make the process hassle-free.
- We will evolve beyond static profiles. Imagine a chat feature akin to WhatsApp, where users can connect with chefs, ask questions about recipes, discuss dietary preferences, and even receive cooking tips. Whether you’re curious about a secret ingredient or want to know the best way to julienne carrots, our chat will be your culinary companion.
- We will provide all users with a seamless and delightful experience. We achieve this by implementing robust alert and success messaging throughout the website(Register, login, logout, comments, chat, online orders, any update on their profile)

## User Stories

Not all stories have been implemented. Some have been left for future implementations as the site grows and expands.

### Admin Stories

- I possess administrative privileges to manage/CRUD operations on user(chef) exist or new  accounts, profiles, and public comments via the admin panel.
- I possess administrative privileges to a list of all registered chefs (Profile/user).
- I possess administrative privileges to a list of all comments (approved/not approved).
- I possess administrative privileges to approve or reject the public comments before they become visible on chefs' profiles.

### Registered User (Chef) Stories

- I have the capability to easy login to my registered account.
- I have the capability to logout of my registered account.
- I have the capability to add, edit, and delete my personal profile data(locations, social media networks links,....).
- I have the capability to add, edit, and delete my cook schedule on my Profile.
- I have the capability to upload/delete my profile picture.
- I have the capability to upload/delete dishes images.
- I have the capability to preview my profile as a public users, allowing me to preview the comments related to my profile and understand how it appears to general users.
- I have the capability to delete my profile along with all the data stored on the website (cannot be undone).
- I have the capability to initiate the password recovery process in the event that I misplace my current account password.
- I have the capability to update the displayed name and email address on my profile page independently of my registration credentials.
- I have the capability to view other chefs' profiles while logged in.
- I have the capability to leave comments on other chefs' profiles or even on my profile too while logged in.

### General User (Visitor) Stories

- I have the capability to register for an account as a chef then i can login after registration.
- I have the capability to easy navigate and understand the structure of the website.
- I have the capability to review profiles of all registered chefs on the website, including their relevant information and associated data.
- I have the capability to preview a specific chef's profile and easy navigate back to all chefs page again.
- I have the capability to leave comments on chefs' profiles.
- I have the capability to search for chefs based on their geographical locations like region, country, and city.

## Agile Methodology

Agile methodology is a flexible and iterative approach to software development that emphasizes collaboration, adaptability, and customer feedback. It allows teams to respond to changing requirements and deliver valuable features incrementally. In this project, we follow Agile principles to enhance productivity and ensure successful project delivery.

- User Stories and Github Issues: I utilized Github issues to create detailed user stories for my project. Each user story included essential components such as story points, acceptance criteria, and associated tasks.These user stories were tracked either on the Kanban board or within the issues themselves.
- Kanban Board for Prioritization: The Github Kanban board played a crucial role in managing my project. User stories were assigned to specific issues, allowing me to define clear goals and priorities. Labels were used to further categorize and prioritize user stories within the Kanban board.

Project Sections: my project was organized into the following sections:

- To-do: User stories awaiting implementation.
- In-progress: Ongoing work.
- Done: Completed tasks.
- Won’t-do: Items were defined as future features.

Sprint Planning with totla (5) Milestones:

- I structured the work into sprints using milestones.
- Each sprint had well-defined objectives.

To review the Kanban board for the project, please click [HERE](https://github.com/users/alakeldev/projects/3)

## Design

### Colour



### Existing Features

- Landing Page + Passwords Generator App Start:


- Get Full-Name + Welcome Message:

![Welcome Message](assets/readme-images/welcome-msg-app.png)

- Passwords Generator Run Full-Path:

![Passwords Generator Normal Path](assets/readme-images/pwd-generator-app.png)

- Passwords Generator Run "Exit" Path:

![Passwords Generator Exit Path](assets/readme-images/pwd-generator-app-exit.png)

- Passwords Manager App Start + Welcome Message:

![Passwords Manager start + Msg](assets/readme-images/pwd-manager-start.png)

- Passwords Manager App - "Save" Path:

![Passwords Manager - Save Path](assets/readme-images/pwd-manager-save-path.png)

- Passwords Manager App - "View" Path => There are saved previous Passwords:

![Passwords Manager - View Path](assets/readme-images/pwd-manager-view-path.png)

- Passwords Manager App - "View" Path => No previous Saved Passwords:

![Passwords Manager - View Path](assets/readme-images/pwd-manager-view-no-previous-pwds.png)

- Passwords Manager App - "Exit" Path => Yes Ask: There are saved previous Passwords:

![Passwords Manager - Exit & Delete](assets/readme-images/pwd-manager-exit-delete-saved-data-path.png)

- Passwords Manager App - "Exit" Path => No Ask: No Previous Saved Passwords:

![Passwords Manager - Exit](assets/readme-images/pwd-manager-exit-no-saved-data.png)

- Passwords Generator + Manager Apps => The Shortest "Exit" Path:

![Passwords Generator and Manager Apps 'Exit'](assets/readme-images/exit-all-path.png)

### Hidden Features

- Passwords Manager App Start:<br>
When the user answer ‘yes’ to the question: ‘Do you want to start the Passwords Manager Application for the first time?’, a new file named ‘the-security-key.key’ will be created, and a symmetric key will be generated and stored inside that file.

- Passwords Manager App - "Save" Path:<br>
When the user chooses the 'save' path and enters a username and password fields (without leaving any fields empty or with only one character), these entries will be saved inside ‘my-passwords.txt’. Then, a function will run to retrieve the data from ‘my-passwords.txt’ and will encrypt the retrieved data with the symmetric key that was stored inside ‘the-security-key.key’. The encrypted data will then be stored inside a new file named ‘my-encrypted-data.txt’.

- Passwords Manager App - "View" Path:<br>
When the user chooses the 'view' path and there are previously saved passwords inside ‘my-passwords.txt’, a function will run to retrieve the data from this file and will encrypt the retrieved data with the symmetric key that is stored inside ‘the-security-key.key’. The encrypted data will then be stored inside a new file named ‘my-encrypted-data.txt’. Then, another function will run to decrypt the data from ‘my-encrypted-data.txt’ file with the same key and print it out on the terminal.

- Passwords Manager App - "Exit" Path:<br>
When the user chooses to exit the Passwords Manager Application and there is previously saved data, a function will run and ask if they want to remove the previously saved data. If the user enters ‘yes’, a new function will run that will delete all of the data inside the files ‘my-passwords.txt’ and ‘my-encrypted-data.txt’.

### Future Features

- Create an account for each user that shows only their passwords and requires a master password and username to access.
- Remove and edit a specific saved username or password inside the file without affecting any other saved data.
- Password expiration reminders, two-factor authentication.
- Create a simple and beautiful GUI for the application.

## Testing

- Extensive testing was completed to review each possible path/scenario a user might take. This was to ensure looping back to the specific and related point, error messages that can be understood by the user were shown to them and finally no dead ends were encountered.
- Check the project flowchart to get each path detail by clicking [HERE](https://alakeldev.github.io/pp3-diagram/).

### Validator Testing

- The code has been tested by using [PEP8-CI Heroku-App](https://pep8ci.herokuapp.com/):<br>
As shown in the photo below, there is an error on line 127 that says “invalid escape sequence ‘\d’”. After conducting extensive searches and consulting with CI tutor support, I was unable to avoid this error as it is related to a “Regular Expression”.

![PEP8-CI Validation](assets/readme-images/pep8-ci.png)

### Fixed Bugs

- 

![Bug-codecs](assets/readme-images/bug-utf-8.png)

- 

![Bug-Fernet1-cryptography](assets/readme-images/bug-fernet1.png)

![Bug-Fernet2-cryptography](assets/readme-images/bug-fernet2.png)

- 

### Unfixed Bugs

- None currently found.

## Technologies Used

### Main Languages Used

- [Python](https://www.python.org/)

### Python Packages-Modules


### Tools

- [Heroku](https://id.heroku.com) was used to deploy the live project.
- [PEP8-CI](https://pep8ci.herokuapp.com/) online was used to validate Python code.
- [Diagrams.net](https://app.diagrams.net/) was used to create the Flowchart.
- [GitHub](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
- [VS-code](https://code.visualstudio.com/) - IDE to write Python code, create new files and folders for the project.

## Deployment

- The application was deployed successfully on the Heroku Cloud Platform.
- I used VS Code IDE to write the Python code, and it was easy to use its terminal to commit my files and push them to my repository on GitHub.
- It’s very important to install all necessary Python modules/packages and import them into your project. Open the VS Code terminal and write: “pip freeze > requirements.txt” then commit and push this change to your GitHub repo before starting the deployment process on Heroku.

### How to deploy

- The deployment on Heroku was done through the following steps:
  - log in to Heroku.
  - Create a new app in Heroku.
  - Select "New" and "Create new app".
  - Name the new app & Choose a region then click "Create app".
  - Click on the "Settings" tab at the top of the page.
  - Open the "Reveal Config Vars" section and input the following information:
    - KEY: PORT, VALUE: 8000.
  - Go to buildpacks section and press on add buildpack.
  - Select Python and Nodejs, Make sure they are in this order.
  - Click on the "Deploy" tab at the top of the page.
  - In "Deployment Method" click on "GitHub" to connect them.
  - Select "connect" to the target Repo on Github.
  - Enable Automatic Deploys" or "Deploy Branch".
  - Heroku will start the process to deploy your App.

### How to clone

- Go to the following repository on GitHub: <https://github.com/alakeldev/passwords-generator-and-manager-pp3>
- At the top right of the screen, click the 'Code' button, and then click 'HTTPs'.
- Copy the link in this field.
- Open VS-code, creat new project folder, open the terminal.
- On the terminal type "git clone", then paste the copied url and press 'Enter'.
- The clone process should now begin.

## Credits



## Acknowledgements

- I would like to express my gratitude to my mentor 'Martina Terlevic' for her invaluable feedback, advice, tips, and reviewing my project.
