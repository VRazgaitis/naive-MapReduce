# Naive MapReduce Project
This project counts and ranks word occurences in a text file, using a naive MapReduce approach to motivate and understand Google's MapReduce solution.

Webscraped data consiting of Stack Overflow Question titles has been chunked into 9 different text files, stored in `titles/`. The host machine launches Docker containers to tally wordcounts in each text file (Mapping task), writing results as JSON files in a filesystem shared with the host machine.

After all word count tasks have finished, the host combines wordcount files and orders results (Shuffle, Reducing tasks),
writing results to `counts/total_counts.json`

<div align="center">
  <img src="imgs/MapReduce_arch.png" width="75%" alt="Naive MapReduce System Arch">
</div>

# Setup and run
* Open Docker
* Build the mapping container with `./build_mapper.sh`
* Run word counter with `./count_words.sh`

# MapReduce History
Google developed MapReduce to efficiently crawl, categorize, and index the internet, for use as inputs into the PageRank algorithm. PageRank evaluates the importance of web pages based off of the quality and quantity of inbound links.  AFter scraping raw HTML data with web crawlers, Google used the Map Phase to parse HTML files into key-value pairs. The Reduce Phase sums up contributions for a given URL to determine its rank

# Shortcomings of Naive approach
### I/O Overhead
* Reading entire files into memory in Docker containers creates I/O overhead, particularly for large files
### Dictionary Overhead
* Using a single dictionary (+=) to accumulate word counts requires loading all intermediate data into memory at once
* Python’s dictionary implementation is not optimized for large-scale parallel reductions. Handling collisions and resizing adds overhead compared to specialized data structures
### Data Shuffling and Sorting
### Containerization Overhead
* Docker container startup times add latency for each file
* Container orchestration tools (e.g., Docker Swarm or Kubernetes) are not inherently optimized for fine-grained MapReduce-style workloads

<details>
<summary>Click to expand references</summary>
  
# References
* Docker Volume mounting - https://docs.docker.com/engine/storage/#volume-mounts
</details>