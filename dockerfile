# Dockerfile



# FROM directive instructing base image to build upon
FROM python:3.6

# COPY startup script into known file location in container
COPY start.sh /start.sh

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["sh","/usr/src/app/start.sh"]
# done!
