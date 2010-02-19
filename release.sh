build_doc () {

    set -e -x

    current_branch=`git branch | awk '/\*/ {print $2}'`
    version=`cat version`
    git checkout gh-pages
    git checkout next doc wordish.py interfaces.py version
    ( cd doc ; sphinx-build  . .. )
    rm -rf static sources images 
    mv {_,}sources
    mv {_,}static  
    mv {_,}images || true
    find . -name '*.html' -o -name '*.js' | \
	xargs sed -i 's/_static/static/g;s/_sources/sources/g;s/_images/images/g' 
    rm .buildinfo .doctrees/ -rf
    git rm -r doc wordish.py interfaces.py version -f
    rm -rf doc *.pyc
    git add * || true
    git commit -a -m "Updated the doc to version $version"
    git push origin gh-pages
    git checkout  $current_branch

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

bump_major () {
    parse_version
    echo $(($major+1)).0.0 > version ; }

bump_minor () {
    parse_version
    echo $major.$(($minor+1)).0 > version ;}

bump_patch () {
    parse_version
    echo $major.$minor.$(($patch+1)) > version ; }

bump_beta () {
    parse_version
    echo $major.$minor.${patch}b$((1+$beta)) > version ; }

stabilize () {
    parse_version
    echo $major.$minor.$patch > version ; }

pre_minor () {
    parse_version ; 
    echo $major.$(($minor+1)).0b > version ; }

pre_major () {
    parse_version ; 
    echo $(($major+1)).0.0.0b > version ; }

