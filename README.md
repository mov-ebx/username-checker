<div align="center">
    <h1>Username checker</h1>
    <img width="400" src="https://i.giphy.com/media/WJOq6yKop0A1y/giphy.gif">
    <h3>Collection of username checkers for various platforms</h3>
    <h5>[WARNING]<br>Using this without proxies will likely leave you ratelimited and possibly banned from using any of these services.</h5>

[![Python 3.10](https://img.shields.io/badge/Python-3.10-bluesvg)](https://www.python.org/download/releases/3.0/)
[![GitHub license](https://img.shields.io/badge/license-GPL%203.0-green)](./LICENSE)
    <a href="https://github.com/mov-ebx">
        <img src="https://gpvc.arturio.dev/mov-ebx">
    </a>
</div>

## Star goals

5 :star: - Adding multi-threading

10 :star: - Improve speeds

## How do you use the checkers?

While you can use each checker indivdually in the [checkers directory](src/checkers/), the easiest way to use the checkers, is by using the launcher. The launcher is available in the [Releases](https://github.com/mov-ebx/username-checker/releases/latest) tab.

All you need is Python installed and the necessary [requirements](src/requirements.txt). I wrote the scripts in Python 3.10.6, so I'd recommend you [install that version](https://www.python.org/downloads/release/python-3106/). However, later versions should work too.

## How can I integrate the checkers in my projects?

You can easily integrate the checkers in your project, just make sure to follow the [license](LICENSE)!

Each script has a function inside of it called "run" which can be called with the necessary parameters.

Here's an example on how to integrate an example script in your project:

```py
import checkers.example
example.run(
    "words.txt", # usernames list path
    "proxies.txt" # proxies path (leave empty if no proxies)
)
```

## How do I use proxies in the checker?

In the same directory as the launcher, add a file named proxies.txt and format it like this:

```
type|type://host:port
```

an example is:

```
http|http://[redacted]:80
http|http://[redacted]:9992
http|http://[redacted]:80
https|https://[redacted]:8080
http|http://[redacted]:8085
http|http://[redacted]:3128
```
