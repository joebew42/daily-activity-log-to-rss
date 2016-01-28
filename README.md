# Daily Activity Log to RSS

[![Build Status](https://travis-ci.org/joebew42/daily-activity-log-to-rss.svg)](https://travis-ci.org/joebew42/daily-activity-log-to-rss)
[![Coverage Status](https://coveralls.io/repos/joebew42/daily-activity-log-to-rss/badge.svg?branch=master&service=github)](https://coveralls.io/github/joebew42/daily-activity-log-to-rss?branch=master)
[![Code Climate](https://codeclimate.com/github/joebew42/daily-activity-log-to-rss/badges/gpa.svg)](https://codeclimate.com/github/joebew42/daily-activity-log-to-rss)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/joebew42/daily-activity-log-to-rss?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

A web application that converts a [**Daily Activity Log**](https://github.com/joebew42/daily-activity-log)
into a **RSS feed**

Live app at: `https://daily2rss.herokuapp.com/rss/` ([example](https://daily2rss.herokuapp.com/rss/?url=http://joebew42.github.io/events))

## Usage

Visits `https://daily2rss.herokuapp.com/rss/?url=XXX`

Where `XXX` is an URL pointing to a Daily Activity Log.

# Getting started

To start the application

1. Install dependencies with `pip install -r requirements.txt`
2. Start the server with `./manage.py server`
3. Visit the service at `http://localhost:5000/rss/?url=XXX`

Where `XXX` is a valid [**Daily Activity Log**](https://github.com/joebew42/daily-activity-log) URL.

_Example:_

`http://localhost:5000/rss/?url=http://joebew42.github.io/events.xml`

To run all tests

1. Unit tests with `./manage.py test`
2. Integration tests with `./manage.py integration-test`

# Try it with Docker

## Run from the official Docker image

```
$ docker run -d -p 5000:80 joebew42/daily2rss:latest
```

Visits `http://localhost/rss/?url=http://joebew42.github.io/events`

## Build and run from scratch

```
$ docker build -t daily2rss:latest --rm=true .
$ docker run -d -p 5000:80 daily2rss:latest
```

Visits `http://localhost/rss/?url=http://joebew42.github.io/events`

# Contributing

## Submit issue

If you have any suggestions (ex. `bug`, `refactoring`, `feature`, or other), please report an
[issue](https://github.com/joebew42/daily-activity-log-to-rss/issues) and rememeber to use tags properly.

## Improve the code

1. Fork it ( https://github.com/joebew42/daily-activity-log-to-rss )
2. Create your feature branch (git checkout -b my-new-feature)
3. Write tests or integration tests for your feature, or regression tests highlighting a bug
4. Write the feature itself, or fix your bug
5. Commit your changes (`git commit -am 'Add some feature'`)
6. Push to the branch (`git push origin my-new-feature`)
7. Create a new Pull Request

_Remember to squash your commits and rebase off master._

## About the code

The code is developed following the `IDD` (Interaction Driven Design)
that was presented by [Sandro Mancuso](https://github.com/sandromancuso) in his various
talks ([Lean Agile Scotland](https://vimeo.com/107963074), [jax 2014 London](https://vimeo.com/128596005)).
I also wrote some [notes](http://joebew42.github.io/notes/20150712SandroMancuso_CraftedDesign.txt)
in which I tried to summarize the concepts behind `Clean Software Architecture`, `IDD` and the development workflow.
