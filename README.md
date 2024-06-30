# YouTube Video Downloader

This project is a web-based YouTube Video Downloader built using Django, a high-level Python web framework.  
The application allows users to download YouTube videos by simply providing the URL of the video through a friendly user interface.

## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **pytube**: A lightweight, Pythonic library for downloading YouTube videos.
- **HTML/CSS**: For building the front-end user interface minimalist but transparent.

## Nice to have:
- ✓ Anaconda installed
- ✓ Basic knowledge of Python and Django

---

## 1. Basic Setup

1. Create environment:
```bash
conda create --name DownloadEnv 
```

2. Active the environment: 
```bash
conda activate DownloadEnv
```

3. Install Framework
```bash
conda install django
````

4. Install Library
```bash
pip install pytube
```
----------------------------------------------------
## 2. Project Setup

1. Create a django project: 

````bash
django-admin startproject youtube_downloader
cd youtube_downloader
````


2. Create a new app:
````bash
python manage.py startapp downloader
````

----------------------------------------------------
## 3. How to run project?

1. Migration command:
````bash
python manage.py migrate
````

 3. Run server:
 Important! Make sure u are in the path where is manage.py file!

````bash
python manage.py runserver
````

## File Tree:
![three](https://github.com/NeverPlayFair/YoutubeDownloader/assets/65012705/9316c504-3039-4adc-a36f-5d5961e3b699)

## Linux view:
![Linux](https://github.com/NeverPlayFair/YoutubeDownloader/assets/65012705/7fc060e6-df54-4608-a75a-f9855f47c62f)



## Demo of app:

![image](https://github.com/NeverPlayFair/YoutubeDownloader/assets/65012705/2b82dc14-f080-42b0-bb9c-9e44dfc5cdcc)

![image](https://github.com/NeverPlayFair/YoutubeDownloader/assets/65012705/bb801ee5-c3a6-4525-8e4d-83ab0acc5619)

![image](https://github.com/NeverPlayFair/YoutubeDownloader/assets/65012705/f3957f44-c4b8-425d-b41e-95e578803f97)

![image](https://github.com/NeverPlayFair/YoutubeDownloader/assets/65012705/ffa2f3a7-8c08-4169-bc66-a7b6c1d3e08a)





