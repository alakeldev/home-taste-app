# TESTING

* [Validator Testing](#validator-testing)
* [Responsiveness Testing](#responsiveness-testing)
* [C.R.U.D Testing](#crud-testing)
* [Features](#features)
* [Fixed Bugs](#fixed-bugs)
* [Unfixed bugs](#unfixed-bugs)

## Validator Testing

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| ----------------------------- | ----------------------- | --------------------------- | ---------- |
| manage.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/manage-py-file.png) | ✅ |
| home_taste - urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/home_taste-urls.png) | ✅ |
| home_taste - settings.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [Issues found](static/images/readme/home-taste-settings.png) | ( E501 line too long : AUTH_PASSWORD_VALIDATORS - STATICFILES_STORAGE) |
| home app - views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/home-views-file.png) | ✅ |
| home app - urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/home-urls-file.png) | ✅ |
| chefs app - views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-views-file.png) | ✅ |
| chefs app - urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-urls-file.png) | ✅ |
| chefs app - models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-models-file.png) | ✅ |
| chefs app - forms.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-forms-file.png) | ✅ |
| chefs app - admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-admin-file.png) | ✅ |
| style.css | [W3C - Jigsaw](https://jigsaw.w3.org/css-validator/) validator | [No issues found](static/images-readme/readme-w3c-css.png) | ✅ |
| Home page - html | [W3C](https://validator.w3.org/) validator - URI | No issues found | ✅ |
| Chefs page - html | [W3C](https://validator.w3.org/) validator - URI | No issues found | ✅ |
| Chef_info page - html | [W3C](https://validator.w3.org/) validator - URI | No issues found | ✅ |
| Sign-in page - html | [W3C](https://validator.w3.org/) validator - URI | No issues found | ✅ |
| My Profile page - html | [W3C](https://validator.w3.org/) validator - Source code | No issues found | ✅ |
| Edit Profile page - html | [W3C](https://validator.w3.org/) validator - Source code | No issues found | ✅ |
| Delete Profile page - html | [W3C](https://validator.w3.org/) validator - Source code | No issues found | ✅ |
| Home page - html | lighthouse | [Acceptable scores](static/images-readme/readme-lighthouse.png) | ✅ |
| About page - html | lighthouse | Acceptable scores | ✅ |
| Blog page - html | lighthouse | Acceptable scores | ✅ |
| Prints page - html | lighthouse | Acceptable scores | ✅ |
| Sign-in page - html | lighthouse | Acceptable scores | ✅ |
| Brave browser | Launch site | Site opens without issue | ✅ |
| Chrome browser | Launch site | Site opens without issue | ✅ |
| Safari browser | Launch site | Site opens without issue | ✅ |

## Responsiveness Testing

| **TEST**                      | **ACTION**              | **EXPECTATION**             | **RESULT** |
| ----------------------------- | ----------------------- | --------------------------- | ---------- |
| Home page - responsiveness    | Size site down to 320px | all elements stay on screen | ✅         |
| Home page - responsiveness    | Size site up to 1920ox  | all elements stay on screen | ✅         |
| About page - responsiveness   | Size site down to 320px | all elements stay on screen | ✅         |
| About page - responsiveness   | Size site up to 1920ox  | all elements stay on screen | ✅         |
| Prints page - responsiveness  | Size site down to 320px | all elements stay on screen | ✅         |
| Prints page - responsiveness  | Size site up to 1920ox  | all elements stay on screen | ✅         |
| Blog page - responsiveness    | Size site down to 320px | all elements stay on screen | ✅         |
| Blog page - responsiveness    | Size site up to 1920ox  | all elements stay on screen | ✅         |
| Sign-in page - responsiveness | Size site down to 320px | all elements stay on screen | ✅         |
| Sign-in page - responsiveness | Size site up to 1920ox  | all elements stay on screen | ✅         |

## C.R.U.D Testing

| **TEST**          | **ACTION**             | **EXPECTATION**          | **RESULT** |
| ----------------- | ---------------------- | ------------------------ | ---------- |
| Blog - Create     | Add new instance to DB | Instance created         | ✅         |
| Blog - Read       | Retrieve all instances | Instances visible in UI  | ✅         |
| Blog - Update     | Modify an instance     | Mods saved & visible     | ✅         |
| Blog - Delete     | Delete an instance     | Instance removed from UI | ✅         |
| Comments - Create | Add new instance to DB | Instance created         | ✅         |
| Comments - Read   | Retrieve all instances | Instances visible in UI  | ✅         |
| Artprint - Create | Add new instance to DB | Instance created         | ✅         |
| Artprint - Read   | Retrieve all instances | Instances visible in UI  | ✅         |
| Artprint - Update | Modify an instance     | Mods saved & visible     | ✅         |
| Artprint - Delete | Delete an instance     | Instance removed from UI | ✅         |
| Like - Create | Add new instance to DB | Instance created         | ✅         |
| Like - Delete | Delete an instance     | Instance removed from UI | ✅         |

## Features

| **TEST**                      | **ACTION**             | **EXPECTATION**                                           | **RESULT** |
| ----------------------------- | ---------------------- | --------------------------------------------------------- | ---------- |
| Navigation bar                | Click on nav link      | user routed to correct page                               | ✅         |
| Footer links                  | Click on footer links  | user routed to new browser tab                            | ✅         |
| Like button                   | Click "like"           | Post liked/unliked accordingly                            | ✅         |
| Edit button                   | Click edit button      | user navigated to edit screen                             | ✅         |
| Delete button                 | Click delete button    | print/blog removed from UI                                | ✅         |
| Internal links                | Click link             | User routed to appropriate page                           | ✅         |
| Login                         | User logs in           | UI updates & user is logged in                            | ✅         |
| Sign up                       | User signs up          | new account created for the user                          | ✅         |
| Logout                        | User clicks logout     | UI updates, user is logged out, user cannot create a post | ✅         |

## Fixed Bugs

## Unfixed Bugs
