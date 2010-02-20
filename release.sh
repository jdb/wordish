#!/bin/bash

# ./release.sh  			-> test evrathing, say what would be uploaded
# ./release.sh upload			-> bump the patch if no b else bump the beta (check last_upload)
# ./release.sh bump_alpha upload	-> bump the patch if no b else bump the beta and upload (check last_upload)
# ./release.sh bump_alpha		-> bump the patch if no b else bump the beta and upload (check last_upload)


die () { echo "$1" >&2 ; exit 1 ;  }

build_doc () {

    set -e -x

    current_branch=`git branch | awk '/\*/ {print $2}'`

    if git status | grep -q -v "nothing to commit (working directory clean)"; 
    then git stash save "Stashing for building documentation"; fi
	
    ( cd doc ; sphinx-build -Q . ../html )
    git checkout gh-pages || return 1

    mv html/* .

    rm -rf static sources images *.pyc .buildinfo .doctrees/
    mv {_,}sources
    mv {_,}static  
    mv {_,}images || true
    find . -name '*.html' -o -name '*.js' | \
	xargs sed -i 's/_static/static/g;s/_sources/sources/g;s/_images/images/g' 


    git commit -a -m "Updated the doc to version $version"
    git checkout $current_branch || return 1

    if git stash list | grep -q "Stashing for building documentation" ;
	then git stash pop ; fi
}

new_version () {
    echo $1 > version
    git commit -m "Updated version to `cat version`" version
}

handle_version () {

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

    case "$1" in

	pre_minor  )  new_version $major.$(($minor+1)).0b	        ;; 
	pre_major  )  new_version $(($major+1)).0.0.0b		        ;; 

	bump_beta  )  new_version $major.$minor.${patch}b$((1+$beta))	;; 
	bump_patch )  new_version $major.$minor.$(($patch+1))	        ;; 
	bump_minor )  new_version $major.$(($minor+1)).0	        ;; 
	
	stabilize  )  new_version $major.$minor.$patch			;; 

	* )  ;;
    esac
}

# 1. Update the version as requested on the command line
version=`cat version`
if [ "$1" != upload ];
    then handle_version "$@" 
fi

# 1'. Never upload twice the same version: update the version if an
# upload is requested, and the current version is the last uploaded
# version (bump the beta if in beta, else bump the patch)

version=`cat version`
if ( [ "$1" = upload -o "$2" = upload ] ) \
    && [ $version = `cat .last_uploaded` ]; then

    if [ `expr index $version b` -eq 0 ] ;
    then handle_version bump_patch
    else handle_version bump_beta ; fi
fi

# 2. Do the tests, build the doc, build the python packaging
for f in `ls test_*.py`; do
    python $f || die "Unit tests failed" ; done
build_doc || die "Build documentation failed"  
python setup.py sdist || die "Python package build failed"


# 3. Eventually upload to pypi, to gh-pages, to master
if [ "$1" = upload -o "$2" = upload ]; then
    if git branch | grep -q '^* master' ; then    
	
	git status | grep "nothing to commit (working directory clean)" \
	    || die "release.sh must be called from a commited repository"
	set -e -x
	git checkout gh-pages
	git push origin gh-pages
	git checkout master
	python setup.py sdist  upload
	echo $version > .last_uploaded
	git commit -a -m "Released v$version"
	git tag v$version
	git push origin master
    else 
	echo "Please release from the master branch,"
	echo "you are on the `git branch | awk '/\*/ {print $2}'` branch" ; 
    fi    
fi