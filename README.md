# Google Search Scraping Tool
## Overview

### `scrape.py`
- Script to scrape google search engine.
- Two types of contents are availabel
    - Text: `n`-top webpage URLs
    - Image: `n`-top image URLs

## Usage
```bash
python scrape.py --keyword 'Junya Watanabe' --ctype image --cnum 100
```
### Use as API server
Build this application with API server

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