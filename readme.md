# overwatch2-unix

In case you encounter some issues, make sure you are up to date with [dependencies].

[dependencies]: https://github.com/lutris/docs/blob/master/WineDependencies.md

### instructions

**1. dependencies:**

- patched wine, such as [wine-tkg-git] or something like gloriousegroll's wine-ge
- jq, aria2, winetricks, tar, jq

**2. battle.net installer**

run `./prepare`. if its permissions aren't set properly, run `chmod +x prepare`
it will let you configure the installation as usual, but be sure to let it install to
the default directory. do not login after installation, just let the installer run once
then close it.

now you can run `./fixes`, which will allow you to run everything smoothly.

**3. launching**

every time you need to launch the battle.net launcher, you can use the `./launch` script
