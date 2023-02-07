# :hot_pepper: The Big IMDB quest :movie_camera:
An application that scrapes data from IMDB and adjusts IMDB ratings.


:computer: Getting Started 
------------
Clone the repository:\
`git clone https://github.com/ktn-andrea/imdb-quest.git`

Step into project folder:\
`cd ./imdb-quest`

Install the required packages with pip:\
`pip install -r requirements.txt`

Run main.py script:\
`python ./scripts/main.py`

:electric_plug: Using the project
------------
- Output is written to __results.json__ in JSON format.
- Python version used for this project: Python 3.11
- Make sure $PYTHONPATH is set correctly on your machine.


:briefcase: Project Organization 
------------

    ├── README.md
    ├── requirements.txt
    ├── scripts
    │   ├── main.py
    │   ├── movie.py
    │   ├── scraper.py
    │   └── rating_calculator.py
    ├── test_packages             
    │   ├── test_scraper.py
    |   └── test_rating_calculator.py
