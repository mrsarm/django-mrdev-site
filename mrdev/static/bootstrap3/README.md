Bootswatch
==========

Bootswatch is a collection of free themes for [Bootstrap](http://getbootstrap.com/). Check it out at [bootswatch.com](http://bootswatch.com).

Usage
-----
Download the `bootstrap.min.css` file associated with a theme and replace Bootstrap's default stylesheet.

The themes are also hosted on [BootstrapCDN](http://www.bootstrapcdn.com/).

Rails users should check out [twitter-bootswatch-rails](https://github.com/scottvrosenthal/twitter-bootswatch-rails).


Customization
------
Bootswatch is open source and you’re welcome to modify the themes.

Each theme consists of two LESS files. `variables.less`, which is included by default in Bootstrap, allows you to customize [these settings](http://getbootstrap.com/customize/#less-variables). `bootswatch.less` introduces more extensive structural changes.

These files are also available in SASS.

Check out the [Help page](http://bootswatch.com/help/) for more details on building your own theme.

API
-----

A simple API is available for integrating your platform with Bootswatch. Send your request to `http://api.bootswatch.com/3/`.

The swatch objects are returned in an array called `themes`, each one with the following properties:  `name`, `description`, `preview`, `thumbnail`, `css`, `cssMin`, `less`, and `lessVariables`.

More info at http://bootswatch.com/help/#api


Install and Build
------

To modify a theme or create your own, follow the steps below in your terminal. You'll need to have Git and Node installed.

   1. This folder is a copy of this repository (syncronize frequently to stay updated): https://github.com/thomaspark/bootswatch.git

   2. Install dependencies: ``npm install && grunt install``

   3. Make sure that you have grunt available in the command line. You can install grunt-cli as described on the Grunt Getting Started page.

   4. Modify variables.less and bootswatch.less in one of the theme directories, or create your own in /custom.

   5. Type grunt swatch:[theme] to build the CSS for a theme, e.g., grunt swatch:amelia for Amelia. Or type grunt swatch to build them all at once.

   6. You can run grunt to start a server, watch for any changes to the LESS files, and automatically build a theme and reload it on change. Run grunt server for just the server, and grunt watch for just the watcher.



Author
------
Thomas Park

+ http://github.com/thomaspark
+ http://thomaspark.co

Thanks
------
[Mark Otto](https://github.com/mdo) and [Jacob Thornton](https://github.com/fat) for [Bootstrap](https://github.com/twbs/bootstrap).

[Jenil Gogari](http://www.jgog.in/) for his contributions to the Flatly theme.

[James Taylor](https://github.com/jostylr) for [cors-lite](https://github.com/jostylr/cors-lite).

[Corey Sewell](https://github.com/cjsewell) for SASS conversion.


Copyright and License
----
Copyright 2014 Thomas Park

Code released under the MIT License.
