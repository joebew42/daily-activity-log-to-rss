FROM joebew42/daily2rss-onbuild:latest

RUN rm -rf .git && \
    rm -rf .gitignore && \
    rm -rf .travis.yml

EXPOSE 5000

CMD [ "python", "manage.py", "server" ]