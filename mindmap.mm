<map version="0.7.1">
<node TEXT="wordish">
<node TEXT="What is wordish?" POSITION="right">
<node TEXT="readme"/>
<node TEXT="man"/>
<node TEXT="wordish --help"/>
<node TEXT="presentation"/>
<node TEXT="installation and verification"/>
</node>
<node TEXT="writing articles" POSITION="right">
<node TEXT="parsing method (prompts, nesting)"/>
<node TEXT="matching methods (ignoring, ellipsis, re)"/>
<node TEXT="one subshell for the session"/>
<node TEXT="working examples: raid, lvm, deb, git, ssh, ipvsadm"/>
</node>
<node TEXT="object model and interfaces" POSITION="right">
<node TEXT="overview"/>
<node TEXT="parser"/>
<node TEXT="output and runner"/>
<node TEXT="reporter"/>
</node>
<node TEXT="software engineering" POSITION="right">
<node TEXT="source, branches and versions"/>
<node TEXT="doctests and unit tests"/>
<node TEXT="packaging">
<node TEXT="facts">
<node TEXT="scripts are placed at install in ./bin in a virtual env"/>
<node TEXT="console script entry point requires eggs"/>
<node TEXT="distutils.core.setup install from pristine source says &apos;running egg_info&apos;"/>
<node TEXT="setup --help-commands tell nothin about eggs"/>
</node>
<node TEXT=""/>
<node TEXT=""/>
<node TEXT="does distribute make eggs? it is talking about eggs anyway"/>
<node TEXT="mention in the doc that working on the setup.py is eased by a virtualenv"/>
<node TEXT="test package_data and data_files, where do they end up?"/>
<node TEXT="distutils, distribute, pip"/>
<node TEXT="content">
<node TEXT="one module"/>
<node TEXT="one test file"/>
<node TEXT="man page, README.rst"/>
<node TEXT="setup.py"/>
<node TEXT="four examples"/>
<node TEXT="MANIFEST"/>
<node TEXT="build"/>
<node TEXT="sdist"/>
</node>
</node>
</node>
<node TEXT="limitations, roadmap and crazy ideas" POSITION="right">
<node TEXT="setup.py and entry point"/>
<node TEXT="rst builder, sphinx builder"/>
<node TEXT="doctests to unittests"/>
<node TEXT="quiet mode without output"/>
<node TEXT="universal linefeed for commands in win articles"/>
<node TEXT="list commands used and version"/>
<node TEXT="at bailout, show rest to help cleanup and help debug"/>
<node TEXT="interactive via cmds.py or screen (tty?), confirm, insert command, ctrl-C ..."/>
<node TEXT="executable article with #!/usr/bin/wordish"/>
<node TEXT="other parsing format, markdown"/>
<node TEXT="hints in a command&apos;s comments" FOLDED="true">
<node TEXT="ignore"/>
<node TEXT="input"/>
<node TEXT="&amp;2"/>
</node>
<node TEXT="differentiate the error and failure in the report, do not bail out on failure"/>
<node TEXT="howto to place or name the test so that it is "/>
<node TEXT="refactor the tests">
<node TEXT="some are harmful for readability"/>
<node TEXT="name the tests"/>
<node TEXT="some are not useful"/>
<node TEXT="some pertinent tests are missing"/>
<node TEXT="some should doctest instead of unittest and vice versa"/>
<node TEXT="distinction should be made between testing the public api and the rest"/>
<node TEXT="have I used backdoors?"/>
<node TEXT="are interface tested?"/>
<node TEXT="am i white box or black box"/>
<node TEXT="how to put the simple session and the git howto in the test_wordish"/>
</node>
</node>
</node>
</map>
