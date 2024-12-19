#!/bin/bash
for FILE_NO in {1..9}; do
    # run 9 docker containers. runs job asynchronously using &
    docker run -v "$(pwd)/counts:/app/counts" p2_vrazgaitis $FILE_NO &
done
wait
echo "All 9 containers finished computation" 
# overide the docker container entrypoint to combine wordcounts with reduce.py
docker run -v "$(pwd)/counts:/app/counts" --entrypoint python p2_vrazgaitis reduce.py
