from urllib2 import urlopen
import argparse

agents_priority = [
    'win7chrome20',
    'win7firefox3',
    'win7ie90',
    'win7safari5',
    'osx10chrome19',
    'osx10safari5',
    'linuxchrome26',
    'linuxfirefox19',
    'win7ie80',
    'winxpchrome20',
    'winxpfirefox12',
    'winxpie80',
    'winxpsafari5',
    'winxpie70',
    'win2kie80',
    'win2kie60',
    'galaxy2chrome25',
    'galaxy2chrome18'
    ]

def parsing():
    """ Parsing the Command Line Arguments by using ArgParse Module """
    # User Agents
    user_agents = '''
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
    galaxy2chrome18         Chrome 18.0.1025.166    (Samsung Galaxy S II,\
Android 4.0.3)
    galaxy2chrome25         Chrome 25.0.1364.123    (Samsung Galaxy S II,\
Android 4.0.3)
    linuxchrome26           Chrome 26.0.1410.19     (Linux)
    linuxfirefox19          Firefox 19.0            (Linux)
    '''
    
    # Description of Command Line arguments    
    parser = argparse.ArgumentParser(description='Distributed Pure Python \
Honeyclient Implementation',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    usage='python %(prog)s [ thug-options ] url',
    fromfile_prefix_chars='@',
    epilog=user_agents)

    def link(urls):
        links = urls.strip().split(',')
        for url in links:
            try:
                if 'http://' not in url:
                    url = 'http://' + url
                urlopen(url)
            except:
                raise argparse.ArgumentTypeError("%s doesn't exist"%url)
        return urls
        
    def link_file(fn):
        fobj = open(fn, 'r')
        url = fobj.readline().strip()
        urls = []
        while url:
            try:
                if 'http://' not in url:
                    url = 'http://' + url
                urlopen(url)
                urls.append(url)
            except:
                raise argparse.ArgumentTypeError("%s doesn't exist"%url)
            url = fobj.readline().strip()
        return urls

    # Mutually Exclusive Group for URL's
    links = parser.add_argument_group('URL Options')
    url = links.add_mutually_exclusive_group(required=True)
    url.add_argument('-U', '--url',
                        metavar='',
                        type=link,
                        nargs='+',
                        help="Enter Single/Multiple URL's to Analyze")
    url.add_argument('-uf', '--url-file',
                        metavar='',
                        type=link_file,
                        help="File containing bunch of URL's(1 per line)")

    def qfile(fn):
        fobj = open(fn, 'r')
        queues = fobj.readlines()
        queues = map((lambda x: x.replace('\n', '')), queues)
        return queues

    # ThugD Options
    thugd = parser.add_argument_group('Thug Distributed Options')
    thugd.add_argument('-ia', '--include-agent',
                        action='store_const',
                        const=agents_priority,
                        help='Display Thug Version')
    # Queues Mutually Exclusive Group
    queue = thugd.add_mutually_exclusive_group(required=False)
    queue.add_argument('-qu', '--queue',
                        nargs='+',
                        metavar='',
                        default='generic',
                        help="Specify Queue/Queues to route URL's \
(*Single Queue: URL's will be routed to specified Queue, \
*Multiple Queues: URL's will be routed to ALL specified Queues)")
    queue.add_argument('-qf', '--queue-file',
                        metavar='',
                        type=qfile,
                        help="Specify File name containing Queue names(1 per \
line)")

    # Thug Options
    thug = parser.add_argument_group('Thug Options')
    thug.add_argument('-V', '--version',
                        action='store_true',
                        help='Display Thug Version')
    thug.add_argument('-u', '--useragent',
                        metavar='',
                        default='winxpie60',
                        help='Select a user agent(see below for values, \
default: winxpie60)')
    thug.add_argument('-e', '--events',
                        metavar='',
                        help='Enable comma-separated specified DOM events \
handling')
    thug.add_argument('-w', '--delay',
                        metavar='',
                        help='Set a maximum setTimeout/setInterval delay value \
(in milliseconds)')
    thug.add_argument('-n', '--logdir',
                        metavar='',
                        help='Set the log output directory')
    thug.add_argument('-o', '--output',
                        metavar='',
                        help='Log to a specified file')
    thug.add_argument('-r', '--referer',
                        metavar='',
                        help='Specify a referer')
    thug.add_argument('-p', '--proxy',
                        metavar='',
                        help='Specify a proxy (see below for format and \
supported schemes)')
    thug.add_argument('-l', '--local',
                        action='store_true',
                        help='Analyze a locally saved page')
    thug.add_argument('-x', '--local-nofetch',
                        action='store_true',
                        help='Analyze a locally saved page and prevent remote\
content fetching')
    thug.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Enable verbose mode')
    thug.add_argument('-d', '--debug',
                        action='store_true',
                        help='Enable debug mode')
    thug.add_argument('-q', '--quiet',
                        action='store_true',
                        help='Disable console logging')
    thug.add_argument('-m', '--no-cache',
                        action='store_true',
                        help='Disable local web cache')
    thug.add_argument('-a', '--ast-debug',
                        action='store_true',
                        help='Enable AST debug mode (requires \
debug mode)')
    thug.add_argument('-t', '--threshold',
                        metavar='',
                        help='Maximum pages to fetch')
    thug.add_argument('-E', '--extensive',
                        action='store_true',
                        help='Extensive fetch of linked pages')
    thug.add_argument('-T', '--timeout',
                        metavar='',
                        help='Timeout in minutes')

    # Plugins
    plugin = parser.add_argument_group('Plugins')
    plugin.add_argument('-A', '--adobepdf',
                        metavar='',
                        default='9.1.0',
                        help='Specify the Adobe Acrobat Reader version \
(default: 9.1.0)')
    plugin.add_argument('-P', '--no-adobepdf',
                        action='store_true',
                        help='Disable Adobe Acrobat Reader Plugin')
    plugin.add_argument('-S', '--shockwave',
                        metavar='',
                        default='10.0.64.0',
                        help='Specify the Shockwave Flash version \
(default: 10.0.64.0)')
    plugin.add_argument('-R', '--no-shockwave',
                        action='store_true',
                        help='Disable Shockwave Flash Plugin')
    plugin.add_argument('-J', '--javaplugin',
                        metavar='',
                        default='1.6.0.32',
                        help='Specify the Java Plugin version (default: \
1.6.0.32)')
    plugin.add_argument('-K', '--no-javaplugin',
                        action='store_true',
                        help='Disable Java Plugin')

    # Classifier
    classifier = parser.add_argument_group('Classifiers')
    classifier.add_argument('-Q', '--urlclassifier',
                            metavar='',
                            help='Specify a list of additional (comma \
separated) URL classifier rule files')
    classifier.add_argument('-W', '--jsclassifier',
                            metavar='',
                            help='Specify a list of additional (comma \
separated) JS classifier rule files')

    return parser.parse_args()

if __name__ == "__main__":
    # Parsing the Command Line Arguments
    args = parsing()
    print vars(args)
    