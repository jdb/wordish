<map version="0.7.1">
<node TEXT="wordish">
<font NAME="SansSerif" SIZE="12"/>
<node TEXT="doc" POSITION="left">
<node TEXT="What is wordish? installation verification"/>
<node TEXT="writing and testing articles" FOLDED="true">
<node TEXT="parsing method (prompts, nesting)"/>
<node TEXT="matching methods (ignoring, ellipsis, re)"/>
<node TEXT="one subshell for the session"/>
<node TEXT="working examples: raid, lvm, deb, git, ssh, ipvsadm"/>
<node TEXT="debug" FOLDED="true">
<node TEXT="false"/>
<node TEXT="log file"/>
<node TEXT="clean up code"/>
</node>
</node>
<node TEXT="roadmap" FOLDED="true">
<node TEXT="get a blessing from the sphinx project"/>
</node>
<node TEXT="interfaces and object model" FOLDED="true">
<node TEXT="overview simple run"/>
<node TEXT="two parsers"/>
<node TEXT="output and runner"/>
<node TEXT="reporter"/>
</node>
<node TEXT="Python sources" FOLDED="true">
<node TEXT="overview simple run"/>
<node TEXT="two parsers"/>
<node TEXT="output and runner"/>
<node TEXT="reporter"/>
</node>
<node TEXT="software engineering" FOLDED="true">
<node TEXT="github, source, branches and versions"/>
<node TEXT="doctests and unit tests"/>
<node TEXT="packaging" FOLDED="true">
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
<node TEXT="some organization with freemind"/>
</node>
<node TEXT="documentation" FOLDED="true">
<node TEXT="partial literalincludes of the interfaces"/>
<node TEXT="readme is also partially include"/>
<node TEXT="readme, setup.py and sphinx doc share paragraphs"/>
<node TEXT="git commit rebuilds the docs, the readme, the setup.py"/>
</node>
<node TEXT="making of" FOLDED="true">
<node TEXT="modelisation"/>
<node TEXT="parser du text, des tokens nexts"/>
<node TEXT="executer des commandes"/>
<node TEXT="packaging"/>
<node TEXT="testing"/>
<node TEXT="sphinx/rst extensions"/>
<node TEXT="making it easy to use for other people than me"/>
<node TEXT="correcting the most annoying bugs"/>
</node>
</node>
<node TEXT="bugs" FOLDED="true" POSITION="right">
<node TEXT="linefeed consumed after a comment when nested, should be left as is"/>
<node TEXT="I get regularly bitten by , 0 in the report"/>
</node>
<node TEXT="git" FOLDED="true" POSITION="right">
<node TEXT="mention in the doc that working on the setup.py is eased by a virtualenv"/>
<node TEXT="gitignore"/>
<node TEXT="git pre-commit relaunch the tests, rebuild the package, the manpage"/>
</node>
<node TEXT="objects" FOLDED="true" POSITION="right">
<node TEXT="ISessionParser" FOLDED="true">
<node TEXT="universal linefeed for commands in win articles"/>
<node TEXT="list commands used and version"/>
<node TEXT="hints in a command&apos;s comments">
<node TEXT="ignore"/>
<node TEXT="input"/>
<node TEXT="&amp;2"/>
<node TEXT="returncode=3"/>
</node>
<node TEXT="let him figure out the cleanup code on its own with comment hints"/>
</node>
<node TEXT="IReporter" FOLDED="true">
<node TEXT="at bailout, show rest to help cleanup and help debug"/>
<node TEXT="differentiate the error and failure in the report, do not bail out on failure"/>
<node TEXT="when bailing out, all tests did not passed"/>
</node>
<node TEXT="ICommandRunner" FOLDED="true">
<node TEXT="interactive via cmds.py or screen (tty?), confirm, insert command, ctrl-C ..."/>
<node TEXT="lancer bash en mode interactif sinon les accolade sont mal interpretes or tty"/>
<node TEXT="really sometimes you just want to execute stuff and not care about the output"/>
<node TEXT="really sometimes just check aborted is enough"/>
<node TEXT="ignore from :argument:, comment"/>
</node>
<node TEXT="ICommandOutput" FOLDED="true">
<node TEXT="only one ellipsis per output, this is not enough"/>
</node>
<node TEXT="IDocutilsNodeMatch"/>
</node>
<node TEXT="wordish module" FOLDED="true" POSITION="right">
<node TEXT="#!/usr/bin/env wordish"/>
</node>
<node TEXT="packaging python" FOLDED="true" POSITION="right">
<node TEXT="does distutils make eggs?">
<node TEXT="setup --help-commands tell nothin about eggs"/>
<node TEXT="distutils.core.setup install from pristine source says &apos;running egg_info&apos;"/>
</node>
<node TEXT="distribute offers eggs which I am not sure I need, but haz console scripts"/>
<node TEXT="does distutils install manpages? and rehash the mandb"/>
<node TEXT="can the scripts be installed in /usr/bin"/>
<node TEXT="what should be the interface between the python sources and deb/rpm on the other side"/>
<node TEXT="where does distutils {package,} additional files go?"/>
<node TEXT="additional vs package data in distutils? another solution in eggs? in buildout? MANIFEST?"/>
<node TEXT="wordish --help"/>
<node TEXT="give the option to attach a cleanup script"/>
</node>
<node TEXT="docutils" FOLDED="true" POSITION="right">
<node TEXT="directive source code">
<node TEXT="argument sh"/>
<node TEXT="no options"/>
<node TEXT="creates a node literal-block with a language sh"/>
</node>
<node TEXT="the sourcecode command should have the ignore all output command "/>
</node>
<node TEXT="sphinx" FOLDED="true" POSITION="right">
<node TEXT="overloading source code to add the snippet to "/>
<node TEXT="sphinx integration, how to to reuse sourcecode"/>
<node TEXT="extension wich cat sourcecode blocks"/>
<node TEXT="in the wodish sources but another python module called sphinx.ext.wordish"/>
<node TEXT="rst builder, sphinx builder"/>
<node TEXT="quiet mode without output only summary"/>
<node TEXT="other parsing format, markdown"/>
<node TEXT="for each snippet the tokens should no be in command anymore"/>
<node TEXT="la directive source code appele le session parser et inserer des noeuds dans le doctree, le report pourrait etre dans le doctree, en latex ou html"/>
</node>
<node TEXT="config" FOLDED="true" POSITION="right">
<node TEXT="bailout_on_abort"/>
<node TEXT="match=string,re,ellipsis"/>
<node TEXT="prompts"/>
<node TEXT="ignore_stderr"/>
</node>
<node TEXT="interfaces" FOLDED="true" POSITION="right">
<node TEXT="context manager"/>
<node TEXT="iterable"/>
<node TEXT="member attribute is a list, a string, a dictionnary (docstring is less readable when building an overview), maybe epydoc is the way, or autointerface"/>
</node>
<node TEXT="packaging debian" FOLDED="true" POSITION="right">
<node TEXT="standalones scripts"/>
<node TEXT="man pages"/>
<node TEXT="doc"/>
<node TEXT="python module"/>
<node TEXT="sphinx extension"/>
<node TEXT="article examples"/>
<node TEXT="interfaces"/>
<node TEXT="article examples found by the module"/>
</node>
<node TEXT="tests" FOLDED="true" POSITION="right">
<node TEXT="howto to place or name the test so that it is "/>
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
<node TEXT="pr plan" FOLDED="true" POSITION="right">
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
