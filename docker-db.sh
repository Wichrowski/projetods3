CONTAINER_NAME=projeto_ds3
DATABASE_NAME=projeto_ds3
POSTGRES_VERSION="9.5"

case $1 in
  run)
    docker run \
      --detach \
      --rm \
      --name ${CONTAINER_NAME} \
      --publish 5432:5432 \
      --env POSTGRES_PASSWORD=${DATABASE_NAME}\
      postgres:${POSTGRES_VERSION}
    ;;

  create)
    docker exec \
      --interactive \
      --tty \
      ${CONTAINER_NAME} psql -U postgres -c "CREATE DATABASE ${DATABASE_NAME}"
    ;;

  console)
    docker exec \
      --interactive \
      --tty \
      ${CONTAINER_NAME} psql -U postgres -d ${DATABASE_NAME}
    ;;

  *)
    echo "Invalid option. Try: run, create or console"
    ;;
esac
