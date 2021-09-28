# Image Repository (Pokémon Edition) - Shopify Challenge 2022

Ever wanted to search up Pokémon based on their similarities to other Pokémon?

This is an image repository focused on helping Pokémon enthusiasts find new Pokémon based on similarities
to their favourite Pokémon. There are currently two methods in which you can use to search for similar Pokémon. The first
method is quite simple and involves selecting a base Pokémon with two types, which are then used to query for other
Pokémon having the same two types. The second method involves the use of [DeepImageSearch](https://github.com/TechyNilesh/DeepImageSearch) - an AI-based image search engine - to search through the repository of Pokémon and returning those that share similarities in appearance.

## Getting Started
1. Clone this repository:

   ```git clone https://github.com/christopher-tse/pokemon-image-repo.git```

2. Make sure you have [Python](https://www.python.org/) installed - instructions on how to do that can be found [here](https://docs.python.org/3/using/index.html)

3. Within the project directory, setup a virtual environment and install the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web application framework - instructions on how to do that can be found [here](https://flask.palletsprojects.com/en/2.0.x/installation/)

4. Using your console/terminal, set the *FLASK_APP* (and optionally *FLASK_DEBUG*) environment variable for the project:

   ```export FLASK_APP=server.py```
   ```export FLASK_DEBUG=1```

5. Using your console/terminal, start the application:

   ```flask run```

6. To view the application, your console/terminal will output a confirmation message with the address/port it is running on

   ```ie. http://localhost:5000```

## Technologies
I built this project using primarily a set of technologies which I have not had experience with before. I decided to go this route because
I wanted to really challenge myself in learning new things and growing my skills as a developer.

The application is written in Python and I chose this because I felt that my prior experience using it was far too long ago. 

In terms of frameworks, I had the option of going with Django or Flask, and in the end I chose Flask because it felt more light-weight, easier to get running quickly, and could scale well.

For my database, I leveraged SQLite because it required little configuration time and met all my simple storage needs.

As for my dataset, I was able to find this really cool [Pokémon dataset](https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types) from [Kaggle](https://www.kaggle.com/), which provided me with a csv file containing Pokémon data and also images of Pokémon.

## TODO: Features/Improvements
In the limited time that I had to work on this project, I was only able to implement mainly search features. Below are some of the features/improvements that I would like to implement in the future!
- Tests: I unfortunately did not have enough time to generate a well defined test suite and was only able to perform sanity tests. I hope to learn about the various
  testing libraries available and apply those to my application in the future!
- Query with new images: Currently the queries are made using existing images in a static directory. It would be nice and very beneficial to have the ability to upload new images (Pokémon) to the image repository for querying, since there are always new images (Pokémon!!) coming out!

## App Demo via Readme!!
coming soon..enjoy these images for now

image repository

<img width="539" alt="Landing" src="https://user-images.githubusercontent.com/50059518/135020466-6f771717-7345-49e1-ac83-8520c9c11eda.png">

searching repository by type

<img width="351" alt="SearchByType" src="https://user-images.githubusercontent.com/50059518/135020773-8dc444b8-a586-4910-ab62-707bdfc373e2.png">

searching repository by image

<img width="351" alt="SearchByImage" src="https://user-images.githubusercontent.com/50059518/135020824-f710f145-c0a5-47c3-a651-8d4a52b21267.png">


