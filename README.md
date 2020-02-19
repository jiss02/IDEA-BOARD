<p align="center">
  <h3 align="center">아이디어 공유를 위한 게시판 서비스</h3>
  <p align="center">
    멋쟁이 사자처럼 해커톤 아이디어를 지속적으로 공유하기 위한, <br/>
    아이디어 게시판 (Backend) <br />
   </p>


&nbsp;
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Requirements](#requirements)
  * [Installation](#installation)

&nbsp;
<!-- ABOUT THE PROJECT -->

## About The Project

<div align="center">
<br/>
해커톤 아이디어를 떠올리기 힘들다면? <br/>
    <b>다른 사람들의 아이디어에 조인해보자</b>
</div>


&nbsp;

해커톤이 임박하여 아이디어를 급하게 정하고 팀을 꾸리는 경우가 대다수입니다. 더욱 견고한 아이디어 기획을 위해 멋사 활동 초반부터 개발하고 싶은 서비스를 기획하고 팀을 모을 수 있도록 아이디어를 기록하고 원하는 아이디어에 조인을 신청할 수 있도록 한 서비스 입니다.


### Built With

* Python Django
* Django-Rest-Framework
* SQLite3

&nbsp;
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Setup project environment with [venv](https://docs.python.org/3/library/venv.html) and [pip](https://pip.pypa.io).

* setting venv
```bash
$ python3 -m venv venv
$ . venv/Scripts/activate
```

* Django
```bash
$ pip install django
```

&nbsp;
### Requirements
```
asgiref==3.2.3
Django==3.0.2
django-cors-headers==3.2.1
djangorestframework==3.11.0
pytz==2019.3
sqlparse==0.3.0
```
&nbsp;
### Installation

1. Clone the repo
```sh
$ git clone https://github.com/jiss02/IDEA-BOARD.git
```
2. Migrate Database
```sh
$ python manage.py migrate
```
3. Create config folder and django-key.json

```sh
$ mkdir config
$ cd config
$ vim django-key.json
```

4. Run server

```
$ python manage.py runserver
```

