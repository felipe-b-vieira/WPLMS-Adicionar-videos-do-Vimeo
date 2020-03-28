# WPLMS-Adicionar-videos-do-Vimeo
Código feito em wordpress usando rest api para poder adicionar vídeos do vímeo a partir de um csv.

Para utilizar é necessário ativar o API point para as units do WPLMS e adicionar os meta do vibe_types e vibe_durations simplesmente adicionando o código presente no txt no functions.php

Também é necessário gerar uma senha de api point através de plugin.
A primeira linha do arquivo contendo as aulas deve conter:

usuario,senhaapi,link do api endpoint do wordpress,id do autor
