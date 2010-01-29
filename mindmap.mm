<map version="0.7.1">
<node TEXT="wordish">
<node TEXT="What is wordish?" FOLDED="true" POSITION="right">
<node TEXT="readme"/>
<node TEXT="man"/>
<node TEXT="wordish --help"/>
<node TEXT="presentation"/>
<node TEXT="installation and verification"/>
</node>
<node TEXT="writing articles" FOLDED="true" POSITION="right">
<node TEXT="parsing method (prompts, nesting)"/>
<node TEXT="matching methods (ignoring, ellipsis, re)"/>
<node TEXT="one subshell for the session"/>
<node TEXT="working examples: raid, lvm, deb, git, ssh, ipvsadm"/>
</node>
<node TEXT="object model and interfaces" POSITION="right">
<node TEXT="overview">
<node TEXT="one of the attribute is an iterable"/>
<node TEXT="a class is iterable" FOLDED="true">
<node TEXT="fact is that there is an __iter__() yielding an iterator which has a next() function. &#xa;&#xa;Should just say this object has an __iter__ (which is a idiom) or should I say it has a next (which is more directly useful, and less a idiom)&#xa;&#xa;The bottom line is trying to express, this interface provides an iterable"/>
</node>
<node TEXT="a class is callable"/>
<node TEXT="a class is a context manager"/>
<node TEXT="complete arguments and return code?"/>
</node>
<node TEXT="should the interface contains the doctest?"/>
<node TEXT="should it contain message sequence diagram?"/>
<node TEXT="for simplicity should the private/public distinction be made clear in the module with underscore"/>
<node TEXT="should a sphinx doc be build cuz it is classe, there is a toc, etc"/>
<node TEXT="should the sphinx doc syntax or the pydoctor be used? are they way clearer?"/>
<node TEXT="dig out, undust and finish the zope.schema extensions"/>
<node TEXT="the sphinx automodule will not be displayed by github and pypi, kiss would advise not to use sphinx, or else, the page is build in a branch and is an article on jdb.github.com ..."/>
</node>
<node TEXT="software engineering" FOLDED="true" POSITION="right">
<node TEXT="source, branches and versions">
<node TEXT="mention in the doc that working on the setup.py is eased by a virtualenv"/>
</node>
<node TEXT="doctests and unit tests"/>
<node TEXT="packaging">
<node TEXT="questions">
<node TEXT="does distutils make eggs? it is talking about eggs anyway">
<node TEXT="setup --help-commands tell nothin about eggs"/>
<node TEXT="distutils.core.setup install from pristine source says &apos;running egg_info&apos;"/>
</node>
<node TEXT="is there a way to distribute man pages with distutils" FOLDED="true">
<node TEXT="console script entry point requires eggs"/>
</node>
<node TEXT="where does distutils {package,} additional files go?"/>
<node TEXT="additional vs package data in distutils? another solution in eggs? in buildout?" FOLDED="true">
<node TEXT="scripts are placed at install in ./bin in a virtual env"/>
</node>
<node TEXT="MANIFEST?"/>
<node TEXT="examples, "/>
</node>
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
<node TEXT="console_script entry point: later needs eggs, eggs can&apos;t do man"/>
<node TEXT="rst builder, sphinx builder"/>
<node TEXT="quiet mode without output"/>
<node TEXT="turn to unix linefeed when parsing other linefeeds"/>
<node TEXT="list commands used and version"/>
<node TEXT="at bailout, show rest to help cleanup and help debug"/>
<node TEXT="interactive via cmds.py or screen (tty?), confirm, insert command, ctrl-C ..."/>
<node TEXT="executable article with #!/usr/bin/wordish"/>
<node TEXT="other parsing format, markdown"/>
<node TEXT="hints in a command&apos;s comments">
<node TEXT="ignore (stdout, stderr, ret)"/>
<node TEXT="input"/>
<node TEXT="the rest is clean up code executed on bailout"/>
<node TEXT="&amp;2"/>
</node>
<node TEXT="differentiate the error and failure in the report, do not bail out on failure"/>
<node TEXT="&quot;something broke&quot; be clearer less fear monging"/>
<node TEXT="the command runner should accept the url of an ssh host"/>
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
