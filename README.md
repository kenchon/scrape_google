# Google Search Scraping Tool
## Overview

### `scrape.py`
- Script to scrape google search engine.
- Two parameters should be specified:
  - Target content type: `--ctype`∈{"text", "image"}
  - Number of contents : `--cnum` ∈ ℕ 

### `Dockerfile`


## Usage

### 1. Run the script on your bare-metal machine.
#### 1.1 Requirements:
- Python `3.x`
- `bs4`, `lxml`: `pip install bs4, lxml` to install the packages.

#### 1.2 How to run
```bash
python scrape.py --keyword 'Junya Watanabe' --ctype image --cnum 100
```
### 2. Run the script on docker container

#### 2.1 Requirements:
- The latest version of `docker` should be installed

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
