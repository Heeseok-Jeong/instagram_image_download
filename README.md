# instagram_image_downloader

Download images you want with tags in Instagram

This program takes an tag, crawling times, download times from user.

It will search for the first one of the tag, crawl by the crawling times, and download images by the downlod times.

Notes 
crawling time : receiving image count
1~2 -> 33 
3+ -> 33 + 12(n-2)

<hr>

## Settings

### 1. Clone this repository

`git clone https://github.com/Heeseok-Jeong/instagram_image_downloader`

### 3. Make an user Instagram information file

To be secure of user privacy for Instagram, you need to make an file contains ID (at line 1) and password (at line 2)

> instagram_user_info.txt

```
myid@email.com
mypassword
```

### 3. Get and set `chromedriver` program

#### Download

This program needs chromedriver for crawling and controling in Instagram.  

Get the program in https://chromedriver.chromium.org/downloads .

Make sure to match this program's version with your chrome browser.

#### Adaption

In `instagram_image_downloader.py`, line 15, when you loads a driver, put chromedriver path to executable_path.


<hr>

## Run

If you done for settings, now you can run the program.

`python3 instagram_image_downloader.py`

### Inputs

tag : string

crawling count : int (at least 1)

download count : int (at least 1)



