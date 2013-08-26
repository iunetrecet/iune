iune.info
=========

Code and contents of [iune.info][iune].

The site uses [Hyde][hyde], the python version of Jekyll, the static site generator, along with some custom plugins witch make [Yammy][yammy] and [SASS][sass] (through [PySCSS][pyscss] work.


Installation
------------


    git clone https://github.com/iunetrecet/iune.git
    cd iune
    pip -r requirements.txt


Development server
------------------


    hyde gen && hyde serve


Deployment
----------


    hyde publish -p github



[iune]: http://iune.info
[hyde]: https://github.com/hyde/hyde
[yammy]: https://bitbucket.org/leporo/yammy
[sass]: http://sass-lang.com/
[pyscss]: https://github.com/Kronuz/pyScss
