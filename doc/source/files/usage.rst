.. _usage:

*****
Usage
*****

Server
######
Options provided by ThugD

.. code-block:: sh
        
        ~/thugd/src $ python run_tasks -h

        Synopsis:
            ThugD: Distributed Pure Python Honeyclient Implementation

            Usage: python run_tasks.py [ thug-options ] url

            Optional Arguments:
            -h, --help                      show this help message and exit

            URL Options:
            -U  [ ...], --url  [ ...]       Enter Single/Multiple URL's to Analyze
            -uf , --url-file                File containing bunch of URL's(1 per line)

            Thug Distributed Options:
            -ia, --include-agent            Display Thug Version
            -qu  [ ...], --queue  [ ...]    Specify Queue/Queues to route URL's 
                                           (*Single Queue: URL's will be routed to specified Queue,
                                            *Multiple Queues: URL's will be routed to ALL specified Queues)
            -qf , --queue-file              Specify File name containing Queue names(1 per line)

            Thug Options:
            -V, --version                   Display Thug Version
            -u , --useragent                Select a user agent(see below for values, default: winxpie60)
            -e , --events                   Enable comma-separated specified DOM events handling
            -w , --delay                    Set a maximum setTimeout/setInterval delay value (in milliseconds)
            -n , --logdir                   Set the log output directory
            -o , --output                   Log to a specified file
            -r , --referer                  Specify a referer
            -p , --proxy                    Specify a proxy (see below for format and supported schemes)
            -l, --local                     Analyze a locally saved page
            -x, --local-nofetch             Analyze a locally saved page and prevent remotecontent fetching
            -v, --verbose                   Enable verbose mode
            -d, --debug                     Enable debug mode
            -q, --quiet                     Disable console logging
            -m, --no-cache                  Disable local web cache
            -a, --ast-debug                 Enable AST debug mode (requires debug mode)
            -t , --threshold                Maximum pages to fetch
            -E, --extensive                 Extensive fetch of linked pages
            -T , --timeout                  Timeout in minutes

            Plugins:
            -A , --adobepdf                 Specify the Adobe Acrobat Reader version (default: 9.1.0)
            -P, --no-adobepdf               Disable Adobe Acrobat Reader Plugin
            -S , --shockwave                Specify the Shockwave Flash version (default: 10.0.64.0)
            -R, --no-shockwave              Disable Shockwave Flash Plugin
            -J , --javaplugin               Specify the Java Plugin version (default: 1.6.0.32)
            -K, --no-javaplugin             Disable Java Plugin

            Classifiers:
            -Q , --urlclassifier            Specify a list of additional (comma separated) URL classifier rule files
            -W , --jsclassifier             Specify a list of additional (comma separated) JS classifier rule files

            Available User-Agents:
            winxpie60               Internet Explorer 6.0   (Windows XP)
            winxpie61               Internet Explorer 6.1   (Windows XP)
            winxpie70               Internet Explorer 7.0   (Windows XP)
            winxpie80               Internet Explorer 8.0   (Windows XP)
            winxpchrome20           Chrome 20.0.1132.47     (Windows XP)
            winxpfirefox12          Firefox 12.0            (Windows XP)
            winxpsafari5            Safari 5.1.7            (Windows XP)
            win2kie60               Internet Explorer 6.0   (Windows 2000)
            win2kie80               Internet Explorer 8.0   (Windows 2000)
            win7ie80                Internet Explorer 8.0   (Windows 7)
            win7ie90                Internet Explorer 9.0   (Windows 7)
            win7chrome20            Chrome 20.0.1132.47     (Windows 7)
            win7firefox3            Firefox 3.6.13          (Windows 7)
            win7safari5             Safari 5.1.7            (Windows 7)
            osx10safari5            Safari 5.1.1            (MacOS X 10.7.2)
            osx10chrome19           Chrome 19.0.1084.54     (MacOS X 10.7.4)
            galaxy2chrome18         Chrome 18.0.1025.166    (Samsung Galaxy S II,Android 4.0.3)
            galaxy2chrome25         Chrome 25.0.1364.123    (Samsung Galaxy S II,Android 4.0.3)
            linuxchrome26           Chrome 26.0.1410.19     (Linux)
            linuxfirefox19          Firefox 19.0            (Linux)


1. Single URL with Default Queue(generic)

.. code-block:: sh
        
		~/thugd/src$ python run_tasks.py -U http://www.google.com
		
2. Single URL with Single Specified Queue(India)

.. code-block:: sh
        
		~/thugd/src$ python run_tasks.py -qu IN -U http://www.google.com

3. Single URL with Multiple Specified Queues(India, Italy, China, US)

.. code-block:: sh
        
		~/thugd/src$ python run_tasks.py -qu IN IT CN US -U http://www.google.com

4. Multiple URL's(Google, Twitter, Mozilla) with Single Specified Queue(India)

.. code-block:: sh
        
		~/thugd/src$ python run_tasks.py -qu IN -U http://www.google.com http://www.twitter.com http://www.mozilla.com
		
5. Multiple URL's(Google, Twitter, Mozilla) with Multiple Specified Queues(India, Italy, China, US)

.. code-block:: sh
        
		~/thugd/src$ python run_tasks.py -qu IN IT CN US -U http://www.google.com http://www.twitter.com http://www.mozilla.com

6. Multiple URL's from file(urls.txt) with Multiple Specified Queues from file(queues.txt)

.. code-block:: sh
        
		~/thugd/src$ python run_tasks.py -qf queues.txt -uf urls.txt

7. Running Thug with following prioritized Agents: Multiple URL's from file(urls.txt) with Multiple Specified Queues from file(queues.txt)

.. code-block:: sh
        
		~/thugd/src$ python run_tasks.py -qf queues.txt -uf urls.txt -ia

**Agents Priority**

.. code-block:: sh

    win7chrome20
    win7firefox3
    win7ie90
    win7safazi5
    osx10chrome19
    osx10safari5
    linuxchrome26
    linuxfirefox19
    win7ie80
    winxpchrome20
    winxpfirefox12
    winxpie80
    winxpsafari5
    winxpie70
    win2kie80
    win2kie60
    galaxy2chrome25
    galaxy2chrome18


Run Flower(optional)
********************

.. code-block:: sh

		$ flower
		
Open `<http://localhost:5555/>`_ to access the tool.    

		
Checking Active Queues
**********************

.. code-block:: sh

		$ sudo rabbitmqctl list_queues

Worker
######

Move inside the **src** folder of thugd

**Single Worker**

.. code-block:: sh

		~/thugd/src$ celery worker -A ThugD.main_server.thugd -l info -n w1

**Multiple Workers**

.. code-block:: sh

		~/thugd/src$ celery multi start w1 w2 w3 -A ThugD.main_server.thugd -l info
		
		

