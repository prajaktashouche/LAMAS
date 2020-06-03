# Game Analysis: I Doubt It

Github files supporting the LAMAS project. An analysis of the game - I Doubt It. Website can be accessed [here](https://prajaktashouche.github.io/LAMAS/)

## Edit on GitHub

Make changes to the markdown file to add content

Example [here](https://github.com/pages-themes/cayman/blob/master/index.md)

## Edit on local machine

### Install Jekyll
Follow instructions on https://jekyllrb.com/

(Windows installation can be tricky)

### Clone the repository
`git clone https://github.com/prajaktashouche/LAMAS.git`

### Bundle Commands

* Use your favorite terminal
* Go to directory `LAMAS/docs`
* In the terminal `bundle install` or `bundle update` if project is already existing. Any changes to the `gem` file, you need to run the update command.

* To build the static pages
```
$ bundle exec jekyll build
```

* To serve the pages on local server
```
$ bundle exec jekyll serve
```

Website can be viewed on http://127.0.0.1:4000

### Adding Content to Pages

Use the markdown files - `index.md`, `theory.md`, `example.md`, etc.

Example [here](https://github.com/pages-themes/cayman/blob/master/index.md)


### Adding/Removing Pages

* Adding Page

> Add as markdown file under `docs/new_page.md`
>
> Add in navigation - `docs/_data/nav.yml`
>
> ```
> - title: new-page-title
>   url: new_page.html
> ```
>

* Removing Page

> Remove from root directory
>
> Remove from navigation - `docs/_data/nav.yml`
