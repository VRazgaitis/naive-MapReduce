#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

# count number of files to MapReduce
filecount=$(ls titles | wc -l)  

# start timer for performance testing 
start_time=$(gdate +%s.%N)  

# run a mapper docker container to count words in each txt file
for file_number in $(seq 1 "$filecount"); do  
    echo "starting map container for $file_number.txt"
    docker run -v "$(pwd)/counts:/app/counts" word_count_mapper $file_number &
done

# wait for each container to finish
wait
echo "All 9 containers finished mapping tasks." 

# Run reducer by overiding the mapping container entrypoint, instead running reduce.py
docker run -v "$(pwd)/counts:/app/counts" --entrypoint python word_count_mapper reduce.py

# End timer, compute elapsed time
end_time=$(gdate +%s.%N)
elapsed=$(echo "$end_time - $start_time" | bc)

echo "Naive MapReduce completed in $elapsed seconds."
