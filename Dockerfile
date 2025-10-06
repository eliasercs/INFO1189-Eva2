FROM mariadb:latest

COPY ./docker/mariadb/init-scripts/ /docker-entrypoint-initdb.d/

COPY ./docker/mariadb/conf/ /etc/mysql/conf.d/

EXPOSE 3306

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD mysqladmin ping -h localhost -u root -p${MYSQL_ROOT_PASSWORD} || exit 1