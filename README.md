# Icon Generator

Web app that generates Github-style user avatars using MD5 hashes of strings.

## Requirements
Found in requirements.txt

## Installation
To run locally:
1. Download the zip file
2. Install Pillow
3. Run using `python3 main.py` in the py directory

To run the Flask app:
1. Download the zip file
2. Install the packages in requirements.txt (`pip3 install -r requirements.txt`)
3. Run using `python3 app.py` in the src directory

## API
### Generate an icon
Request: `GET /api/generate/?username=<string>&palette=<string>&num_colors=<int>`

Response:
`
{
  "success": True,
  "data": <base64 string>
}
`

## Demo
![](https://imgur.com/VBc3qKE.png)
![](https://imgur.com/06TRhUO.png)
![](https://imgur.com/3Rn1rdo.png)
![](https://imgur.com/QZbW7Qx.png)
