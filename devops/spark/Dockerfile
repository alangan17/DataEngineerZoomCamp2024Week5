FROM docker.io/bitnami/spark:3.3

ENV PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"
ARG PIPENVFILE

USER root
RUN apt-get update 
RUN apt-get install wget -qqq

# the rootless user ID
USER 1001    

## Install custom Python libraries (with uv)
## copy scripts folder
# COPY scripts/* /opt/init_scripts/

## set the working directory
# WORKDIR /opt/init_scripts

# ENV VIRTUAL_ENV=/usr/local
# RUN pip3 install uv
# RUN uv pip install --no-cache -r /opt/init_scripts/${PIPENVFILE}

# ENV PYTHONPATH="${PYTHONPATH}:/home/mage_code"
# ENV PYTHONPATH="${PYTHONPATH}:/home/src"
# ENV MAGE_DATA_DIR="/home/src/mage_data"