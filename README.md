# Task
Part of the coursework for CSU33012 Software Engineering. We were tasked with interrogating the GitHub API and visualising the retrieved data.

# Description
This implementation retrieves data about the repositories belonging to the authenticated user (such as their size, top languages etc.), and then visualises this data using the JavaScript library D3.js. You can find more information about D3.js here:
https://d3js.org/.

The data is gathered into the appropriate JSON files by running _gather.sh_. The visualisation is served using a simple HTTP server which is initialised by running the script
_run-server.sh_.
The visualisation can then be viewed by navigating to localhost:8000 in your browser.

This visualisation project has been written in Python and makes use of the PyGithub library for data retrieval from the GitHub API. The retrieved data is written to local JSON files which are then used in the visualisations. **NOTE**: to retrieve data, you will need to generate a personal access token and pass that token into the appropriate place within _main.py_. You can find more information about generating personal access tokens at the following link: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

The quickest way to see this visualisation in action is using the data contained in the JSON files within this repository. To do this, you must:

1. Clone the repository into a local directory.
2. Navigate to that directory.
3. Either run the shell script _run-server.sh_ or manually enter its contents into your command line, the end result will be the same. The contents of this shell script are _python3 -m http.server_.
4. Navigate to localhost:8000 in your browser.
5. Voilà! Now you have the visualisations up and running. 

For demonstrative purposes, I have captured the visualisations that are returned to me when I execute this application using my own personal access token.
# Demo
Here is a brief demonstration of my visualisation:

![Visualisation demo](demo/demo.gif)

# Requirements
**1. Python:** You can check what version of Python is installed on your machine by entering _python --version_ via the command line.

**2. Pip:** This can be installed by running the _get-pip.py_ file that is located within the repository.

**3. PyGithub:** Command for installation: _pip install PyGithub_ 

**4. JSON** (which is a Python module and can simply be imported)

