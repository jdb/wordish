

Configuration
=============

default = {
    "parse_cmd_hint"      : True,
    "prompts"             : ["~# ", "~$ "],
    "verbose"             : False,
    "parse_stderr"        : True,
    "shell"               : "bash",
    "match_method"        : "ellipsis",
    "directive_filter"    : "sourcecode",
    "directive_arguments" : ["sh"],
    }



How it is done
--------------

The classes of the module can have two different behavior:

- Either the different objects trust the existence, and validity of
  the points of configuration in a global object which integrated in
  the module,

- or they do their own checking and embed their own default value and
  they defend themselves against a corrupted configuration,

It is not too difficult for the module objects to trust the
configuration which is also embedded in the module.

There is a dictionary containing the default value, which is loaded by
the global configuration instance and which is further customized by
command line argument or hints in command line comments.
