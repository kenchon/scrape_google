# Google Search Scraping Tool
## Overview

![howtouse](https://i.imgur.com/NTuaVL1.gif)

### `scrape.py`
- Script to scrape google search engine.
- Two parameters should be specified:
  - Target content type: `--ctype`∈{"text", "image"}
  - Number of contents : `--cnum` ∈ ℕ 

## Usage

### 1. Use as a script.
#### 1.1 Requirements:
- Python `3.x`
- `bs4`, `lxml`
  - `pip install bs4, lxml` to install the packages.

#### 1.2 How to run
```bash
python scrape.py --keyword 'Junya Watanabe' --ctype image --cnum 100
```
### 2. Run the script on docker container
#### 2.1 Requirements:
```bash
➜  scrape_google git:(master) docker -v
Docker version 19.03.2, build 6a30dfc
```

#### 2.2 How to run

1. Clone this repository and move to working directory.
2. Build the API server
```bash
docker build -t api/app .
```
3. Run docker container
```bash
docker run -p 4000:3000 --rm --name app -d -t api/app
```
4. Test the server
```bash
docker ps # to check wheather the server is working
curl http://0.0.0.0:3000/junya%E3%80%80watanabe/image/
```
