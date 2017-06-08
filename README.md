# nnhejmo (novanovahejmo)

![nnh](https://a.pomf.cat/suipzh.png)

### Dependencies

`mako`

### Get it

`git clone https://bitbucket.org/underr/nnhejmo && cd nnhejmo`

`cp links.ex.ho links.ho`

`make`

### Customize it

You can change and add you're links using the `links.ho` file. 
It follows the minimal homeru's syntax (documented later). 
Nnhejmo's template may be changed with the `tmpl.html` file.

### make commands:

`make` builds the page

`clean` removes index.html

`watch` uses [wendy](http://git.z3bra.org/cgit.cgi/wendy/) to watch for changes
to the `tmpl.html` file and rebuilds `index.html` (good for when you're changing something)

### Attention:

__nnhjemo is configured by a occult file named .links.ho that should be placed on
your $HOME folder;__

__run ``cp links.ho ~/.links.ho`` to get a base file.__

### homeru

**homeru** is a useless format targeted at ~~this project~~ homepages. It uses
the .ho extension.

A homeru file looks like this:

```
# 1 wikis
https://www.wikipedia.org wikipedia 3
https://wiki.archlinux.org/index.php 2
http://emulation-general.wikia.com/wiki/Emulation_General_Wiki 1
# 2 search engines
http://www.bing.com bing 3
https://duckduckgo.com ddg 2 
https://google.com google 1

```

Lines starting with # delimit a category.
Following lines belong to the previous declared category.
Each line follows the format "[url] [name] [priority]", where priority determines the size and color of the link (that can be customized on homeru.py).



