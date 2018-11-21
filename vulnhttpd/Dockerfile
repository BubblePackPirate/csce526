FROM debian:stretch

#WORKDIR /tmp

#nice stuff to have in a container perhaps
RUN apt-get update && apt-get install curl locate nano tcpdump -y

# grab baddie
ADD https://archive.apache.org/dist/httpd/binaries/linux/httpd-2.0.48-x86_64-unknown-linux-gnu.tar.gz .
RUN mkdir /www && chmod 777 /www
RUN tar -xzf httpd-2.0.48-x86_64-unknown-linux-gnu.tar.gz && cd /httpd-2.0.48 && ./install-bindist.sh /www
RUN rm -rf httpd-2.0.48-x86_64-unknown-linux-gnu.tar.gz && rm -rf /httpd-2.0.48

RUN ln -s /usr/lib/x86_64-linux-gnu/libdb-5.3.so /usr/lib/x86_64-linux-gnu/libdb.so.2
RUN cp /www/lib/* /usr/lib/x86_64-linux-gnu/



COPY entrypoint.sh .
COPY httpd.conf /www/conf/	

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ./entrypoint.sh
EXPOSE 80
