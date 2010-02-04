<map version="0.7.1">
<node TEXT="wordish">
<node TEXT="What is wordish? installation verification" POSITION="right"/>
<node TEXT="writing and testing articles" POSITION="right">
<node TEXT="parsing method (prompts, nesting)"/>
<node TEXT="matching methods (ignoring, ellipsis, re)"/>
<node TEXT="one subshell for the session"/>
<node TEXT="working examples: raid, lvm, deb, git, ssh, ipvsadm"/>
<node TEXT="false"/>
<node TEXT="log"/>
<node TEXT="clean up code"/>
<node TEXT="sphinx integration, how to to reuse sourcecode"/>
</node>
<node TEXT="interfaces and object model" FOLDED="true" POSITION="right">
<node TEXT="overview simple run"/>
<node TEXT="two parsers"/>
<node TEXT="output and runner"/>
<node TEXT="reporter"/>
</node>
<node TEXT="the Python sources" FOLDED="true" POSITION="right">
<node TEXT="overview simple run"/>
<node TEXT="two parsers"/>
<node TEXT="output and runner"/>
<node TEXT="reporter"/>
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
<node TEXT="include the readme in the long description"/>
<node TEXT="which license"/>
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
<node TEXT="making of" FOLDED="true" POSITION="right">
<node TEXT="modelisation"/>
<node TEXT="parser du text, des tokens nexts"/>
<node TEXT="executer des commandes"/>
<node TEXT="packaging"/>
<node TEXT="testing"/>
<node TEXT="sphinx/rst extensions"/>
<node TEXT="making it easy to use for other people than me"/>
<node TEXT="correcting the most annoying bugs"/>
</node>
<node TEXT="limitations, roadmap and crazy ideas" FOLDED="true" POSITION="right">
<node TEXT="setup.py and entry point"/>
<node TEXT="rst builder, sphinx builder"/>
<node TEXT="quiet mode without output only summary"/>
<node TEXT="universal linefeed for commands in win articles"/>
<node TEXT="list commands used and version"/>
<node TEXT="at bailout, show rest to help cleanup and help debug"/>
<node TEXT="interactive via cmds.py or screen (tty?), confirm, insert command, ctrl-C ..."/>
<node TEXT="executable article with #!/usr/bin/wordish"/>
<node TEXT="other parsing format, markdown"/>
<node TEXT="hints in a command&apos;s comments">
<node TEXT="ignore"/>
<node TEXT="input"/>
<node TEXT="&amp;2"/>
<node TEXT="returncode=3"/>
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
<node TEXT="man"/>
<node TEXT="wordish --help"/>
<node TEXT="give the option to attach a cleanup script"/>
<node TEXT="let him figure out the cleanup code on its own with comment hints"/>
<node TEXT="when bailing out, all tests did not passed"/>
<node TEXT="only one ellipsis per output, this is not enough"/>
<node TEXT="the sourcecode command should have the ignore all output command "/>
<node TEXT="for each snippet the tokens should no be in command anymore"/>
<node TEXT="lancer bash en mode interactif sinon les accolade sont mal interpretes or tty"/>
</node>
<node TEXT="bugs" POSITION="right">
<node TEXT="problem with the way comments in functions are parsed, bad linefeed"/>
<node TEXT="I get regularly bitten by , 0"/>
<node TEXT="really sometimes you just want to execute stuff and not care about the output"/>
<node TEXT="really sometimes just check aborted is enough"/>
<node TEXT="ignore from :argument:, comment"/>
</node>
<node TEXT="integration with sphinx" POSITION="left">
<node TEXT="overloading source code to add the snippet to "/>
</node>
<node TEXT="extension wich cat sourcecode blocks" POSITION="left"/>
<node TEXT="in the wodish sources but another python module called sphinx.ext.wordish" POSITION="left"/>
<node TEXT="config" FOLDED="true" POSITION="left">
<node TEXT="bailout_on_abort"/>
<node TEXT="match=string,re,ellipsis"/>
<node TEXT="prompts"/>
<node TEXT="ignore_stderr"/>
</node>
<node TEXT="directive source code" POSITION="left">
<node TEXT="argument sh"/>
<node TEXT="no options"/>
<node TEXT="creates a node "/>
</node>
<node TEXT="pr plan" POSITION="left">
<node TEXT="shunit"/>
<node TEXT="lo lange"/>
<node TEXT="ubuntu"/>
<node TEXT="sphinx"/>
<node TEXT="docutils"/>
<node TEXT="lvs"/>
<node TEXT="guy from redhat"/>
<node TEXT="debian administration"/>
<node TEXT="python planet"/>
<node TEXT="debian planet"/>
<node TEXT="debian ml"/>
<node TEXT="anevia"/>
<node TEXT="roming"/>
<node TEXT="imil"/>
</node>
</node>
</map>
