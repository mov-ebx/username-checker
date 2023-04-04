<div align="center">
    <h1>Username checker</h1>
    <h3>Collection of username checkers for various platforms. Proxyless and proxy support!</h3>
    <h5>[WARNING]<br>Using this without proxies will likely leave you ratelimited and possibly banned from using any of these services.</h5>

[![Python 3.10 and up](https://img.shields.io/badge/Python-3.10%20and%20up-bluesvg)](https://www.python.org/download/releases/3.0/)
[![GitHub license](https://img.shields.io/badge/license-GPL%203.0-green)](./LICENSE)
    <a href="https://github.com/mov-ebx">
        <img src="https://gpvc.arturio.dev/mov-ebx">
    </a>
</div>

## Current progress:
<details>
<summary>List of supported websites</summary>

- [Chess.com](https://chess.com)
- [Discord](https://discord.gg) (vanity)
- [Fornite](https://fortnite.com)
- [GitHub](https://github.com)
- [Gmail](https://gmail.com)
- [Instagram](https://instagram.com)
- [Kahoot](https://kahoot.com)
- [Lichess](https://lichess.org)
- [Minecraft](https://minecraft.net)
- [Pastebin](https://pastebin.com)
- Pornhub (haram)
- [Replit](https://replit.com)
- [Roblox](https://roblox.com)
- [Solo.to](https://solo.to)
- [Soundcloud](https://soundcloud.com)
- [Speedrun.com](https://speedrun.com)
- [Steam](https://store.steampowered.com)
- [TikTok](https://tiktok.com)
- [Twitch](https://twitch.tv)
- [Twitter](https://twitter.com)
- [Xbox](https://xbox.com)
- [YouTube](https://youtube.com) (/c/ and @)

There is also support for adding your own checkers by supplying an API endpoint.

</details>
<details>
<summary>Star goals</summary>

- [x] :star:5  - Adding multi-threading
- [x] :star:7  - More advanced custom checkers
- [x] :star:10 - Improved speeds
- [x] :star:15 - 1 new checker
- [x] :star:20 - 1 new checker
- [x] :star:30 - 5 new checkers
- [x] :star:35 - 2 new checkers
- [ ] :star:40 - Improved speeds

</details>

## How do you use the checkers?

While you can use each checker individually in the [checkers directory](src/checkers/), the easiest way to use the checkers, is by using the launcher. The launcher is available in the [Releases](https://github.com/mov-ebx/username-checker/releases/latest) tab.

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
) # returns list of hits
```

For the run function, if you check the code, you might see a "usernames" parameters. DO NOT USE THAT PARAMETER, that is used by previous versions of the launcher, and allows for backwards compatability support. If you use that rather than the "usernames_path" parameter, instead of returning a set of all the valid usernames, it will rather return nothing and automatically download the valid usernames to a file called "hits.txt". Make what you will of this information.

You can also check 1 username at a time, here's an example:

```py
import checkers.example
example.check(
    "Example", # username
    "127.0.0.1:80" # proxy (leave empty if no proxy)
) # returns the username if valid, or None if its not
```

As far as I know, the "custom" checker doesn't work with the individual "check" function, however the "run" function should work.

## How do I use proxies in the checker?

In the same directory as the launcher, add a file named proxies.txt and format it like this:

```
type|protocol://host:port
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

## Do I need to re-download each update?

In short, no.

The launcher automatically updates checkers, however some larger features such as multi-threading (support added in launcher beta 0.2) require launcher updates to use, however launcher updates are mostly QOL or bug fixes and are recommended! My goal is to make it so you can use this in any launcher version possible, with full backwards compatibility!
