# This is a sample Python script.
from github import Github
import json

g = Github("token")

user = g.get_user()

dct = {'user': user.login,
       'fullname': user.name,
       'location': user.location,
       'public_repos': user.public_repos,
       'private_repos': user.total_private_repos
       }
# if there is no value, remove the key
for k, v in dict(dct).items():
       if v is None:
              del dct[k]

with open('data.json', 'w') as outfile:
       json.dump(dct, outfile)

# here we are gathering information about the repos and their size for displaying
# repo.size automatically gives back size in bytes
repos = user.get_repos()
repoDict = [] 
for repo in user.get_repos():
       currentRepo = { 'repoName': repo.name,
       'size': repo.size
       }
       if repo.size > 0:    # we don't want to add empty repos to the visualisation
              repoDict.append(currentRepo)

with open('repoData.json', 'w') as outfile:
       json.dump(repoDict, outfile)

tinyRepos = []
mediumRepos = []
largeRepos = []
for repo in user.get_repos():
       checkSize = { 'repoName': repo.name,
       'size': repo.size,
       }
       if repo.size > 0 and repo.size <= 200:
              tinyRepos.append(checkSize)
       elif repo.size > 200 and repo.size <= 2000:
              mediumRepos.append(checkSize)

for repo in user.get_repos():
       checkSize = { 'repoName': repo.name,
       'size': (repo.size/1024),   # divide by 1024 to convert to kb
       }
       if repo.size > 2000:
              largeRepos.append(checkSize)              

with open('tinyRepos.json', 'w') as outfile:
       json.dump(tinyRepos, outfile)

with open('mediumRepos.json', 'w') as outfile:
       json.dump(mediumRepos, outfile)

with open('largeRepos.json', 'w') as outfile:
       json.dump(largeRepos, outfile)

repoLanguages = []
for repo in user.get_repos():
       getLanguages = {
              'language': repo.language
       }
       if repo.language is not None:
              repoLanguages.append(getLanguages)

with open('repoLanguages.json', 'w') as outfile:
       json.dump(repoLanguages, outfile)

repoForks = []
for repo in user.get_repos():
       getForks = { 'repoName': repo.name,
              'forks': repo.forks
       }
       if repo.forks != 0:
              repoForks.append(getForks)
with open('repoForks.json', 'w') as outfile:
       json.dump(repoForks, outfile)
