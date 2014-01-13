
_hey_dewey()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"
    
    if [ $COMP_CWORD -eq 1 ]; then
        COMPREPLY=( $( compgen -W 'co new-branch nb workon pep8 hi checkout' -- $cur) )
    else
        case ${COMP_WORDS[1]} in
            co)
            _hey_dewey-co
        ;;
            new-branch)
            _hey_dewey-new-branch
        ;;
            nb)
            _hey_dewey-nb
        ;;
            workon)
            _hey_dewey-workon
        ;;
            pep8)
            _hey_dewey-pep8
        ;;
            hi)
            _hey_dewey-hi
        ;;
            checkout)
            _hey_dewey-checkout
        ;;
        esac

    fi
}

_hey_dewey-co()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"
    
    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -W '' -- $cur) )
    fi
}

_hey_dewey-new-branch()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"
    
    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -W '' -- $cur) )
    fi
}

_hey_dewey-nb()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"
    
    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -W '' -- $cur) )
    fi
}

_hey_dewey-workon()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"
    
    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -W '' -- $cur) )
    fi
}

_hey_dewey-pep8()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"
    
    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -W '' -- $cur) )
    fi
}

_hey_dewey-hi()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"
    
    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -W '' -- $cur) )
    fi
}

_hey_dewey-checkout()
{
    local cur
    cur="${COMP_WORDS[COMP_CWORD]}"
    
    if [ $COMP_CWORD -ge 2 ]; then
        COMPREPLY=( $( compgen -W '' -- $cur) )
    fi
}

complete -F _hey_dewey hey_dewey
complete -F _hey_dewey hey_dewey
complete -F _hey_dewey dewey
complete -F _hey_dewey d
