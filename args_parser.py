import argparse
import logging
import re
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description="Slow HTTP Attacker, a tool providing three types of slow HTTP attack."
    )
    parser.add_argument("url", nargs="?", help='URL to perform stress test on. ("http[s]://<host>[:port][/path]")')
    parser.add_argument(
        "-m", "--mode", default='header',
        help='Mode of attack. The supported options are "header", "post" and "read". ("header" by default)',
        type=str
    )
    parser.add_argument(
        "-s",
        "--sockets",
        default=150,
        help="Number of sockets to use in the test",
        type=int,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="Increases logging",
    )
    parser.add_argument(
        "-ua",
        "--randuseragents",
        dest="randuseragent",
        action="store_true",
        help="Randomizes user-agents with each request",
    )
    parser.add_argument(
        "--sleeptime",
        dest="sleeptime",
        default=15,
        type=int,
        help="Time to sleep between beats",
    )
    parser.add_argument(
        "-w", "--window",
        dest="window",
        default=1,
        type=int,
        help="The window size used in Read mode (1 by default)",
    )
    parser.set_defaults(verbose=False)
    parser.set_defaults(randuseragent=False)

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    args.mode = args.mode.lower()

    if args.mode not in ['header', 'post', 'read']:
        print('Unsupported mode. The supported modes are "header", "post" and "read".')
        sys.exit(1)

    if args.verbose:
        logging.basicConfig(
            format="[%(asctime)s] %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",
            level=logging.DEBUG,
        )
    else:
        logging.basicConfig(
            format="[%(asctime)s] %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",
            level=logging.INFO,
        )

    m = re.fullmatch(r'(?P<protocol>https?)://(?P<host>[^:/]*)(:(?P<port>\d*))?(?P<path>/.*)?', args.url)
    if m is None:
        print('URL needs to be like "http[s]://<host>[:port][/path]"')
        sys.exit(1)
    https = True if m.group('protocol') == 'https' else False
    host = m.group('host')
    port = int(m.group('port')) if m.group('port') is not None else 80
    path = m.group('path') if m.group('path') is not None else '/'
    return args, https, host, port, path
