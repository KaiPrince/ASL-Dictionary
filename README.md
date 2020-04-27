# ASL Dictionary
A visual dictionary for American Sign Langauge.
<br/>Check out the live [website](https://asl-dictionary.web.app/).

## Motivation
This full-stack web app is a useful reference for basic ASL words and phrases. Add new words to the app as you learn them. Much more effective than written notes.

## Screenshots
<img src="https://imgur.com/xT8mEi4.png" alt="Index page" width="400" />
<img src="https://imgur.com/2p1N0qC.png" alt="Detail page" width="400" />

<small>Sample data from [Lifeprint.com](https://www.lifeprint.com). Used for demo purposes only.</small>

## Features
This app features:
- Easy editing with built-in Content Management System
- Fast loading with Server-Side Rendering
- Beautiful styling with Material Design spec
- Autocomplete search function
- Compare resources on external sites via web scraping
- Video compression for low network usage
- Thumbnail generation for faster first paint

## Tech/framework used

<b>Built with</b>
- [Nuxt](https://www.nuxtjs.org)
- [Vue.js](https://www.vuejs.org)
- [Vuetify](https://www.vuetifyjs.com)
- [Jest](https://www.jestjs.io)
- [Django](https://www.djangoproject.com)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [FFMPEG](https://ffmpeg.org/)

## Installation
See READMEs of individual projects for installation instructions.

## How to use?
To view the dictionary, navigate to the frontend at 'localhost:3000'. <br />
To edit the dictionary, navigate to the backend at 'localhost:8000/admin'.

## API Reference
```json
[
    {
        "id": 6,
        "label": "Enthusiastic",
        "description": "To do the concept \"enthusiastic\" (or \"enthusiasm\"), rub your hands together in enthusiastic anticipation",
        "images": [
            {
                "id": 4,
                "alt_text": "ENTHUSIASTIC",
                "caption": "Enthusiastic",
                "image_file": "[path to file]"
            }
        ],
        "videos": [],
        "see_also": []
    },
]
```

## Tests
Frontend:
```
yarn run test
```

Backend:
```
python manage.py test
```
