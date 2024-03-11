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
| printstatements - settings.py | PEP8 validator | [No issues found](static/images-readme/readme-pep8.png) | ✅ |
| printstatements - urls.py | PEP8 validator | No issues found | ✅ |
| blog app - forms.py | PEP8 validator | No issues found | ✅ |
| blog app - models.py | PEP8 validator | No issues found | ✅ |
| blog app - views.py | PEP8 validator | No issues found | ✅ |
| blog app - urls.py | PEP8 validator | No issues found | ✅ |
| blog app - admin.py | PEP8 validator | No issues found | ✅ |
| artprint app - forms.py | PEP8 validator | No issues found | ✅ |
| artprint app - models.py | PEP8 validator | No issues found | ✅ |
| artprint app - views.py | PEP8 validator | No issues found | ✅ |
| artprint app - urls.py | PEP8 validator | No issues found | ✅ |
| artprint app - admin.py | PEP8 validator | No issues found | ✅ |
| style.css | [W3C - Jigsaw](https://jigsaw.w3.org/css-validator/) validator | [No issues found](static/images-readme/readme-w3c-css.png) | ✅ |
| Home page - html | [W3C](https://validator.w3.org/) validator - source code | No issues found | ✅ |
| About page - html | W3C validator - source code | No issues found | ✅ |
| Blog page - html | W3C validator - source code | No issues found | ✅ |
| Prints page - html | W3C validator - source code | No issues found | ✅ |
| Sign-in page - html | W3C validator - source code | No issues found | ✅ |
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
