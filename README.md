# Icon Generator

Generates Github-style user avatars using MD5-hashed strings in Python and Javascript (currently in development). 

An interactive web implementation can be (soon) found on [my GitHub site](https://mg2239.github.io/projects/icon_gen.html).

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
3. Run using `python3 app.py` in the py directory

## API
### Generate an icon
Request: `GET /api/generate/`

Body:
`
{
  "username": <string>,
  "palette": <string>,
  "num_colors": <string>
}
`

Response:
`
{
  "success": True,
  "data": <imgur url>
}
`

## Demo
![](https://imgur.com/VBc3qKE.png)
![](https://imgur.com/06TRhUO.png)
![](https://imgur.com/3Rn1rdo.png)
![](https://imgur.com/QZbW7Qx.png)
