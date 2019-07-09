<p align="center">
写真立て (shashintate)
<br />
<strong>DIY Digital Picture Frame</strong>
</p>

An easy to use set of scripts, configs, and software for setting up a digital picture frame. This has been designed and developed with RaspberryPi in mind, but can be used with other setups.

<hr />

## Install

### Setup the server.

This is all based on a fresh install of a RaspberryPi OS install with the GUI.

```shell
$ sudo apt-get install git openssh-server pqiv libpng-dev libjpg-dev supervisor
$ sudo systemctl enable ssh
$ sudo systemctl enable supervisor
```

### Hostname (Optional)

If you change the host name you can use `avahi/bonjour/zeroconf` to rever to the server based on the host name. On the RaspberryPi `avahi` is already running. Just change the host name and reboot.

Change `/etc/hostname`.

```
pictureframe
```

From here you will be able to visit http://pictureframe:8000

### Viewer

We will use `pqiv` to display images as a slideshow since it has the slideshow feature built-in, and can be configured via a config file.

Add `~/.config/pqivrc`

```ini
[options]
fullscreen=1
slideshow=1
shuffle=1
slideshow-interval=10
hide-info-box=1
scale-images-up=1
low-memory=1
watch-directories=1
```

### Web Site

The website is a custom django based website used for uploading images to the digital picture frame through a web portal. For now it lets you manage the images, later you will be able to do more.

```shell
$ git clone https://github.com/buddylindsey/shashinta.git
$ cd shashinta/web
$ python3 -m venv .venv --prompt=shashinta
$ source .venv/bin/activate
$ ./manage.py migrate
$ mkdir -p media/images/
$ ./manage.py import_images
```

### Supervisor

We use supervisor to run both the website, and the viewer as a background process. Supervisor also helps to manage the process so if it goes down it will bring it back up. It also will start the process up on boot so it "just starts".

```shell
$ cd ~/shashinta/supervisor
$ sudo cp viewer.conf /etc/supervisor/conf.d/
$ sudo cp web.conf /etc/supervisor/conf.d/
$ sudo supervisorctl reload
```

### Reboot

Now that everything is installed and in place you should be able to reboot and start using it.

```shell
$ sudo shutdown -r now
```

## Contribute

Contributions are welcome. Feel free to ask questions and add PRs.
