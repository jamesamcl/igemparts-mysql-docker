
FROM ubuntu:14.04
MAINTAINER James Alastair McLaughlin <j.a.mclaughlin@ncl.ac.uk>

RUN apt-get update
RUN apt-get install -y \
    debconf-utils \
    git \
    nodejs \
    npm \
    && update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10

ADD xml_parts.xml.gz /tmp/igemparts/
ADD fixsql.js /tmp/igemparts/
ADD xmldumpimport.py /tmp/igemparts/
ADD create_sql.sh /tmp/igemparts/

RUN cd /tmp/igemparts \
        && gzip -d xml_parts.xml.gz \
        ; chmod +x create_sql.sh \
        && ./create_sql.sh

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server && service mysql stop

ADD my.cnf /etc/mysql/

RUN service mysql start && \
    echo 'CREATE DATABASE igem;' | mysql -u root && \
    mysql -u root igem < /tmp/igemparts/parts.sql && \
    service mysql stop

EXPOSE 3306

CMD service mysql start && tail -F /var/log/mysql/error.log



