die () { echo "$1" >&2 ; exit 1 ;  }

build_doc () {

    # here be fragons
    set -e -x

    current_branch=`git branch | awk '/\*/ {print $2}'`

    ( cd doc ; sphinx-build  . ../html )
    # switch to the doc repository, then checkout the doc sources
    git checkout gh-pages 
    git branch | grep -q '* gh-pages'  || return 1

    mv html/* .
    # adapt the sphinx layout to the github conventions
    rm -rf static sources images *.pyc .buildinfo .doctrees/
    mv {_,}sources
    mv {_,}static  
    mv {_,}images || true
    find . -name '*.html' -o -name '*.js' | \
	xargs sed -i 's/_static/static/g;s/_sources/sources/g;s/_images/images/g' 

    # commit the doc, push to github, back the current branch
    git commit -a -m "Updated the doc to version $version"
    # git push origin gh-pages
    git checkout  $current_branch
    git branch | grep -q "* $current_branch"  || return 1

}

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

pre_minor  () { echo $major.$(($minor+1)).0b		 > version ; }
pre_major  () { echo $(($major+1)).0.0.0b		 > version ; }

bump_beta  () { echo $major.$minor.${patch}b$((1+$beta)) > version ; }
bump_patch () { echo $major.$minor.$(($patch+1))	 > version ; }
bump_minor () { echo $major.$(($minor+1)).0		 > version ; }

stabilize  () { echo $major.$minor.$patch                > version ; }

if [ -n "$1" ] ; then 

    $1 || die "wrong argument: $1" ;
    parse_version 
    git commit -m "Updated version to `cat version`" version

if git branch | grep -q '^* master'; then    

    version=`cat version`
    for f in `ls test_*.py`; do
      python $f || die "Unit tests failed" ; done 

    build_doc || die "Build documentation failed"  
    python setup.py sdist || die "Python package build failed"

else 
    echo "Please release from the master branch,"
    echo "you are on the `git branch | awk '/\*/ {print $2}'` branch" ; fi    

