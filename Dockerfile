FROM python:2-onbuild

RUN rm -rf .git && \
    rm -rf .gitignore && \
    rm -rf .travis.yml

EXPOSE 5000

CMD [ "python", "manage.py", "server" ]