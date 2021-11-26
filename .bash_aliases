
#alias sudo='sudo '

#Vim aliases
alias vim='nvim'

#Alias for Trash and Desktop
alias rm='trash-put'
alias clear-desktop='trash-put ~/Desktop/*'

#cd aliases
alias ..='cd ..'

#ls aliases
alias ls='lsd'
alias la='lsd -A'
alias ll='lsd -l'
alias lla='lsd -lA'

#alias for store dot files in a bare git repo at $HOME/.dot-files-repo
alias cdf-git='/usr/bin/git --git-dir=$HOME/.dot-files-repo/ --work-tree=$HOME'
