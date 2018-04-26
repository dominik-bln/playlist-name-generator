FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.4

COPY --chown=elasticsearch:elasticsearch ./config/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/config/elasticsearch.yml

EXPOSE 9200
