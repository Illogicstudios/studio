import sys
import importlib

if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/studio'
    if not sys.path.__contains__(install_dir):
        sys.path.append(install_dir)

    modules = [
        "studio_loader"
    ]

    from utils import *
    unload_packages(silent=True, packages=modules)

    for module in modules:
        importlib.import_module(module)

    import studio_loader

    studio_loader.run()
