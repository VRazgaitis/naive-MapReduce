## Problem 2
### Instructions
* Create a docker image by running ```./build.sh```
* Count word occurences by running ```./count.sh```
* the final wordcounts json is saved in the host directory as ```counts/total_counts.json```
 
### Solution notes
* Rather than having reduce.py wait for the 9 containers running map.py to finish
(via polling or some other method), I decided to have the bash script ```./count.sh``` 
handle container orchestration. 
* ```./count.sh``` starts the 9 docker containers and allows them to run concurrently. Once 
all of these jobs are finished, the 10th container runs reduce.py to combine results

### Known issues or bugs
* None that I'm aware of. 