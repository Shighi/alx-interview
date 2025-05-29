# 0x06. Star Wars API

## Description

This project focuses on interacting with an external API using Node.js. Specifically, you will use the [Star Wars API (SWAPI)](https://swapi-api.alx-tools.com/) to fetch and display data about characters in a Star Wars movie.

## Requirements

### General

* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted on **Ubuntu 20.04 LTS** using **Node.js v10.14.x**
* Files must end with a new line
* The first line of all your files should be:

  ```bash
  #!/usr/bin/node
  ```
* Code must follow **semistandard** style (Standard + semicolons)
* All files must be executable
* File length will be tested using `wc`
* You are **not allowed to use `var`**

### Installation

Install Node.js 10:

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Install `semistandard` for code style checks:

```bash
$ sudo npm install semistandard --global
```

Install the `request` module:

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

### 0. Star Wars Characters

**Mandatory**

Write a script that prints all characters of a Star Wars movie:

* The first positional argument passed is the Movie ID. For example: `3` = "Return of the Jedi".
* Display one character name per line in the same order as listed in the `characters` array in the `/films/` endpoint.
* You must use the Star Wars API.
* You must use the `request` module.

#### Example:

```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Repository Information

* GitHub repository: `alx-interview`
* Directory: `0x06-starwars_api`
* File: `0-starwars_characters.js`

## Author

**Daisy Mwambi**

---

> This project is part of the ALX Software Engineering Interview Preparation curriculum.

