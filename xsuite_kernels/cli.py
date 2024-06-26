# copyright ############################### #
# This file is part of the Xsuite project.  #
# Copyright (c) CERN, 2024.                 #
# ######################################### #
import argparse
from importlib.metadata import version

from xsuite_kernels.prebuild_kernels import (
    clear_kernels, regenerate_kernels, XSK_PREBUILT_KERNELS_LOCATION,
)


def regenerate_command(args):
    regenerate_kernels()
    print('Kernels regenerated.')


def clean_command(args):
    clear_kernels(verbose=args.verbose)
    print('Cleaned kernels.')


def info_command(args):
    version_str = version("xsuite_kernels")
    print(f'Xsuite kernels version {version_str}')
    print(f'Kernels location: {XSK_PREBUILT_KERNELS_LOCATION}')


def main():
    parser = argparse.ArgumentParser(
        prog='xsuite-kernels',
        description='Regenerate and clean precompiled kernels for Xsuite.',
    )
    subparsers = parser.add_subparsers(
        title='commands',
        required=True,
    )

    # `regenerate` commend
    regenerate_parser = subparsers.add_parser(
        'regenerate',
        description='Regenerate the kernels.'
    )
    regenerate_parser.set_defaults(func=regenerate_command)

    # `clean` command
    clean_parser = subparsers.add_parser(
        'clean',
        description='Clean the kernel directory.'
    )
    clean_parser.add_argument(
        '-v', '--verbose',
        help='list the files being deleted',
        action='store_true',
    )
    clean_parser.set_defaults(func=clean_command)

    # `info` command
    info_parser = subparsers.add_parser(
        'info',
        description='Print additional info.',
    )
    info_parser.set_defaults(func=info_command)

    # handle the right action
    args = parser.parse_args()
    args.func(args)
