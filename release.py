import re

from collections import namedtuple
Version = namedtuple('Version', 'major minor patch beta')

version_re=re.compile(r"""^
(?P<version>\d+\.\d+)         # minimum 'N.N'
(?P<extraversion>(?:\.\d+)*)  # any number of extra '.N' segments
(?:
    (?P<prerel>[abc]|rc)         # 'a' = alpha, 'b' = beta
                                 # 'c' or 'rc' = release candidate
    (?P<prerelversion>\d+(?:\.\d+)*)
)?
(?P<postdev>(\.post(?P<post>\d+))?(\.dev(?P<dev>\d+))?)?
$""", re.VERBOSE )

def parse_version():

    m=version_re.match(file("version").read().strip())
    if m:
        d=m.groupdict()
        ma, mi = d['version'].split('.')
        return Version( ma, mi, 
                        d['extraversion'].strip('.'),  
                        d.get('prerelversion'))

    else:
        raise Exception


def format(v):
    return '{0.major}.{0.minor}.{0.patch}{1}'.format( 
        v,'b'+v.beta if v.beta else '')


def bump(which):
    v=parse_version()
    setattr(v, which, str(int(getattr(v,which)) + 1))
    file('version','w').write(format(v))
    print file('version').read()


