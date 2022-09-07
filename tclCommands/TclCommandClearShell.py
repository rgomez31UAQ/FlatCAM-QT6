from tclCommands.TclCommand import TclCommand
from ObjectCollection import *


class TclCommandClearShell(TclCommand):
    """
    Tcl shell command to creates a circle in the given Geometry object.

    example:

    """

    # List of all command aliases, to be able use old names for backward compatibility (add_poly, add_polygon)
    aliases = ['clear']

    # Dictionary of types from Tcl command, needs to be ordered
    arg_names = collections.OrderedDict([

    ])

    # Dictionary of types from Tcl command, needs to be ordered , this  is  for options  like -optionname value
    option_types = collections.OrderedDict([

    ])

    # array of mandatory options for current Tcl command: required = {'name','outname'}
    required = []

    # structured help for current command, args needs to be ordered
    help = {
        'main': "Clear the text in the Tcl Shell browser.",
        'args': collections.OrderedDict([
        ]),
        'examples': []
    }

    def execute(self, args, unnamed_args):
        """

        :param args:
        :param unnamed_args:
        :return:
        """
        self.app.inform.emit("Tcl Shell Editor cleared ...")
        self.app.shell._browser.clear()
        pass
