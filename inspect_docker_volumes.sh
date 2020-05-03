for i in `docker volume ls -q`
do
    echo "volume: ${i}"
    docker run --rm -it -v ${i}:/vol alpine:latest ls /vol
    echo
done

