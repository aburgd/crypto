FROM python:3.6.0-onbuild
RUN pip install -r requirements.txt
RUN python setup.py install
CMD python ./crypto.py && pytest