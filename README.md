# WPLMS-Adicionar-videos-do-Vimeo
Código feito em wordpress usando rest api para poder adicionar vídeos do vímeo a partir de um csv.

Para utilizar é necessário ativar o API point para as units do WPLMS e adicionar os meta do vibe_types e vibe_durations simplesmente adicionando o código presente no txt no functions.php

Também é necessário gerar uma senha de api point através de plugin.
A primeira linha do arquivo contendo as aulas deve conter:

usuario,senhaapi,link do api endpoint do wordpress,id do autor

//ATUALIZAÇÃO//

No plugin do WP Rest API Controller, alterar no arquivo classs-wp-rest-api-controller.php na pasta includes, mudar a função append_post_type_meta_data_to_api com o código abaixo:
'update_callback' => null,  com:
'update_callback' => 'update_post_meta_for_api',
Adicionar a função no php:
function update_post_meta_for_api( $value, $object, $field_name ) {

if ( ! $value ) {
    return;
}

return update_post_meta( $object->ID, $field_name, $value );
}

Além disso, ativar no plugin, o controle de curriculo e vibe_course_curriculum
