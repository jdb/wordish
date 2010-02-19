die () { echo "$1" >&2 ; exit 1 ;  }


build_doc () {

    # here be fragons
    set -e -x

    current_branch=`git branch | awk '/\*/ {print $2}'`
    version=`cat version`

    # switch to the doc repository, then checkout the doc sources
    git checkout gh-pages 
    git branch | grep -q '* gh-pages'  || return 1
    git checkout $current_branch doc wordish.py interfaces.py version

    # build the doc
    ( cd doc ; sphinx-build  . .. )

    # adapt the sphinx layout to the github conventions
    rm -rf static sources images 
    mv {_,}sources
    mv {_,}static  
    mv {_,}images || true
    find . -name '*.html' -o -name '*.js' | \
	xargs sed -i 's/_static/static/g;s/_sources/sources/g;s/_images/images/g' 

    # suppress the sources
    git rm -r doc wordish.py interfaces.py version -f
    rm -rf *.pyc .buildinfo .doctrees/

    # add potential new html file (no new file most of the time)
    # git add * || true

    # commit the doc, push to github, back the current branch
    # git commit -a -m "Updated the doc to version $version"
    # git push origin gh-pages
    git checkout  $current_branch
    git branch | grep -q "* $current_branch"  || return 1
    rm -rf *.html  sources/ static/ searchindex.js objects.inv
}

###################
### functions dealing with the version

parse_version () {

    unset major minor patch beta
    
    remaining=`cat version`
    major=${remaining%%.*}

    remaining=${remaining#*.}
    minor=${remaining%%.*}

    remaining=${remaining#*.}

    if [ `expr index b $remaining` -ne 0 ] ; then
	patch=${remaining%%b*}
	beta=${remaining##*b}
    else
	patch=$remaining
    fi 
}

pre_minor () {
    parse_version ; 
    echo $major.$(($minor+1)).0b > version ; }

pre_major () {
    parse_version ; 
    echo $(($major+1)).0.0.0b > version ; }


bump_beta () {
    parse_version
    echo $major.$minor.${patch}b$((1+$beta)) > version ; }

bump_patch () {
    parse_version
    echo $major.$minor.$(($patch+1)) > version ; }

bump_minor () {
    parse_version
    echo $major.$(($minor+1)).0 > version ;}

# do not use, use pre_major instead
# bump_major () {
#     parse_version
#     echo $(($major+1)).0.0 > version ; }

stabilize () {
    parse_version
    echo $major.$minor.$patch > version ; }

### end of functions dealing with the version
###################




if [ -n "$1" ] ; then $1 || die "wrong argument: $1" ;  fi

if git branch | grep -q '^* master'; then    

    for f in `ls test_*.py`; do
        python $f || die "Unit tests failed" ; done 
    build_doc || die "Build documentation failed"  
    python setup.py sdist || die "Python package build failed"  return 1
    
elif git branch | grep -q '^* next'; then    

    for f in `ls test_*.py`; do
	python $f || die "Unit tests failed" ; done 
    build_doc || die "Build documentation failed"  
    python setup.py sdist || die "Python package build failed"  return 1

elif git branch | grep -q '^* debian'; then

    for f in `ls test_*.py`; do
	python $f || die "Unit tests failed" ; done 
    build_doc || die "Build documentation failed"
    dpkg-buildpackage ; fi

