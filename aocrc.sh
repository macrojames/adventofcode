# Add these to your ~/.bash_aliases

set AOC="~/workspace/adventofcode" # remember to change this to whatever your AOC directory is

alias aos="python3 solution.py < in.txt"
alias aot="cd $AOC; echo -ne '\\e[0;34m'; python3 solution.py < test.txt; echo -ne '\\e[0m'"
alias aoc="aot; echo; aos"

alias aoc-new="cd $AOC;"

function aoc-load () {
    pushd $AOC 2> /dev/null

    if [ $1 ]
    then
        y=$1
        d=$2
   else
        y=$(date +%Y)
        d=$(date +%d | sed 's/^0//g')
    fi

    echo "Checking for https://adventofcode.com/$y/day/$d"

    zd=`printf "%02d" "$d"`
    mkdir -p $y/inputs
    if [ ! -f "$y/inputs/$zd.input" ]; then
        aocd $y $d > $y/inputs/$zd.input && echo "Data loaded: $y/inputs/$zd.input"
    fi    
    if [ ! -f "$y/inputs/$zd.sample" ]; then
        aocd -e reference $y $d > $y/inputs/$zd.sample && echo "Data loaded: $y/inputs/$zd.sample"
    fi
    if [ ! -f "$y/$zd.py" ]; then
        if [ -f "$y/new.py" ]; then
            cp $y/new.py $y/$zd.py && echo "Template created: $y/$zd.py"
        else 
            cp 2023/new.py $y/$zd.py && echo "Template created: $y/$zd.py"
        fi
    fi
    if [ ! -f "$y/util.py" ]; then
        cp 2023/util.py $y/util.py && echo "File created: $y/$zd.py"
    fi
    popd 2> /dev/null
}