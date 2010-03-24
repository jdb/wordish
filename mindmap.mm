
<map version="0.7.1">
<node TEXT="wordish">
<font NAME="SansSerif" SIZE="12"/>
<node TEXT="doc" POSITION="left">
<node TEXT="writing"/>
<node TEXT="testing">
<node TEXT="false"/>
<node TEXT="log file"/>
<node TEXT="clean up code"/>
<node TEXT="debug"/>
</node>
<node TEXT="roadmap"/>
<node TEXT="interfaces" FOLDED="true">
<node TEXT="overview simple run"/>
<node TEXT="two parsers"/>
<node TEXT="output and runner"/>
<node TEXT="reporter"/>
</node>
<node TEXT="making of" FOLDED="true">
<node TEXT="object modelisation"/>
<node TEXT="parser du text, des tokens nexts, iterator"/>
<node TEXT="executer des commandes dans un sous shell"/>
<node TEXT="packaging"/>
<node TEXT="testing"/>
<node TEXT="docutils"/>
<node TEXT="making it easy to use for other people than me"/>
<node TEXT="sphinx"/>
<node TEXT="debian package"/>
<node TEXT="documentation">
<node TEXT="partial literalincludes of the interfaces"/>
<node TEXT="readme is also partially include"/>
<node TEXT="readme, setup.py and sphinx doc share paragraphs"/>
<node TEXT="git commit rebuilds the docs, the readme, the setup.py"/>
<node TEXT="include .. in the beginning of the sys.path"/>
</node>
<node TEXT="release management"/>
<node TEXT="version management"/>
<node TEXT="git branch batch branch incursion to store the documentation"/>
<node TEXT="the dist directory should be the build interface">
<node TEXT="release use build as well as gitignore"/>
</node>
<node COLOR="#ff0000" TEXT="1. just use distribute to have eggs which have dependencies which will install docutils..."/>
<node TEXT="3. use the official documentation repository"/>
<node COLOR="#ff0000" TEXT="2. use distutils to generate console scripts"/>
<node TEXT="where can distutils install the manpages? rehash the db? the answer is no"/>
<node TEXT="can the scripts be installed in /usr/bin? only with debian packages"/>
<node TEXT="what should be the interface between the python sources and deb/rpm on the other side? the dist directory"/>
<node TEXT="where does distutils {package,} additional files go? don&apos;t use then unless the code require them"/>
</node>
<node TEXT="changelog"/>
<node TEXT="software engineering">
<node TEXT="git source, branches, virtualenv"/>
<node TEXT=" versions and interfaces"/>
<node TEXT="doctests and unit tests"/>
<node TEXT="source tarball"/>
<node TEXT="documentation"/>
<node TEXT="setup.py, packages/pypi.python.org"/>
<node TEXT="some organization with freemind"/>
</node>
</node>
<node TEXT="objects" FOLDED="true" POSITION="right">
<node TEXT="ISessionParser">
<node TEXT="universal linefeed for commands in win articles"/>
<node TEXT="list commands used and version"/>
<node TEXT="hints in a command&apos;s comments">
<node TEXT="ignore"/>
<node TEXT="input"/>
<node TEXT="&amp;2"/>
<node TEXT="returncode=3"/>
</node>
<node TEXT="let him figure out the cleanup code on its own with comment hints"/>
<node TEXT="get rid of get_command and get output,  make takewhile private"/>
<node TEXT="when docutils is not present, be able to use a raw log "/>
</node>
<node TEXT="IReporter" FOLDED="true">
<node COLOR="#ff0000" TEXT="explicit output manipulation outisde the reporter at bailout, show rest to help cleanup and help debug"/>
<node TEXT="differentiate the error and failure in the report, do not bail out on failure"/>
<node TEXT="when bailing out, all tests did not passed"/>
<node TEXT="I get regularly bitten by , 0 in the report"/>
<node TEXT="report knows less about command output"/>
</node>
<node TEXT="ICommandRunner" FOLDED="true">
<node TEXT="interactive via cmds.py or screen (tty?), confirm, insert command, ctrl-C ..."/>
<node TEXT="some command are not meant to be executed, others not identical, others not aborted"/>
<node TEXT="ignore from :argument:, comment"/>
</node>
<node TEXT="ICommandOutput" FOLDED="true">
<node TEXT="only one ellipsis per output, this is not enough"/>
<node TEXT="how does doctest do the ellipsis. Is it limited to one like us?"/>
</node>
<node TEXT="IBlockSelector">
<edge WIDTH="thin"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
<node TEXT="wordish module" FOLDED="true" POSITION="right">
<node TEXT="wordish --help"/>
<node TEXT="wordish --prompt &apos;&gt;&gt;&gt;&apos;"/>
<node TEXT="--match &apos;exact|ellipsis|regexp&apos;"/>
<node TEXT="give the option to attach a cleanup script"/>
</node>
<node TEXT="packaging python" POSITION="right">
<node TEXT="4. use the python 2to3 automation">
<node TEXT="setuptools2.4/2.5/3.1 required to use venv2.4/2.5/3.1"/>
</node>
</node>
<node TEXT="docutils" FOLDED="true" POSITION="right">
<node TEXT="directive source code">
<node TEXT="argument sh"/>
<node TEXT=" option test which can be false or cleanup"/>
<node TEXT="creates a node literal-block with a language sh"/>
</node>
<node TEXT="the sourcecode command should have the ignore all output command "/>
<node TEXT="la creation de la directive source prend le renvoie une queue sous la forme d&apos;une stringio, la directive source code &#xe9;crit dans cette stringio que le session parser consomme. &#xa;&#xa;Le doctree g&#xe9;n&#xe9;r&#xe9; est jet&#xe9;, on s&apos;en sert juste pour lancer la directive sourcecode, tout en effet de bord. (on evite peut etre aussi la latence au d&#xe9;marrage)&#xa;&#xa;Ca ne sert pas a grand chose d&apos;utiliser le session parser pour r&#xe9;inserer des noeuds command et output sous la forme de literal block dans la mesure ou il seront disjoint dans le doc final. Sauf si un r&#xe9;&#xe8;l builder html/latex impl&#xe9;mnte un IReporter"/>
</node>
<node TEXT="interfaces" FOLDED="true" POSITION="right">
<node TEXT="context manager"/>
<node TEXT="iterable"/>
<node TEXT="member attribute is a list, a string, a dictionnary (docstring is less readable when building an overview), maybe epydoc is the way, or autointerface"/>
</node>
<node TEXT="packaging debian" POSITION="right">
<node TEXT="man pages"/>
<node TEXT="python and cddb"/>
<node TEXT="doc"/>
<node TEXT="python module"/>
<node TEXT="script"/>
<node TEXT="sphinx extension"/>
<node TEXT="build depends on sphinx"/>
</node>
<node TEXT="tests" FOLDED="true" POSITION="right">
<node TEXT="some impede readability"/>
<node TEXT="some may be redundant"/>
<node TEXT="some pertinent tests are missing"/>
<node TEXT="some doctest would better be unit test and vice versa"/>
<node TEXT="clear distinction between public (black box) and private api (white box) (test the public at least)"/>
<node TEXT="some use backdoors"/>
<node TEXT="functional_tests should be launched as root and be run on every file in example"/>
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
<node TEXT="sphinx" FOLDED="true" POSITION="right">
<node TEXT="sphinx integration, how to to reuse sourcecode"/>
<node TEXT="extension wich cat sourcecode blocks"/>
<node TEXT="in the wodish sources but another python module called sphinx.ext.wordish"/>
<node TEXT="rst builder, sphinx builder"/>
<node TEXT="quiet mode without output only summary"/>
<node TEXT="other parsing format, markdown"/>
<node TEXT="for each snippet the tokens should no be in command anymore"/>
<node TEXT="completely on top of wordish, use the isession parser, the icommnad runner and reimplemente the ireporter for a directive test-report"/>
<node COLOR="#338800" TEXT="ask sphinx howto extend sourcecode to include :options: such as no_run, no_check, can_abort">
<font NAME="Dialog" SIZE="12"/>
</node>
<node TEXT="extend sourcecode directive and propose a patch"/>
<node TEXT="INodeSelector( node ) -&gt; true | false"/>
<node TEXT="config" FOLDED="true">
<node TEXT="bailout_on_abort"/>
<node TEXT="match=string,re,ellipsis"/>
<node TEXT="prompts"/>
<node TEXT="ignore_stderr"/>
</node>
<node TEXT="need a node selector for article, clenaupm sourcecode"/>
<node TEXT="# Un node match pour la directive article &#xa;# un node match pour la directive cleanup &#xa;# un node match pour la directive sourcecode  &#xa;# essence = [ n  &#xa;#             for n in doctree.traverse()  &#xa;#             if is_article(n) or is_cleanup(n) or is_shell(n) ]  &#xa;# snippets = [ split(a, is_cleanup ) for a in split( essence, is_article ) ]"/>
<node TEXT="need a directive .. test_report::"/>
<node TEXT="need a directive wordish with an argument telling the name of the article, and with an option to configure the list of prompts"/>
<node TEXT="the sphinx builder can generate scripts with a cleanup section"/>
</node>
<node TEXT="a bug in python?" FOLDED="true" POSITION="right">
<node TEXT="cd doc"/>
<node TEXT="python"/>
<node TEXT="import sys"/>
<node TEXT="import test_wordish -&gt; except"/>
<node TEXT="sys.path.append(&apos;..&apos;)"/>
<node TEXT="import test_wordish"/>
<node TEXT="can&apos;t import TestMachin (why, and why this one)"/>
</node>
</node>
</map>
