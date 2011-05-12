<map version="0.9.0">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1276868083511" ID="ID_1093128797" MODIFIED="1276868083511" TEXT="wordish">
<font NAME="SansSerif" SIZE="12"/>
<node CREATED="1276868083511" ID="ID_1538119186" MODIFIED="1276868083511" POSITION="left" TEXT="doc">
<node CREATED="1276868083511" FOLDED="true" MODIFIED="1276868083511" TEXT="writing">
<node CREATED="1276868083511" MODIFIED="1276868083511" TEXT="working examples: raid, lvm, deb, git, ssh, ipvsadm"/>
</node>
<node CREATED="1276868083512" FOLDED="true" ID="ID_766317851" MODIFIED="1298237490227" TEXT="testing">
<node CREATED="1276868083512" MODIFIED="1276868083512" TEXT="false"/>
<node CREATED="1276868083512" MODIFIED="1276868083512" TEXT="log file"/>
<node CREATED="1276868083512" MODIFIED="1276868083512" TEXT="clean up code"/>
<node CREATED="1276868083512" MODIFIED="1276868083512" TEXT="debug"/>
<node CREATED="1276868083512" FOLDED="true" MODIFIED="1276868083512" TEXT="software engineering">
<node CREATED="1276868083512" MODIFIED="1276868083512" TEXT="github, source, branches and versions"/>
<node CREATED="1276868083512" MODIFIED="1276868083512" TEXT="doctests and unit tests"/>
<node CREATED="1276868083512" FOLDED="true" MODIFIED="1276868083512" TEXT="packaging">
<node CREATED="1276868083512" MODIFIED="1276868083512" TEXT="test package_data and data_files, where do they end up?"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="distutils, distribute, pip"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="include the readme in the long description"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="which license"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="content">
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="one module"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="one test file"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="man page, README.rst"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="setup.py"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="four examples"/>
<node CREATED="1276868083513" MODIFIED="1276868083513" TEXT="MANIFEST"/>
<node CREATED="1276868083514" MODIFIED="1276868083514" TEXT="build"/>
<node CREATED="1276868083514" MODIFIED="1276868083514" TEXT="sdist"/>
</node>
</node>
<node CREATED="1276868083514" MODIFIED="1276868083514" TEXT="some organization with freemind"/>
<node CREATED="1276868083514" MODIFIED="1276868083514" TEXT="mention in the doc that working on the setup.py is eased by a virtualenv"/>
</node>
</node>
<node CREATED="1276868083514" FOLDED="true" ID="ID_856530675" MODIFIED="1298237492269" TEXT="roadmap">
<node CREATED="1276868083514" ID="ID_412239221" MODIFIED="1276868083514" TEXT="get a blessing from the sphinx project"/>
</node>
<node CREATED="1276868083514" FOLDED="true" ID="ID_120988705" MODIFIED="1276868083514" TEXT="interfaces">
<node CREATED="1276868083514" MODIFIED="1276868083514" TEXT="overview simple run"/>
<node CREATED="1276868083514" MODIFIED="1276868083514" TEXT="two parsers"/>
<node CREATED="1276868083515" MODIFIED="1276868083515" TEXT="output and runner"/>
<node CREATED="1276868083515" MODIFIED="1276868083515" TEXT="reporter"/>
</node>
<node CREATED="1276868083515" FOLDED="true" ID="ID_1319536219" MODIFIED="1276868083515" TEXT="making of">
<node CREATED="1276868083515" MODIFIED="1276868083515" TEXT="object modelisation"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="parser du text, des tokens nexts, iterator"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="executer des commandes dans un sous shell"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="packaging"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="testing"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="docutils"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="making it easy to use for other people than me"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="sphinx"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="debian package"/>
<node CREATED="1276868083518" MODIFIED="1276868083518" TEXT="documentation">
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="partial literalincludes of the interfaces"/>
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="readme is also partially include"/>
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="readme, setup.py and sphinx doc share paragraphs"/>
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="git commit rebuilds the docs, the readme, the setup.py"/>
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="include .. in the beginning of the sys.path"/>
</node>
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="release management"/>
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="version management"/>
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="git branch batch branch incursion to store the documentation"/>
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="the dist directory should be the build interface">
<node CREATED="1276868083519" MODIFIED="1276868083519" TEXT="release use build as well as gitignore"/>
</node>
</node>
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="changelog"/>
</node>
<node CREATED="1276868083520" FOLDED="true" ID="ID_519584447" MODIFIED="1276868083520" POSITION="right" TEXT="objects">
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="ISessionParser">
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="universal linefeed for commands in win articles"/>
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="list commands used and version"/>
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="hints in a command&apos;s comments">
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="ignore"/>
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="input"/>
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="&amp;2"/>
<node CREATED="1276868083520" MODIFIED="1276868083520" TEXT="returncode=3"/>
</node>
<node CREATED="1276868083521" MODIFIED="1276868083521" TEXT="let him figure out the cleanup code on its own with comment hints"/>
<node CREATED="1276868083521" MODIFIED="1276868083521" TEXT="get rid of get_command and get output,  make takewhile private"/>
<node CREATED="1276868083521" MODIFIED="1276868083521" TEXT="when docutils is not present, be able to use a raw log "/>
</node>
<node CREATED="1276868083521" FOLDED="true" MODIFIED="1276868083521" TEXT="IReporter">
<node COLOR="#ff0000" CREATED="1276868083521" MODIFIED="1276868083521" TEXT="explicit output manipulation outisde the reporter at bailout, show rest to help cleanup and help debug"/>
<node CREATED="1276868083521" MODIFIED="1276868083521" TEXT="differentiate the error and failure in the report, do not bail out on failure"/>
<node CREATED="1276868083521" MODIFIED="1276868083521" TEXT="when bailing out, all tests did not passed"/>
<node CREATED="1276868083521" MODIFIED="1276868083521" TEXT="I get regularly bitten by , 0 in the report"/>
<node CREATED="1276868083521" MODIFIED="1276868083521" TEXT="report knows less about command output"/>
</node>
<node CREATED="1276868083522" FOLDED="true" MODIFIED="1276868083522" TEXT="ICommandRunner">
<node CREATED="1276868083522" MODIFIED="1276868083522" TEXT="interactive via cmds.py or screen (tty?), confirm, insert command, ctrl-C ..."/>
<node CREATED="1276868083522" MODIFIED="1276868083522" TEXT="some command are not meant to be executed, others not identical, others not aborted"/>
<node CREATED="1276868083522" MODIFIED="1276868083522" TEXT="ignore from :argument:, comment"/>
</node>
<node CREATED="1276868083522" FOLDED="true" MODIFIED="1276868083522" TEXT="ICommandOutput">
<node CREATED="1276868083522" MODIFIED="1276868083522" TEXT="only one ellipsis per output, this is not enough"/>
<node CREATED="1276868083522" MODIFIED="1276868083522" TEXT="how does doctest do the ellipsis. Is it limited to one like us?"/>
</node>
<node CREATED="1276868083522" MODIFIED="1276868083522" TEXT="IBlockSelector">
<edge WIDTH="thin"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
<node CREATED="1276868083523" ID="ID_590619470" MODIFIED="1298237494811" POSITION="right" TEXT="wordish module">
<node CREATED="1276868083523" ID="ID_434690225" MODIFIED="1276868083523" TEXT="wordish --help"/>
<node CREATED="1276868083523" ID="ID_1730301649" MODIFIED="1276868083523" TEXT="wordish --prompt &apos;&gt;&gt;&gt;&apos;"/>
<node CREATED="1276868083523" ID="ID_285620273" MODIFIED="1276868083523" TEXT="--match &apos;exact|ellipsis|regexp&apos;"/>
<node CREATED="1276868083523" ID="ID_490439587" MODIFIED="1276868083523" TEXT="give the option to attach a cleanup script"/>
<node CREATED="1298238931250" ID="ID_1465520753" MODIFIED="1298238941950" TEXT="integrate to unittest"/>
<node CREATED="1298238942930" ID="ID_1302675057" MODIFIED="1298238976974" TEXT="run the tests to help build the tests"/>
<node CREATED="1298240620636" ID="ID_44188351" MODIFIED="1298240629958" TEXT="python -m too verbose"/>
</node>
<node CREATED="1276868083523" ID="ID_241640184" MODIFIED="1276868083523" POSITION="right" TEXT="packaging python">
<node COLOR="#ff0000" CREATED="1276868083523" ID="ID_483781" MODIFIED="1276868083523" TEXT="1. just use distribute to have eggs which have dependencies which will install docutils..."/>
<node COLOR="#ff0000" CREATED="1276868083523" ID="ID_1123262926" MODIFIED="1276868083523" TEXT="2. use distutils to generate console scripts"/>
<node CREATED="1276868083523" ID="ID_642831640" MODIFIED="1276868083523" TEXT="3. use the official documentation repository"/>
<node CREATED="1276868083524" ID="ID_228292561" MODIFIED="1276868083524" TEXT="4. use the python 2to3 automation"/>
<node CREATED="1276868083524" ID="ID_1904025909" MODIFIED="1276868083524" TEXT="where can distutils install the manpages? rehash the db? the answer is no"/>
<node CREATED="1276868083524" ID="ID_1181981802" MODIFIED="1276868083524" TEXT="can the scripts be installed in /usr/bin? only with debian packages"/>
<node CREATED="1276868083524" ID="ID_2279338" MODIFIED="1276868083524" TEXT="what should be the interface between the python sources and deb/rpm on the other side? the dist directory"/>
<node CREATED="1276868083524" ID="ID_512520794" MODIFIED="1276868083524" TEXT="where does distutils {package,} additional files go? don&apos;t use then unless the code require them"/>
<node CREATED="1276868683002" ID="ID_1769487369" MODIFIED="1276871694356" TEXT="virer la doc de github, et ne laisser que le readme, simplifier le release pour ne pas changer de branch"/>
</node>
<node CREATED="1276868083524" FOLDED="true" ID="ID_274953561" MODIFIED="1276868083524" POSITION="right" TEXT="docutils">
<node CREATED="1276868083524" MODIFIED="1276868083524" TEXT="directive source code">
<node CREATED="1276868083524" MODIFIED="1276868083524" TEXT="argument sh"/>
<node CREATED="1276868083524" MODIFIED="1276868083524" TEXT=" option test which can be false or cleanup"/>
<node CREATED="1276868083524" MODIFIED="1276868083524" TEXT="creates a node literal-block with a language sh"/>
</node>
<node CREATED="1276868083525" MODIFIED="1276868083525" TEXT="the sourcecode command should have the ignore all output command "/>
<node CREATED="1276868083525" MODIFIED="1276868083525" TEXT="la creation de la directive source prend le renvoie une queue sous la forme d&apos;une stringio, la directive source code &#xe9;crit dans cette stringio que le session parser consomme. &#xa;&#xa;Le doctree g&#xe9;n&#xe9;r&#xe9; est jet&#xe9;, on s&apos;en sert juste pour lancer la directive sourcecode, tout en effet de bord. (on evite peut etre aussi la latence au d&#xe9;marrage)&#xa;&#xa;Ca ne sert pas a grand chose d&apos;utiliser le session parser pour r&#xe9;inserer des noeuds command et output sous la forme de literal block dans la mesure ou il seront disjoint dans le doc final. Sauf si un r&#xe9;&#xe8;l builder html/latex impl&#xe9;mnte un IReporter"/>
</node>
<node CREATED="1276868083525" ID="ID_623325466" MODIFIED="1298237538698" POSITION="right" TEXT="interfaces">
<node CREATED="1276868083525" ID="ID_847096959" MODIFIED="1276868083525" TEXT="context manager"/>
<node CREATED="1276868083525" ID="ID_1499088194" MODIFIED="1276868083525" TEXT="iterable"/>
<node CREATED="1276868083525" ID="ID_1182696320" MODIFIED="1276868083525" TEXT="member attribute is a list, a string, a dictionnary (docstring is less readable when building an overview), maybe epydoc is the way, or autointerface"/>
</node>
<node CREATED="1276868083525" ID="ID_1898318518" MODIFIED="1276868083525" POSITION="right" TEXT="packaging debian">
<node CREATED="1276868083526" MODIFIED="1276868083526" TEXT="standalones shell scripts generated by console_scripts"/>
<node CREATED="1276868083526" MODIFIED="1276868083526" TEXT="man pages"/>
<node CREATED="1276868083526" MODIFIED="1276868083526" TEXT="doc"/>
<node CREATED="1276868083526" MODIFIED="1276868083526" TEXT="python module"/>
<node CREATED="1276868083526" MODIFIED="1276868083526" TEXT="sphinx extension"/>
<node CREATED="1276868083526" MODIFIED="1276868083526" TEXT="article examples"/>
<node CREATED="1276868083526" MODIFIED="1276868083526" TEXT="interfaces"/>
<node CREATED="1276868083526" MODIFIED="1276868083526" TEXT="article examples found by the module"/>
<node CREATED="1276868083526" ID="ID_233041482" MODIFIED="1276868083526" TEXT="build dependency, sphinx"/>
</node>
<node CREATED="1276868083526" ID="ID_1288519177" MODIFIED="1298237525070" POSITION="right" TEXT="tests">
<node CREATED="1276868083526" ID="ID_687569743" MODIFIED="1276868083526" TEXT="some impede readability"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="some may be redundant"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="some pertinent tests are missing"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="some doctest would better be unit test and vice versa"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="clear distinction between public (black box) and private api (white box) (test the public at least)"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="some use backdoors"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="functional_tests should be launched as root and be run on every file in example"/>
</node>
<node CREATED="1276868083527" FOLDED="true" MODIFIED="1276868083527" POSITION="right" TEXT="pr plan">
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="shunit"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="lo lange"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="ubuntu"/>
<node CREATED="1276868083527" MODIFIED="1276868083527" TEXT="sphinx"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="docutils"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="lvs"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="guy from redhat"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="debian administration"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="python planet"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="debian planet"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="debian ml"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="anevia"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="roming"/>
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="imil"/>
</node>
<node CREATED="1276868083528" FOLDED="true" MODIFIED="1276868083528" POSITION="right" TEXT="sphinx">
<node CREATED="1276868083528" MODIFIED="1276868083528" TEXT="sphinx integration, how to to reuse sourcecode"/>
<node CREATED="1276868083529" MODIFIED="1276868083529" TEXT="extension wich cat sourcecode blocks"/>
<node CREATED="1276868083529" MODIFIED="1276868083529" TEXT="in the wodish sources but another python module called sphinx.ext.wordish"/>
<node CREATED="1276868083529" MODIFIED="1276868083529" TEXT="rst builder, sphinx builder"/>
<node CREATED="1276868083529" MODIFIED="1276868083529" TEXT="quiet mode without output only summary"/>
<node CREATED="1276868083529" MODIFIED="1276868083529" TEXT="other parsing format, markdown"/>
<node CREATED="1276868083529" MODIFIED="1276868083529" TEXT="for each snippet the tokens should no be in command anymore"/>
<node CREATED="1276868083529" MODIFIED="1276868083529" TEXT="completely on top of wordish, use the isession parser, the icommnad runner and reimplemente the ireporter for a directive test-report"/>
<node COLOR="#338800" CREATED="1276868083529" MODIFIED="1276868083529" TEXT="ask sphinx howto extend sourcecode to include :options: such as no_run, no_check, can_abort">
<font NAME="Dialog" SIZE="12"/>
</node>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="extend sourcecode directive and propose a patch"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="INodeSelector( node ) -&gt; true | false"/>
<node CREATED="1276868083530" FOLDED="true" MODIFIED="1276868083530" TEXT="config">
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="bailout_on_abort"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="match=string,re,ellipsis"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="prompts"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="ignore_stderr"/>
</node>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="need a node selector for article, clenaupm sourcecode"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="# Un node match pour la directive article &#xa;# un node match pour la directive cleanup &#xa;# un node match pour la directive sourcecode  &#xa;# essence = [ n  &#xa;#             for n in doctree.traverse()  &#xa;#             if is_article(n) or is_cleanup(n) or is_shell(n) ]  &#xa;# snippets = [ split(a, is_cleanup ) for a in split( essence, is_article ) ]"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="need a directive .. test_report::"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="need a directive wordish with an argument telling the name of the article, and with an option to configure the list of prompts"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="the sphinx builder can generate scripts with a cleanup section"/>
</node>
<node CREATED="1276868083530" FOLDED="true" MODIFIED="1276868083530" POSITION="right" TEXT="a bug in python?">
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="cd doc"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="python"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="import sys"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="import test_wordish -&gt; except"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="sys.path.append(&apos;..&apos;)"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="import test_wordish"/>
<node CREATED="1276868083530" MODIFIED="1276868083530" TEXT="can&apos;t import TestMachin (why, and why this one)"/>
</node>
</node>
</map>
