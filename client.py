from socket import *
import sys, argparse


def main():
    args = parser.parse_args()
    if not args.sampleName:
        sys.exit()

    sample_info = args.sampleName

    socket_con = socket(AF_INET, SOCK_STREAM)
    socket_con.connect(('192.168.77.6', 7777))

    socket_con.send(sample_info.encode('utf-8'))
    socket_con.shutdown(SHUT_RDWR)
    socket_con.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Request sample")
    parser.add_argument(
        '-s', '--sampleName', help='Sample name', required=True)

    main()
