filetype on
"call pathogen#runtime_append_all_bundles()
filetype plugin indent on
set nocompatible
set modelines=0

syntax on
set backupdir=~/.vim/vim_backups
set undodir=~/.vim/vim_undos

set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab

set encoding=utf-8
set scrolloff=3
set autoindent
set showmode
set showcmd
set hidden
set wildmenu
set wildmode=list:longest
set visualbell
set cursorline
set ttyfast
set ruler
set backspace=indent,eol,start
set laststatus=2
set relativenumber
set undofile

" Leader key mappings
let mapleader = ","

"Search/move settings
nnoremap / /\v
vnoremap / /\v
set ignorecase

" Set default replace to global.
set gdefault

set incsearch
set showmatch
set hlsearch
nnoremap <leader><space> :noh<CR>
nnoremap <tab> %
vnoremap <tab> %

"For loooooooooong lines
set wrap
set textwidth=79
set formatoptions=qrn1
set colorcolumn=85

"Auto completion omnifunctions
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType python set omnifunc=pythoncomplete#Complete

" Fix color of autocomplete selected item background, expand all folders
highlight Pmenu ctermbg=238
highlight PmenuSel ctermfg=black
set foldlevel=1  " open all folds

"Apparently for some textmate compatibility.
"set list
"set listchars=tab:\ ,eol:

inoremap <up> <nop>
inoremap <down> <nop>
inoremap <left> <nop>
inoremap <right> <nop>

"Brilliant get rid of help key... which i hit whenever i hit Esc, wanted this
"for a long time

inoremap <F1> <ESC>
nnoremap <F1> <ESC>
vnoremap <F1> <ESC>

"the usual replace : with ; for save etc..
nnoremap ; :


" Save on lose focus, feature from Textmate
au FocusLost * :wa

"Strip all trailing whitespace in current file with <leader ><W>
nnoremap <leader>W :5s/\s\+$//<CR>:let @/=''<CR>

" Fold tag (Apparently good for html)
nnoremap <leader>ft Vatzf

"Sorting CSS properties
nnoremap <leader>S ?{<CR>jV/^\s*\}?$<CR>k:sort<CR>:noh<CR>

"Reselect just pasted text for operations like formatting,indenting etc..
nnoremap <leader>v V`]


"Open ~/.vimrc in a new vertical tab
nnoremap <leader>ev <C-w><C-v><C-l>:e $MYVIMRC<CR>


"Now for split-window based settings
",w for a new split window and switching to it

nnoremap <leader>w <C-w>v<C-w>1


