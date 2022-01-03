# Task
Part of the coursework for CSU33012 Software Engineering. We were tasked with interrogating the GitHub API and visualising the retrieved data.

# Description
This implementation retrieves data about the repositories belonging to the authenticated user, and then visualises them using D3.js. The visualisation is served using a simple HTTP server which is initialised by running the script
_run-server.sh_.
The visualisation can then be viewed by navigating to localhost:8000 in your browser.

This visualisation project has been written in Python and makes use of the PyGithub library for data retrieval from the GitHub API. The retrieved data is written to local JSON files which are then used in the visualisations. **NOTE**: to run this application and retrieve data, you will need to generate a personal access token and pass that token into the appropriate place within _main.py_. You can find more information about generating personal access tokens at the following link: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

For demonstrative purposes, I have captured the visualisations that are returned to me when I execute this application using my own personal access token:

# Requirements
**1. Python:** You can check what version of Python is installed on your machine by entering _python --version_ via the command line.

**2. Pip:** This can be installed by running the _get-pip.py_ file that is located within the repository.

**3. PyGithub:** Command for installation: _pip install PyGithub_ 

**4. JSON** (which is a Python module and can simply be imported)

