FROM localhost/rpaservice:latest

RUN mkdir /rpa
COPY  requirement.txt  /rpa
COPY  rpaserver.py /rpa

COPY  t.robot /rpa

RUN   pip install robotframework \
                  uvicorn \
                  PyYAML \
                  robotframework-seleniumlibrary \
                  fastapi

