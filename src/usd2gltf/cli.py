import argparse
import sys
import logging

try:
    import pxr  # noqa: F401 — OpenUSD; PyPI package name is usd-core
except ImportError:
    print(
        "usd2gltf needs OpenUSD Python bindings (the `pxr` module).\n"
        "  • With pip: install a supported Python (3.9–3.13), then: pip install usd-core\n"
        "  • The `usd-core` wheel on PyPI does not support Python 3.14 yet.\n"
        "  • Or use a Pixar USD build and add its `lib/python` (or equivalent) to PYTHONPATH.",
        file=sys.stderr,
    )
    sys.exit(1)

import usd2gltf.converter as converter


def run(args):
    print("Converting: {0}\nTo: {1}".format(args.input, args.output))
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    factory = converter.Converter()
    factory.interpolation = args.interpolation
    factory.flatten_xform_animation = args.flatten

    stage = factory.load_usd(args.input)
    factory.process(stage, args.output)

    print("Converted!")


def main():
    parser = argparse.ArgumentParser(
        description="Convert incoming USD(z) file to glTF/glb"
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        action="store",
        help="Input USD (.usd, .usdc, .usda, .usdz)",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        action="store",
        help="Output glTF (.gltf, .glb)",
    )

    parser.add_argument(
        "--interpolation",
        dest="interpolation",
        action="store",
        default="LINEAR",
        help="Interpolation of animation (LINEAR, STEP, CUBIC)",
    )

    parser.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="Run in debug mode",
    )

    parser.add_argument(
        "-f",
        "--flatten",
        dest="flatten",
        action="store_true",
        default=False,
        help="Flatten all animations into one animation",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
