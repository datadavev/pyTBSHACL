"""

"""
import sys
import argparse
import logging
import tbshacl

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-l', '--log_level',
                        action='count',
                        default=0,
                        help='Set logging level, multiples for more detailed.')
    parser.add_argument("-d","--datafile",
                        default=None,
                        help="Path to data file in turtle format")
    parser.add_argument("-s","--shapefile",
                        default=None,
                        help="Optional path to shape file in turtle format")
    args = parser.parse_args()
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels) - 1, args.log_level)]
    logging.basicConfig(level=level,
                        format="%(asctime)s %(levelname)s %(message)s")
    if args.datafile is None:
        logging.error("Datafile is required.")
        return 1
    resout, reserr = tbshacl.tbShaclValidate(args.datafile, shape_file=args.shapefile)
    if resout is None:
        return 2
    print("stdout=\n" + resout.decode())
    print("stderr=\n" + reserr.decode())
    return 0

if __name__ == "__main__":
    sys.exit(main())