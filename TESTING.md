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
| home_taste - settings.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | No issues found | [E501 line too long: AUTH_PASSWORD_VALIDATORS - STATICFILES_STORAGE](static/images/readme/home-taste-settings.png) |
| home app - views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/home-views-file.png) | ✅ |
| home app - urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/home-urls-file.png) | ✅ |
| chefs app - views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-views-file.png) | ✅ |
| chefs app - urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-urls-file.png) | ✅ |
| chefs app - models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-models-file.png) | ✅ |
| chefs app - forms.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-forms-file.png) | ✅ |
| chefs app - admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](static/images/readme/chefs-admin-file.png) | ✅ |
| main.js | [JSHint](https://jshint.com/) | [No issues found](static/images/readme/jshint-main-js-file.png) | ✅ |
| base.css | [W3C - Jigsaw CSS](https://jigsaw.w3.org/css-validator/) | [No issues found](static/images/readme/css-w3c.png) | ✅ |
| Home page - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-home.png) | ✅ |
| Chefs page - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-chefs.png) | ✅ |
| Chef Information page - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-chef-information.png) | ✅ |
| Login page - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-login.png) | ✅ |
| Register page - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-register.png) | ✅ |
| password/reset page - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-password-reset-page.png) | ✅ |
| password/reset/done Email sent page - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-password-reset-done-email-sent.png) | ✅ |
| password/reset/key page opened from the received email - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-password-reset-key.png) | ✅ |
| password/reset/key/done page password changed - html | [W3C - URI](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-password-key-done.png) | ✅ |
| My Profile page - html | [W3C - Direct Input](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-my_profile-page.png) | ✅ |
| Edit/Update Profile page - html | [W3C - Direct Input](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-edit-profile-page.png) | ✅ |
| Logout page - html | [W3C - Direct Input](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-logout-page.png) | ✅ |
| Delete profile page - html | [W3C - Direct Input](https://validator.w3.org/) | [No issues found](static/images/readme/w3c-delete-profile-page.png) | ✅ |
| Home page - html | lighthouse | [Acceptable scores](static/images/readme/light-house-overall.png) | ✅ |
| MS-Edge browser | Launch site | Site opens without issue | ✅ |
| Chrome browser | Launch site | Site opens without issue | ✅ |
| Safari browser | Launch site | Site opens without issue | ✅ |

## Responsiveness Testing

| **TEST**                      | **ACTION**              | **EXPECTATION**             | **RESULT** |
| ----------------------------- | ----------------------- | --------------------------- | ---------- |
| Home page - responsiveness    | Size site down to 370px | all elements stay on screen | ✅         |
| Home page - responsiveness    | Size site up to 1920px  | all elements stay on screen | ✅         |
| Chefs page - responsiveness   | Size site down to 370px | all elements stay on screen | ✅         |
| Chefs page - responsiveness   | Size site up to 1920px  | all elements stay on screen | ✅         |
| Chef-Info Profile page - responsiveness  | Size site down to 370px | all elements stay on screen | ✅         |
| Chef-Info Profile page - responsiveness  | Size site up to 1920px  | all elements stay on screen | ✅         |
| Login page - responsiveness    | Size site down to 370px | all elements stay on screen | ✅         |
| Login page - responsiveness    | Size site up to 1920px  | all elements stay on screen | ✅         |
| Register page - responsiveness | Size site down to 370px | all elements stay on screen | ✅         |
| Register page - responsiveness | Size site up to 1920px  | all elements stay on screen | ✅         |
| My Profile page - responsiveness | Size site down to 370px | all elements stay on screen | ✅         |
| My Profile page - responsiveness | Size site up to 1920px  | all elements stay on screen | ✅         |
| Update Profile page - responsiveness | Size site down to 370px | all elements stay on screen | ✅         |
| Update Profile page - responsiveness | Size site up to 1920px  | all elements stay on screen | ✅         |
| Logout page - responsiveness | Size site down to 370px | all elements stay on screen | ✅         |
| Logout page - responsiveness | Size site up to 1920px  | all elements stay on screen | ✅         |
| Delete Profile page - responsiveness | Size site down to 370px | all elements stay on screen | ✅         |
| Delete Profile page - responsiveness | Size site up to 1920px  | all elements stay on screen | ✅         |
| Forgot Password process (4-pages) - responsiveness | Size site down to 370px | all elements stay on screen | ✅         |
| Forgot Password process (4-pages) - responsiveness | Size site up to 1920px  | all elements stay on screen | ✅         |

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
