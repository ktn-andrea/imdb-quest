# :hot_pepper: The Big IMDB quest :movie_camera:
An application that scrapes data from IMDB and adjusts IMDB ratings.


:electric_plug: Getting Started 
------------
- Python version used for this project: Python 3.11
- Make sure $PYTHONPATH is set correctly on your machine.


:computer: Using the project
------------
Clone the repository:\
`git clone https://github.com/ktn-andrea/imdb-quest.git`

Step into project folder:\
`cd ./imdb-quest`

Install the required packages with pip:\
`pip install -r requirements.txt`

Run main.py script:\
`python ./scripts/main.py`\
\
Output result is written to __results.json__ in JSON format.


:briefcase: Project Organization 
------------

    ├── README.md
    ├── requirements.txt
    ├── scripts
    │   ├── main.py
    │   ├── movie.py
    │   ├── scraper.py
    │   └── rating_calculator.py
    ├── tests_package        
    │   ├── test_scraper.py
    |   └── test_rating_calculator.py
